from scipy.stats import spearmanr
from scipy.stats import pearsonr
import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances
from evaluation_framework.abstract_model import AbstractModel

float_precision = 15

"""
Model of the Document similarity task
"""


class DocumentSimilarityModel(AbstractModel):
    """
        It initialize the model of the classification task

    task_name: name of the task
    distance_metric: distance metric used to compute the similarity score
    with_weights: {TRUE, FALSE} if the evaluation metric should consider the weights provided by the annotator or not
    debugging_mode: {TRUE, FALSE}, TRUE to run the model by reporting all the errors and information; FALSE otherwise
    """

    def __init__(self, task_name, distance_metric, with_weights, debugging_mode):
        self.debugging_mode = debugging_mode
        self.task_name = task_name
        self.distance_metric = distance_metric
        self.with_weights = with_weights
        if self.debugging_mode:
            print("Document similarity model initialized")

    """
    It trains the model based on the provided data
    
    data: dataframe with entity name as first column, and the vectors starting from the second column
    stats: it contains the data used as gold standard
    
    It returns the result object reporting the task name, the used configuration and the evaluation metrics.
    """

    def train(self, data, stats):
        doc_similarity, log_info = self.compute_doc_distance(data)
        gold_similarity_score, similarity_score = self.get_gold_and_actual_score(
            stats, doc_similarity
        )
        (
            pearson_score,
            spearman_score,
            harmonic_mean,
        ) = self.evaluate_document_similarity(gold_similarity_score, similarity_score)

        if self.with_weights:
            conf = "without_weights"
        else:
            conf = "with_weights"

        return {
            "task_name": self.task_name,
            "conf": conf,
            "pearson_score": round(pearson_score, float_precision),
            "spearman_score": round(spearman_score, float_precision),
            "harmonic_mean": round(harmonic_mean, float_precision),
        }, log_info

    """
    It computes the predicted document distance
    
    data: dataframe with entity name as first column, class label as second column and the vectors starting from the third column
    
    It returns 
    	the dataframe containing the similarity for each pair of documents;
    	log_info which reports all the problems occurred
    """

    def compute_doc_distance(self, data):
        log_info = ""

        result_dict = {}
        doc1_list = list()
        doc2_list = list()
        doc_similarity = list()

        for i in range(1, 51):
            # 1. extract entities of document i and j
            set1 = self.extract_entities(i, data)
            if len(set1) == 0:
                log_info += "Document Similarity: No entities in doc " + str(i) + "\n"
                continue

            for j in range(i, 51):
                set2 = self.extract_entities(j, data)
                if len(set2) == 0:
                    log_info += (
                        "Document Similarity: No entities in doc " + str(j) + "\n"
                    )
                    continue

                # 1. DONE : set 1 and set 2 contain entities of document i and j

                # 2. compute the similarity for each pair of entities in d_i and d_j
                # similarity is interpreted as the opposite of distance
                similarity_score1 = self.compute_similarity(set1, set2)
                similarity_score2 = self.compute_similarity(set2, set1)
                if (
                    self.with_weights
                ):  # if weights are enabled - multiply distances with weight matrix
                    similarity_score1 = similarity_score1 * np.outer(
                        set1["weight"], set2["weight"]
                    )
                    similarity_score2 = similarity_score2 * np.outer(
                        set2["weight"], set1["weight"]
                    )

                # 3. for each entity in d_i identify the maximum similarity to an entity in d2, and viceversa
                max_sim1 = np.max(similarity_score1, axis=1)
                max_sim2 = np.max(similarity_score2, axis=1)

                # 4. calculate document similarity
                document_similarity = (sum(max_sim1) + sum(max_sim2)) / (
                    len(max_sim1) + len(max_sim2)
                )

                if self.debugging_mode:
                    print(
                        "Doc "
                        + str(i)
                        + " - Doc "
                        + str(j)
                        + " : distance similarity "
                        + str(document_similarity)
                    )

                doc1_list.append(i)
                doc2_list.append(j)
                doc_similarity.append(document_similarity)

        result_dict["doc1"] = doc1_list
        result_dict["doc2"] = doc2_list
        result_dict["similarity"] = doc_similarity

        return pd.DataFrame(result_dict), log_info

    """
    It returns the document similarity value used as gold standard and the actual one
    
	gold_stats: dataframe containing data used as gold standard
	actual_stats: dataframe containing the predicted results
    """

    def get_gold_and_actual_score(self, gold_stats, actual_stats):
        merged = pd.merge(gold_stats, actual_stats, on=["doc1", "doc2"], how="inner")
        return (merged.iloc[:, 2], merged.iloc[:, 3])

    """
    It evaluates the predicted document similarity against the document similarity used as gold standard.
    
    gold_similarity_score: array containing the document similarity used as gold standard
    similarity_score: array containing the actual document similarity score
    """

    def evaluate_document_similarity(self, gold_similarity_score, similarity_score):
        spearman_score, _value = spearmanr(gold_similarity_score, similarity_score)
        pearson_score, _value = pearsonr(gold_similarity_score, similarity_score)
        harmonic_mean = (2 * pearson_score * spearman_score) / (
            pearson_score + spearman_score
        )
        return pearson_score, spearman_score, harmonic_mean

    """
    It extracts the entities related to the document in input from the whole entities dataframe
    
    documentID: current document ID as integer from 1 to 50
    data: dataframe containing documentID in the doc column, the entity in the document and the weight returned by the annotator
        """

    def extract_entities(self, documentID, data):
        set1 = data[data["doc"] == documentID]
        if len(set1) == 0:
            if self.debugging_mode:
                print("No entities in doc " + str(documentID))
        else:
            set1 = set1.sort_values("weight", ascending=False).drop_duplicates(
                subset="name", keep="first"
            )
        return set1

    """
    It computes the similarity among all the entities in the provided inputs.
    
    set1, set2: dataframe containing the entities of a document
    
    It returns the pairwise distance of all the pairs in the dataframes provided in input
    """

    def compute_similarity(self, set1, set2):
        return 1 - pairwise_distances(
            set1.iloc[:, 3:], set2.iloc[:, 3:], metric=self.distance_metric
        )
