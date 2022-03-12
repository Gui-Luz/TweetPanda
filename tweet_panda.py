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

    def rank(self, attribute):
        if attribute == 'username':
            if 'username' in self.filtered_df:
                frame = self._rank_username(attribute)
                return frame
        else:
            if 'tweet' in self.filtered_df:
                frame = self._rank_other_attributes(attribute)
                return frame
            else:
                raise ImportError("Your dataset don't contain tweets")

    def sort(self, attribute):
        if attribute in self.filtered_df:
            return self.filtered_df.sort_values(by=attribute, ascending=False, ignore_index=True)
        else:
            raise AttributeError("You didn't provided a valid attribute")

    def time_series(self):
        if 'date' in self.filtered_df:
            self.filtered_df['count'] = 1
            return self.filtered_df.groupby('date').sum('count')['count']
        else:
            raise ImportError("Your dataset don't contain dates")

    def save_csv(self, file_name, method):
        result = eval(f'self.{method}()')
        print(type(result))
        result.to_csv(file_name)

    def print_results(self, method, max_rows=None):
        if max_rows is None:
            max_rows = len(self.filtered_df)
        result = eval(f'self.{method}()')
        print(result.to_string(justify='justify-all', max_rows=max_rows))

    def _rank_username(self, attribute):
        series = self.filtered_df[attribute].value_counts()
        frame = self._convert_series_to_frame(series)
        frame = self._rename_dataframe_columns(frame, attribute)
        return frame

    def _rank_other_attributes(self, attribute):
        try:
            object_attribute = eval(f'self.{attribute}')
            series = pd.Series(object_attribute).value_counts()
            frame = self._convert_series_to_frame(series)
            frame = self._rename_dataframe_columns(frame, attribute)
            return frame
        except AttributeError as e:
            raise AttributeError("You didn't provided a valid attribute")

    @property
    def df(self):
        return self.filtered_df

    @staticmethod
    def _convert_series_to_frame(series):
        return series.to_frame()

    @staticmethod
    def _rename_dataframe_columns(frame, index_name):
        frame.reset_index(inplace=True)
        frame.columns = [index_name, 'count']
        return frame

