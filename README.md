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
    | Ollie       | 0.51        | 0.35          | 0.41          |
    | PropS       | 0.34        | 0.30          | 0.32          |
    | OpenIE-4    | 0.55        | 0.44          | 0.49          |
    | OpenIE-5    | 0.52        | 0.42          | 0.47          |
    | OpenIE-6    | <u>0.58</u> | 0.48          | <u>0.52</u>   |
    | ClausIE     | 0.41        | <u>0.50</u>   | 0.45          |
    | IMoJIE      | 0.59    | 0.49          | __0.54__      |
    | __ClausIE-DGNN__ | __0.63__        | __0.54__      | __0.58__      |

