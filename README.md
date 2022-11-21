# DGnnIE: Dependency Graph Neural Network based Open Information Extraction

## Requirements
- Ubuntu 18.04
- python>=3.7
- pytorch>=1.6
- [torchtext](https://pypi.org/project/torchtext/)
- graph4nlp
- [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/download.html) for dependnecy parsing

## Dataset
- Training set is from __imojie__, the original set can download from [here](https://github.com/dair-iitd/imojie) by running __download_data.sh__ 
1. Training set:
    By running
    ```
    python process_imojie_train_dataset.py
    ```
    you can get `train_1w.json`, `train_3w.json` and `train_9w.json` in `/raw` folder

2. Val and test set is placed in `/raw` folder named as `val.json` and `test.json`, they are from [CaRB](https://github.com/dair-iitd/CaRB)
    
    ⚠ Noting that because DGnnIE only considers binary extraction, the `val` and `test` are processed by filtering out n-ary extractions, running
    ```python
    python process_carb_val_and_test_dataset.py
    ``` 

## Train model
```bash
bash train.sh
```

## Inference
```bash
bash inference.sh
```
with `single input` and `batch input`

## Performance
1. [Training log](./out/gcn_bi_sep_l2_ckpt/metric.log)
    - with BLEU score `BLEU_1 = 0.64975, BLEU_2 = 0.59110, BLEU_3 = 0.53981, BLEU_4 = 0.49458`

2. [Performance on CaRB](./out/gcn_bi_sep_l2_ckpt/carb.log)

    |  System     | Precision   | Recall        |     F1        |
    | :---:       |    :----:   |     :---:     |     :---:     |
    | Ollie       | 0.59        | 0.46          | 0.52          |
    | ClausIE     | 0.53        | 0.62          | 0.57          |
    | PropS       | 0.45        | 0.36          | 0.40          |
    | OpenIE-4    | 0.63        | 0.58          | 0.60          |
    | OpenIE-5    | 0.58        | 0.57          | 0.57          |
    | RnnOIE      | -           | -             | 0.50          |
    | SpanOIE     | -           | -             | 0.48          |
    | IMoJIE      | 0.66        | 0.55          | 0.60          |
    | OpenIE-6    | 0.65        | 0.56          | 0.60          |
    | __DGnnIE__ | __0.70__     | __0.66__      | __0.68__      |

