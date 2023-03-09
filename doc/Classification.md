## Classification

### Datasets used as gold standard

| **Dataset** | **Semantic of classes** | **Classes** | **Size** | **Source** |
| :---------: | :---------------------: | ----------: | -------: | :--------: |
|   PersonObjectPlace    |      Type of entities       |           3 |      540 |   KGRC-RDF-star   |
|   QT900     |  Type of quoted triples   |           3 |      900 |    KGRC-RDF-star     |

### Model and its configuration

| **Model** | **Configuration** |
| :---------: | :---------------------: |
| Naive Bayes | - |
| C 4.5 decision tree | - |
| k-NN | k=3 |
| Support Vector Machine | C = {10^{-3}, 10^{-2}, 0.1, 1, 10, 10^2, 10^3} |

**Missing entities** are simply ignored.

The results are calculated using stratified _10-fold cross-validation_.

### Output of the evaluation

| **Metric** | **Range** | **Optimum** |
| :---------: | :---------------------: | :----------: |
| Accuracy | \[0,1\] | Highest |
