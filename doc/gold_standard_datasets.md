# Gold standard datasets

## Contents
- [PersonObjectPlace](#personobjectplace)
- [QT900](#qt900)
- [kgrc_entity_relatedness](#kgrc_entity_relatedness)
- [QT50](#qt50)
- [Prefix](#prefix)

## PersonObjectPlace

[Download](../evaluation_framework/Classification/data/kgrc_person_object_place.tsv)

PersonObjectPlace contains pairs of entities and labels, the labels classified into <i>Person</i>, <i>Object</i>, and <i>Place</i>.
It is an unbiased dataset randomly extracted from the [KGRC-RDF-star](https://github.com/aistairc/KGRC-RDF-star) using SPARQL queries and designed to have an equal number of each class.

Therefore, the PersonObjectPlace dataset contains 540 entities with cluster labels based on its rdf:type information (# of Person: 180, # of Object: 180, # of Place: 180). 

## QT900

[Download](../evaluation_framework/Classification/data/kgrc_qt900.tsv)

QT900 contains pairs of QTs and labels, the labels classified into <i>Situation</i>, <i>Statement</i>, and <i>Thought</i>, and it is also an unbiased dataset desined to have an equal number of each class. It is also an unbiased dataset randomly extracted from the [KGRC-RDF-star](https://github.com/aistairc/KGRC-RDF-star) using SPARQL queries and designed to have an equal number of each class.

Therefore, the QT900 contains 900 QTs with cluster labels based on its rdf:type information (# of Scene=300, # of Situation=300, # of Thought=300).

## kgrc_entity_relatedness

[Download](../evaluation_framework/EntityRelatedness/data/kgrc_entity_relatedness.txt)

The kgrc_entity_relatedness is a set of 21 person entities extracted from the KGRC-RDF-star and 10 entities related to each person, and the related entities are sorted by their relatedness.
This gold standard dataset was created as follows, referring to the methodology of [KORE](https://doi.org/10.1145/2396761.2396832).

1. Twenty-one person entities are extracted as seed entities from the KGRC-RDF-star.
2. Ten candidates are extracted based on the sorted lists of entities that co-occur with the seed entity in the same scenes (210 in total).
3. All possible comparisons of the 10 candidates with respect to their seed are created (945 in total).
4. Amazon Mechanical Turk (MTurk) workers are asked which of the given two entities is more related to the seed entity. Ten workers answer each question.
5. Ten comparison pairs are created as the gold standard by authors to improve the quality of the crowdsourcing task. Spam workers are removed based on the answers for these pairs.
6. All comparisons are aggregated into a single confidence that one entity is more (or equally) related to the seed.
7. The 10 candidate entities are ranked by these confidence values.

## QT50

[Download score data](../evaluation_framework/DocumentSimilarity/data/LP50_averageScores.csv)  
[Download label data](../evaluation_framework/DocumentSimilarity/data/LP50_entities.json)

QT50 is a set of similarity scores among fifty QTs.
QT50 was created with the following steps, using the methodology of [LP50](https://hdl.handle.net/2440/28910).
1. Fifty QTs and the scene descriptions corresponding to the QTs are extracted from KGRC-RDF-star and KGRC.
2. All possible pairs of the 50 QTs are created (1,225 in total).
3. MTurk workers judge the similarity on a five-point scale (with one indicating "not similar at all" and five indicating "quite similar"). Each question is answered by 10 workers.
4. Five pairs are created as the gold standard by authors to improve the quality of the crowdsourcing task. Spam workers are removed based on the answers for these pairs.
5. The average similarity scores of each pair are calculated.

## Prefix
The following prefixes are used in the URI of the entity.

| Prefix | URI                                                 |
|--------|-----------------------------------------------------|
| ac:    | http://kgc.knowledge-graph.jp/data/ACaseOfIdentity/ |
| ag:    | http://kgc.knowledge-graph.jp/data/AbbeyGrange/     |
| cm:    | http://kgc.knowledge-graph.jp/data/CrookedMan/      |
| dm:    | http://kgc.knowledge-graph.jp/data/DancingMen/      |
| df:    | http://kgc.knowledge-graph.jp/data/DevilsFoot/      |
| rp:    | http://kgc.knowledge-graph.jp/data/ResidentPatient/ |
| sl:    | http://kgc.knowledge-graph.jp/data/SilverBlaze      |
| sb:    | http://kgc.knowledge-graph.jp/data/SpeckledBand     |
| kdp:   | http://kgc.knowledge-graph.jp/data/predicate/       |
| kgc:   | http://kgc.knowledge-graph.jp/ontology/kgc.owl#     |
| rdf:   | http://www.w3.org/1999/02/22-rdf-syntax-ns#         |
| rdfs:  | http://www.w3.org/2000/01/rdf-schema#               |
| owl:   | http://www.w3.org/2002/07/owl#                      |

## License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">GEval for KGRC-RDF-star</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/Ease112/GEval-forKGRC-RDF-star" property="cc:attributionName" rel="cc:attributionURL">Shusaku Egami</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/aistairc/KGRC-RDF-star" rel="dct:source">https://github.com/aistairc/KGRC-RDF-star</a>.