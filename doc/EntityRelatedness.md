## Entity Relatedness

### Datasets used as gold standard

| **Dataset** | **Structure** | **Size** |
| :---------: | :---------------------: | ----------: | 
|   [kgrc_entity_relatedness](./gold_standard_datasets.md#kgrc_entity_relatedness)    |  _Person entity_ with a sorted list of 10 _related entities_ | 210 entities |

### Model 
    sim_scores = []
    for each main entity as me:
      for each related entity as re:
        sim_scores.add(similarity_function(me,re))
      sort(sim_scores) //from more to less similar}

The _similarity\_function_ can be customized by the user.

Missing entities are managed as follows:
- if a main entity is missing, it is simply ignored;
- if one or more related entities attached to the same main entity are missing, first, the task compute the similarity among the available entities as reported in the model described in the below table; then, all the missing related entities are randomly put in the tail of the sorted list, and, finally, the evaluation metric is calculated on the ranking obtained by the similarity score among all the available pairs concatenated with the missing entities.

### Output of the evaluation

| **Metric** | **Range** | **Interpretation** |
| :---------: | :---------------------: | :----------: |
| Kendall's tau correlation coefficient | \[-1,1\] | Extreme values: correlation,   Values close to 0: no correlation |
