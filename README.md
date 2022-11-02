# GraphOIE

## Requirements
- Ubuntu 18.04
- python>=3.7
- pytorch>=1.6
- [torchtext](https://pypi.org/project/torchtext/)
- graph4nlp
- [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/download.html) for dependnecy parsing

## Dataset
- Train set is from __imojie__, the original can download from [here](https://github.com/dair-iitd/imojie) by running __download_data.sh__ 
1. Train set:
    By running
    ```
    python process_imojie_train_dataset.py
    ```
    you can get `train_1w.json`, `train_3w.json` and `train_9w.json` in `/raw` folder

2. Val and test set is placed in `/raw` folder named as `val.json` and `test.json`, they are from [CaRB](https://github.com/dair-iitd/CaRB)

## Train
```bash
bash train.sh
```
## Inference
```bash
bash inference.sh
```

## Performance
- [训练日志](./out/gcn_bi_sep_l2_ckpt/metric.log)

|  System     | Precision   | Recall        |     F1        |
| :---:       |    :----:   |     :---:     |     :---:     |
| Ollie       | 0.51        | 0.35          | 0.41          |
| PropS       | 0.34        | 0.30          | 0.32          |
| OpenIE-4    | 0.55        | 0.44          | 0.49          |
| OpenIE-5    | 0.52        | 0.42          | 0.47          |
| OpenIE-6    | 0.58        | 0.48          | 0.52          |
| ClausIE     | 0.41        | 0.50          | 0.45          |
| IMoJIE      | __0.59__    | 0.49          | 0.54          |
| __GraphIE__ | 0.53        | __0.54__      | __0.54__      |

