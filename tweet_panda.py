import pandas as pd
import re


class TweetPanda:
    def __init__(self, file, date=None, username=None, name=None, tweet=None, replies_count=None, retweets_count=None,
                 likes_count=None):
        self._file = file
        self._args = [date, username, name, tweet, replies_count, retweets_count, likes_count]
        self._map = {date: 'date', username: 'username', name: 'name', tweet: 'tweet', replies_count: 'replies_count',
                     retweets_count: 'retweets_count', likes_count: 'likes_count'}
        self._generate_filtered_df()

        self.hashtags = self._extract_artifact(r'#(\S*)')
        self.mentions = self._extract_artifact(r'@(\S*)')
        self.urls = self._extract_artifact(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

    def _generate_filtered_df(self):
        df = pd.read_csv(self._file)
        filtered_args = list(filter(None, self._args))
        if filtered_args:
            self.filtered_df = df[filtered_args]
            self.filtered_df = self.filtered_df.rename(columns=self._map)
        else:
            self.filtered_df = df[
                ['date', 'username', 'name', 'tweet', 'replies_count', 'retweets_count', 'likes_count']]

    def _extract_artifact(self, pattern):
        artifacts = []
        for item in self.filtered_df['tweet']:
            artifact_list = re.findall(pattern, item)
            for artifact in artifact_list:
                artifacts.append(artifact)
        return artifacts

    def rank_usernames(self):
        if 'username' in self.filtered_df:
            return self.filtered_df['username'].value_counts()

    def rank_hashtags(self):
        if 'tweet' in self.filtered_df:
            return pd.Series(self.hashtags).value_counts()

    def rank_mentions(self):
        if 'tweet' in self.filtered_df:
            return pd.Series(self.mentions).value_counts()

    def rank_urls(self):
        if 'tweet' in self.filtered_df:
            return pd.Series(self.urls).value_counts()

    def sort_by_replies(self):
        if 'replies_count' in self.filtered_df:
            return self.filtered_df.sort_values(by='replies_count', ascending=False, ignore_index=True)

    def sort_by_retweets(self):
        if 'retweets_count' in self.filtered_df:
            return self.filtered_df.sort_values(by='retweets_count', ascending=False, ignore_index=True)

    def sort_by_likes(self):
        if 'likes_count' in self.filtered_df:
            return self.filtered_df.sort_values(by='likes_count', ascending=False, ignore_index=True)

    def get_time_series(self):
        if 'date' in self.filtered_df:
            self.filtered_df['count'] = 1
            return self.filtered_df.groupby('date').sum('count')['count']

    def save_csv(self, file_name, method):
        result = eval(f'self.{method}()')
        print(type(result))
        result.to_csv(file_name)

    def print_results(self, method, max_rows=None):
        if max_rows is None:
            max_rows = len(self.filtered_df)
        result = eval(f'self.{method}()')
        print(result.to_string(justify='justify-all', max_rows=max_rows))
