# dota2_predictor
dota2_predictor is an useful tool to predict results of your matches.
## Install
### **Requirement:**

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
or download the zip file from github

### **get data and set up:**

**1.Api key**

dota2_predictor get data via dota2api, so a steam api key is needed. If you haven't got one, get it from https://steamcommunity.com/dev/apikey (can't visit in Chinese mainland)

Then paste your api key in steam_api_key.txt

**2.Steam id**

Save your friends' and your steam ids in our_ids.txt like:

```
123456
654321
098765
```

**3.Images**

Run get_images.py to download images. 

**4.Get data**

Run get_matches.py to get data of matches of you and your friends. The more data you get, the more accurate the prediction will be.

## Start predicting
Run gui.py after completing the previous steps.

To update your data, you can just run get_matches.py again. 

If dota2 has an update involving new heroes, run get_id_name.py and get_images.py again.