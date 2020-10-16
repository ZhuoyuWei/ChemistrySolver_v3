# ChemistryQA Data


In the real world, there are QA tasks which cannot be solved by end-to-end neural networks and is very difficult to translate the natural language to any kind of formal representation which can be solved. Solving Chemical Calculation Problems is such a QA task. We collect about 5,000 chemical calculation problems from SOCRATIC.ORG, which cover more than 200 topic in chemistry. Unlike other QA datasets, we propose to only label the variable asked and conditions from question stem, but do not label the complex solving process. We name the dataset as ChemistryQA. To encourage other researchers to explore various solutions, we keep this task weakly supervised.


## Data

>Data

>>train.tsv

>>dev.tsv

>>test.tsv

## Evaluation

Please use evaluate.py to evaluate the result as following.
```
python evaluate.py {answer_predict.tsv} {answer_index} {predict_index}
```
where answer_predict.tsv should contain both correct answer and predicted answer by your method, and answer_index and predict_index represent the columne number of correct answer and predicted answer, respectively. 


## Citation

If you want to use ChemistryQA for your research, please cite as the following. 

```
@inproceedings{
anonymous2021chemistryqa,
    title={Chemistry{\{}QA{\}}: A Complex Question Answering Dataset from Chemistry},
    author={Zhuoyu Wei, Wei Ji, Xiubo Geng, Yining Chen, Baihua Chen, Tao Qin, Daxin Jiang},
    booktitle={Submitted to International Conference on Learning Representations},
    year={2021},
    url={https://openreview.net/forum?id=oeHTRAehiFF},
    note={under review}
}
```
