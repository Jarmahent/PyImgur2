from praw import Reddit as PrawReddit
from pyimgur import Imgur as pimg
class Reddit():

    def __init__(self, app_id, app_secret, subreddit, pimg_id, pimg_secret):
        self._subreddit = subreddit

        self._reddit = PrawReddit(
            client_id=app_id,
            client_secret=app_secret,
            user_agent="This is my user agent"
        )
        self._Imgur = pimg(
            client_id = pimg_id,
            client_secret = pimg_secret
        )


    def get_random_submission(self):
        return self._reddit.subreddit(self._subreddit).random().url

    def process_url(self, url):
        if('redd' in url):
            print("Reddit {}".format(url))
        if('imgur' in url):
            print("Imgur {}".format(url))
        if('.jpd' in url):
            print("")

   # def download_From_Imgur(self, url):



