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
