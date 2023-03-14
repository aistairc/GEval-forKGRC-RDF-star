# GEval for KGRC-RDF-star
[![Apache-2.0 License](https://img.shields.io/github/license/mariaangelapellegrino/Evaluation-Framework)](https://github.com/mariaangelapellegrino/Evaluation-Framework/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository is an extension of [GEval](https://github.com/mariaangelapellegrino/Evaluation-Framework). 

This repository contains a (software) evaluation framework to perform evaluation and comparison on *RDF-star graph embedding techniques*. 

## How to use

If you want to run the tools, install Jupyter and run it on your host.

```bash
jupyter notebook
```

Example of Classification Task

run [evaluation_rdfstar2vec.ipynb](evaluation_rdfstar2vec.ipynb)

Example of interpretation of the results

run [tutorial_results_interpretation/results_interpretation_rdf-star2vec.py.ipynb](tutorial_results_interpretation/results_interpretation_rdf-star2vec.py.ipynb)


## Tasks 
The implemented tasks are:

- Machine Learning 
	* [Classification](./doc/Classification.md) 
	* [Clustering](./doc/Clustering.md)

- Semantic tasks 
	* [Entity Relatedness](./doc/EntityRelatedness.md) 
	* [QT Similarity](./doc/DocumentSimilarity.md) 

<!--    
Each task follows the same workflow:
1.  the task manager asks data manager to merge each gold standard dataset and the input file and keeps track of both the retrieved vectors and the **missing entities**,  i.e.,  entities  required  by  the  gold  standard  dataset,  but  absent  in the input file;
2.  a model for each configuration is instantiated and trained;
3.  the missing entities are managed: it is up to the task to decide if they should affect the final result or they can be simply ignored;
4.  the scores are calculated and stored.

You can separately analyze each task by following its link. You will find details related to the used gold standard datasets, the configuration of the model(s), and the computed evaluation metrics.

## Framework details
### Parameters

|       Parameter      |                     Default                    |                                                      Options                                                      | Mandatory |       Used\_by      |
|:--------------------:|:----------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|:---------:|:-------------------:|
|     vector\_file    |                        -                       |                                                  vector file path                                                 |     <ul><li>- [x] </li></ul>    |         all         |
| vector\_file\_format |                       TXT                      |                                                     TXT, HDF5                                                     |           |    data\_manager    |
|     vector\_size     |                       200                      |                                                   numeric value                                                   |           |    data\_manager    |
|         tasks        |                      \_all                     |                                       Class, Reg, Clu, EntRel, DocSim, SemAn                                      |           | evaluation\_manager |
|       parallel       |                      False                     |                                                      boolean                                                      |           | evaluation\_manager |
|    debugging\_mode   |                      False                     |                                                      boolean                                                      |           |          *          |
|  similarity\_metric  |                     cosine                     | [Sklearn affinity metrics](https://scikit-learn.org/stable/modules/classes.html\#module-sklearn.metrics.pairwise) |           |     Clu, DocSim     |
|   analogy\_function  | None (to use the _default\_analogy\_function_) |                                                handler to function                                                |           |  semantic\_analogy  |
|        top\_k        |                        2                       |                                                   numeric value                                                   |           |        SemAn        |
|     compare\_with    |                      \_all                     |                                                  list of run IDs                                                  |           | evaluation\_manager |

### Vector file format
The input file can be provided either as a plain text (also called **TXT**) file or as a [**HDF5**](https://www.hdfgroup.org/solutions/hdf5/).

The **TXT** file must be a white-space separated value file with a line for each embedded entity. Each row must contain the IRI of the embedded entity - without angular brackets - and its vector representation. 


<!--The **HDF5** vectors file must be an H5 file with a single `group` called `Vectors`. 
In this group, there must be a `dataset` for each entity with the `base32 encoding` of the entity name as the dataset name and the embedded vector as its value.-->

<!--
### Running details

The evaluation framework can be run from the command line. Users can customize the evaluation settings by: 
1) specifying parameters on the command line (useful when only a few settings must be specified and the user desires to use the default value for most of the parameters);
2) organizing them in an XML file (especially useful when there is the need to define most of the parameters); 
3) passing them to a function that starts the evaluation. 

In the **example** folder of the project on GitHub, there are examples for the different ways to provide the parameters.

To execute one of them you can move the desired *main* file at the top level of the project and then run it.

**Note**: The tasks can be executed sequentially or in parallel. If the code raises MemoryError it means that the tasks need more memory than the one available. In that case, run all the tasks sequentially.

### Results storage

For each task and each file used as a gold standard, the framework will create 
1) an output file that contains a reference to the file used as a gold standard and all the information related to evaluation metric(s) provided by each task, 
2) a file containing all the **missing** entities, 
3) a log file reporting extra information, occurred problems, and execution time, 
4) information related to the comparison with previous runs. 
In particular, about the comparison, it reports the values effectively considered in the comparison and the ranking of the current run upon the other ones. The results of each run are stored in the directory _results/result\_<starting time of the execution>_ generated by the evaluation manager in the local path.
    
In **Evaluation-Framework/tutorial_results_interpretation** folder you can find some tutorials to interpret results.

-->

## Dataset
	
We used [KGRC-RDF-star](https://github.com/aistairc/KGRC-RDF-star).

Please see **[here](doc/gold_standard_datasets.md)** for more information about gold standard datasets.
	
## Dependencies
The framework is tested to work with Python 3.8.3.

The required dependencies are: `Numpy==1.14.0, Pandas==0.22.0, Scikit-learn==0.19.2, Scipy==1.1.0, H5py==2.8.0, unicodecsv==0.14.1`.

## License
The Apache license applies to the extended source code. The CC BY 4.0 applies to the gold standard datasets ([PersonObjectPlace, QT900](evaluation_framework/Classification/data/README.md), [kgrc_entity_relatedness](evaluation_framework/EntityRelatedness/data/README.md), [QT50](evaluation_framework/DocumentSimilarity/data/README.md)). The license of the original software can be found [here](https://github.com/mariaangelapellegrino/Evaluation-Framework). For source datasets, please check the license information [here](https://github.com/aistairc/KGRC-RDF-star#license).