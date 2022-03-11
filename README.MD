# Tweet Panda
## Tweet Panda is a python object that helps you quickly extract meaningful data from Twitter datasets.
### It is built on top of pandas dataframes, delivering simple methods to extract information such as top hashtags, hashtag time series, rank user accounts, and more.

### Installation
```shell
git clone https://github.com/Gui-Luz/TweetPanda.git
pip install -r requirements.txt
```
### Creating a Tweet Panda object
If you are working with a [twint](https://github.com/twintproject/twint) generated dataset you can simple pass your file as an argument:
```python
from tweet_panda import TweetPanda

tp = TweetPanda(file='my_twint_dataset.csv')
```
If you have a dataset from a different source you should also specify the dataset columns that you are using:
```python
from tweet_panda import TweetPanda
tp = TweetPanda(file='my_twiter_dataset.csv', date='date_column_name', username='username_column_name', 
                name='name_column_name', tweet='tweet_column_name', replies_count='replies_column_name', 
                retweets_count='retweet_column_name', likes_count='likes_column_name')
```
### Methods
```python
>>>from tweet_panda import TweetPanda
>>>tp = TweetPanda(file='#FridayFellings.csv')
```
```python3
>>>tp.rank_usernames()

    paulcurtis1956     17
    brcctlc             4
    top50clean          3
    politribune         2
    iservedrinks        2
```
```python3
>>>tp.rank_hashtags()

    FridayFeeling      82
    Friday             24
    Weekendvibes       17
    Happyweekend       17
    Fun                17
```
```python3
>>>tp.rank_mentions()

    MichelleHardie6             1
    spooooookyszn               1
    VisionaryMinds2             1
    terrinakamura               1
    TammyReeseMedia             1
    FORKSTER_2013               1
```
```python3
>>>tp.rank_urls()

    https://t.co/YC65EIiAot     1
    https://t.co/OFicTUzgOO     1
    https://t.co/y6MTofOh2k     1
    https://t.co/InF9F72WY8     1
    https://t.co/p7ADdhzsB5     1
```
```python3
>>>tp.sort_by_replies()

           date         username                                              tweet  ... replies_count  retweets_count  likes_count
26   2022-03-11         ouchyomh  Which song do you prefer?   Run to the Hills o...  ...             7               0            6
29   2022-03-11      brynbentley  My #Snapchat got deleted. Anyways.. #HappyFrid...  ...             2               0            1
96   2022-03-11        ohrabbits  Tell me your favorite flower and (as a florist...  ...             2               0            2
21   2022-03-11       top50clean  Hit Rewind CLEAN:  🥇 Ruth B. (9 days) 🥈 Sam Sm...  ...           1               0            0
92   2022-03-11       top50clean  All Out 90s CLEAN:  🥇 Backstreet Boys (9 days)...  ...            1               0            0
```
```python3
>>>tp.sort_by_retweets()

           date         username                                              tweet   replies_count  retweets_count  likes_count
68   2022-03-11    rappcatsadopt  ✨Introducing Cyrus✨This young kitty was rescue...           0              18           58
89   2022-03-11          jaouitv  🥳 #FridayFeeling GIFT CARD GIVEAWAY 🥳  RETWEET...           0               6            5
98   2022-03-11    thesoulfulemu  Sharing #FRIDAYvibes ♥️ with ALL-STAR Tweeple ...              1               5            5
64   2022-03-11   thisismarietta  This is the moment a 6-month-old baby koala ca...             0               3           13
25   2022-03-11             nhms  Current #FridayFeeling. 😃  https://t.co/vt5TBt...            1               2            7
```
```python3
>>>tp.sort_by_likes()

           date        username                                              tweet  ... replies_count  retweets_count  likes_count
68   2022-03-11   rappcatsadopt  ✨Introducing Cyrus✨This young kitty was rescue...  ...           0              18           58
7    2022-03-11  sienkiewiczart      #FridayFeeling #Dune  https://t.co/pzsPLfw7ZQ  ...             1               1           15
64   2022-03-11  thisismarietta  This is the moment a 6-month-old baby koala ca...  ...             0               3           13
78   2022-03-11        pentapod  Daily coworker photo: Friday feels! And Friday...  ...             1               1           12
35   2022-03-11      tomfolanmd  Radiologists heading for exit at 4:59pm   #Fri...  ...             0               0            8
```
```python3
>>>tp.get_time_series()

date
2022-03-11      110
2022-03-10      32    
2022-03-09      30
2022-03-08      29
2022-03-07      45    
```
