## QT Similarity

### Datasets used as gold standard

| **Dataset** | **Structure** | **Size** |
| :---------: | :---------------------: | ----------: | 
|   QT50   | qt1 qt2 avg | 50 QTs |

### Model 
similarity(qt1, qt2)

The QT Similarity task simply ignores any *missing entities* and computes the similarity only on entities that both occur in the gold standard dataset and in the input file.

### Output of the evaluation

| **Metric** | **Range** | **Interpretation** |
| :---------: | :---------------------: | :----------: |
| Pearson correlation coefficient (P\_cor) | \[-1,1\] | Extreme values: correlation, Values close to 0: no correlation |
| Spearman correlation coefficient (S\_cor) | \[-1,1\] | Extreme values: correlation, Values close to 0: no correlation |
| Harmonic mean of P\_cor and S\_cor  | \[-1,1\] | Extreme values: correlation, Values close to 0: no correlation |
