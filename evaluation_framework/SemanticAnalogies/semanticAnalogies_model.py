import numpy as np
from evaluation_framework.abstract_model import AbstractModel

float_precision = 15


def default_analogy_function(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.array(b) - np.array(a) + np.array(c)


"""
Model of the semantic analogies task
"""


class SemanticAnalogiesModel(AbstractModel):
    """
    It initialize the model of the semantic analogies task

    task_name: name of the task
    top_k: the predicted vector is compared with all the vectors and the k nearest ones are depicted. If the actual vector is among the k nearest one, the task is considered correct
    debugging_mode: {TRUE, FALSE}, TRUE to run the model by reporting all the errors and information; FALSE otherwise
    analogy_function (optional): is the function to compute the analogy. It takes 3 vectors and returns the predicted one
    """

    def __init__(self, task_name, top_k, debugging_mode, analogy_function=None):
        self.debugging_mode = debugging_mode
        self.task_name = task_name

        if analogy_function is None:
            self.analogy_function = default_analogy_function
        else:
            self.analogy_function = analogy_function

        self.top_k = top_k
        if debugging_mode:
            print("SemanticAnalogies model initialized")

    """
    It trains the model based on the provided data
    
    vocab: dictionary of all the entities
    data: dataframe with entity name as first column, class label as second column and the vectors starting from the third column
    W: all the vectors in the input file (even if they are not present in the dataset used as gold standard)
    It returns the result object reporting the task name and the evaluation metrics.
    """

    def train(self, vocab, data, W):
        indices = np.array([[vocab[word] for word in row] for row in data])
        ind1, ind2, ind3, ind4 = indices.T

        predictions = np.zeros((len(indices), self.top_k))

        for j in range(len(indices)):
            pred_vec = self.analogy_function(
                W[ind1[j], :], W[ind2[j], :], W[ind3[j], :]
            )
            dist = np.dot(W, pred_vec.T)

            dist[ind1[j]] = -np.Inf
            dist[ind2[j]] = -np.Inf
            dist[ind3[j]] = -np.Inf

            predictions[j] = np.argsort(-dist, axis=0)[: self.top_k].T

        correct_predictions = 0
        for actual_entity, predicted_entities in zip(ind4, predictions):
            if actual_entity in predicted_entities:
                correct_predictions += 1
        total_predictions = len(predictions)
        accuracy = correct_predictions / total_predictions

        if self.debugging_mode:
            if total_predictions == 0:
                print("SemanticAnalogies : No data to check")
            else:
                print(
                    "SemanticAnalogies : ACCURACY TOP %d: %.2f%% (%d/%d)"
                    % (self.top_k, accuracy, correct_predictions, total_predictions)
                )

        return {
            "task_name": self.task_name,
            "top_k_value": self.top_k,
            "right_answers": correct_predictions,
            "tot_answers": total_predictions,
            "accuracy": round(accuracy, float_precision),
        }
