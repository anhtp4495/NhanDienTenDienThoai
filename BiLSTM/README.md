The system achieved an F1 score of 92.05% on VLSP standard testset. The performance of our system with each feature set is 
described in the following table. 

| Word2vec | POS | Chunk | Regex |   F1   |
|:--------:|:---:|:-----:|:-----:|:------:|
|          |     |       |       | 62.87% |
|     x    |     |       |       | 74.02% |
|     x    |  x  |       |       | 85.90% |
|     x    |     |   x   |       | 86.79% |
|     x    |     |       |   x   | 74.13% |
|     x    |  x  |   x   |   x   | 92.05% |

## Installation

The input data's format of vie-ner-lstm follows VLSP 2016 campaign format. There are four columns in this dataset 
including of **word**, **pos**, **chunk**, and **named entity**. For details, see sample data in **'data'** directory.
The table below describes an example Vietnamese sentence in VLSP dataset.

| Word      | POS | Chunk | NER   |
|-----------|-----|-------|-------|
| Từ        | E   | B-PP  | O     |
| Singapore | NNP | B-NP  | B-LOC |
| ,         | CH  | O     | O     |
| chỉ       | R   | O     | O     |
| khoảng    | N   | B-NP  | O     |
| vài       | L   | B-NP  | O     |
| chục      | M   | B-NP  | O     |
| phút      | Nu  | B-NP  | O     |
| ngồi      | V   | B-VP  | O     |
| phà       | N   | B-NP  | O     |
| là        | V   | B-VP  | O     |
| dến       | V   | B-VP  | O     |
| được      | R   | O     | O     |
| Batam     | NNP | B-NP  | B-LOC |
| .         | CH  | O     | O     |

Path:

* ``word_dir``:       path for word dictionary
* ``vector_dir``:         path for vector dictionary
* ``train_dir``:   path for training data
* ``dev_dir``:      path for development data
* ``test_dir``:      path for testing data
* ``num_lstm_layer``:      number of LSTM layers used in this system
* ``num_hidden_node``:     number of hidden nodes in a hidden LSTM layer
* ``dropout``:      dropout for input data (The float number between 0 and 1)
* ``batch_size``:      size of input batch for training this system.
* ``patience``:      number used for early stopping in training stage

Download word2vector (1GB) and words.pl as follows:
([vector](https://drive.google.com/open?id=0BytHkPDTyLo9WU93NEI1bGhmYmc), 
[word](https://drive.google.com/open?id=0BytHkPDTyLo9SC1mRXpkbWhfUDA)) and put it into **embedding** directory.

# References
[Thai-Hoang Pham, Phuong Le-Hong, "The Importance of Automatic Syntactic Features in Vietnamese Named Entity 
Recognition" Proceedings of the 31th Pacific Asia Conference on Language, Information and Computation 
(PACLIC 31)](https://arxiv.org/abs/1705.10610)

Install:
- Keras
- Numpy
- codecs
- pickle
- pyvi (tokenized Vietnamse language)
- underthesea (POS tag)

Change the path by your path
Copy all file in C:\Users\BuiHung\PycharmProjects\untitled2  (our project)
Run only the file: NERner.py

You have to build:
- Save to your model
- Analysis your data
- Present your result and data on your website
- Demo on your website

All code in Python 3.5


