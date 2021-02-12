# Dota2 Predictor
Dota2 Predictor is a program based on mechine learning to predict results of Data2 matches. It can automatically obtain the game data of designated players, and predict the results of their future games according to the heroes selected in these games.
## 1. Install
### 1.1 Download
Requirement:

- Python 3.x
- Python packages:
- - dota2api
- - sklearn
- - pandas
- - numpy
- - requests

Then download this program via:

```
git clone https://github.com/ccpcc/dota2_predictor.git
```
or download the [zip file.](https://github.com/ccpcc/dota2_predictor/archive/master.zip)

### 1.2 Get Data and Set Up:

**1.2.1 Api key**

dota2_predictor get data via dota2api, so a steam api key is needed. If you haven't got one, get it from https://steamcommunity.com/dev/apikey (can't visit in Chinese mainland)

Then paste your api key in steam_api_key.txt

**1.2.2 Steam id**

Save your friends' and your steam ids in our_ids.txt like:

```
123456
654321
098765
```

**1.2.3 Images**

Run get_images.py to download images. 

**1.2.4 Get data**

Run get_matches.py to get data of matches of you and your friends. The more data you get, the more accurate the prediction will be.

## 2. Start predicting
Run gui.py after completing the previous steps.

To update your data, you can just run get_matches.py again. 

If dota2 has an update involving new heroes, run get_id_name.py and get_images.py again.

## 3. Algorithm and Evaluation
In the development of this program, 653 matches of my friends and me were used. The model selection and final evaluation are as follows.
### 3.1 Data Set Partition
First, the dataset is divided into training set, validation set and test set according to the scale shown in the figure below. The training set is used to trian models, the validation set is used to determined hyperparameters and the test set is used for final evaluation .

![image](http://cccpcccai.top/Imgs/dataset.jpg)
### 3.2 Model Selection
Various algorithms are tried and their hyperparameters are determined by maximizing the accuracy on validition set. (shown as the figure below) 

![image](http://cccpcccai.top/Imgs/hyperparameters.jpg)

After determining hyperparameters, the accuracy and the area of the ROC curve (noted as ROC scores) on the test set of the three algorithms which perform well on the validation set are calculated. (shown as the figure below)

![image](http://cccpcccai.top/Imgs/scores.jpg)

After considering the accuracy and the ROC scores, Naive Bayes model is selected.
### 3.3 Evaluation
The accuracy on test set of the model is 0.586 and the ROC score is 0.622. The ROC curve is shown in the figure below.

![image](http://cccpcccai.top/Imgs/ROC.jpg)

In summary, Dota2 Predictor is not robust enough to predict every matches accurately because of the randomness of Dota2. But, it can reflect the likelihood of winning or losing a game for designated players to some extent.

 