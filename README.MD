# Tweet Panda
## Tweet Panda is a python object that helps you quickly extract meaningful data from Twitter datasets.
### It is built on top of [Pandas](https://pandas.pydata.org/) dataframes, delivering simple methods to extract information such as top hashtags, hashtag time series, rank user accounts, and more.

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
````python
>>>tp.save_csv(file_name='my_time_series.csv', method='get_time_series')
# Saves the result of another method into a csv file
````
````python
tp.print_results('sort_by_replies', 10)
           date         username                                name                                                                                                                                                                                                                                                                            tweet  replies_count  retweets_count  likes_count
0    2022-03-11         ouchyomh   "Ouch, You're on my Hair" Podcast                  Which song do you prefer?   Run to the Hills or One   Every song today is by either #IronMaiden or #Metallica   #rockband #rock #hardrock #heavymetal #Retweet #Trending #FridayFeeling #FridayMotivation #vocals #guitar #drums #bass  https://t.co/kY7OqLBycs              7               0            6
1    2022-03-11      brynbentley                        Bryn Bentley                                                                                                                                                      My #Snapchat got deleted. Anyways.. #HappyFriday #selfie #SelfPortrait #FridayFeeling #FridayVibes  https://t.co/JxERoqD4Jd              2               0            1
2    2022-03-11        ohrabbits                   Grace Hertenstein                                                                                                                                     Tell me your favorite flower and (as a florist) I will tell you how I feel about that particular bloom 🌼🌾🌿  #FridayFeeling #Flowers #florist              2               0            2
3    2022-03-11       top50clean    Top 50 Clean - Spotify Playlists  Hit Rewind CLEAN:  🥇 Ruth B. (9 days) 🥈 Sam Smith 🥉 Julia Michaels, Niall Horan 4️⃣ MKTO 5️⃣ One Direction ⬆️ 6️⃣ Rita Ora ⬆️ 7️⃣ Taylor Swift ⬇️ 8️⃣ Gym Class Heroes, Adam Levine ⬇️ 9️⃣ David Guetta, Kid Cudi 🔟 Bruno Mars  #FridayFeeling #Friday  https://t.co/LtVeKy7aah              1               0            0
4    2022-03-11       top50clean    Top 50 Clean - Spotify Playlists                 All Out 90s CLEAN:  🥇 Backstreet Boys (9 days) 🥈 Britney Spears 🥉 Spice Girls 4️⃣ Oasis 5️⃣ Coolio, L.V. 6️⃣ Sixpence None The Richer 7️⃣ 2Pac, Roger, Dr. Dre 8️⃣ Natalie Imbruglia 9️⃣ Cher 🔟 Destiny's Child  #FridayFeeling #Friday  https://t.co/H55dkWMSOD              1               0            0
..          ...              ...                                 ...                                                                                                                                                                                                                                                                              ...            ...             ...          ...
105  2022-03-11  adventurelarry1             Adventure with Larry 🚌💙                                                                                                                                         To book an adventure with Larry follow web link in bio 💙 #traveling #lakedistrict #FridayFeeling #adventuretime  https://t.co/e5gl2uas9K              0               0            0
106  2022-03-11         mrsdill2                             MrsDill                                                                                                                                                                                      I’ve heard of “time flying” but wow!  😂 #timechange #FridayFeeling  https://t.co/oHa3Q3w4V2              0               0            1
107  2022-03-11       tomfolanmd                      Tom Folan 🇮🇪🇺🇦                                                                                                                                                                                             Radiologists heading for exit at 4:59pm   #FridayFeeling     https://t.co/e0Bsc1lrQX              0               0            8
108  2022-03-11   dwdpodcast2021          Death with Dignity Podcast                                       Having a terminal disease sucks but one can always stop and appreciate the beauty in little things.  Enjoy the sunshine, smell a flower, believe in the good and be the #good. #FridayFeeling #CANCER #MedicalAidinDying #DeathwithDignity              0               1            0
109  2022-03-11      305mosquito  Miami-Dade County Mosquito Control              #FridayFeeling: stay #mosquito bite free today and all weekend by applying an @EPA-registered #repellent before venturing outdoors. Bonus tip: apply your sunscreen first, then your repellent. Find out which type is best for you here:  https://t.co/hvdCBiHvf8.              0               0            0

````
### Properties
````python
### accessing the pandas dataframe for regular pandas manipulation
>>>df = tp.df
>>>df.head(2)

         date       username  ... likes_count count
0  2022-03-11  mtorezwriting  ...           0     1
1  2022-03-11        brcctlc  ...           0     1
[2 rows x 8 columns]
````

