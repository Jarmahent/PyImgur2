from praw import Reddit as PrawReddit
import os
import string
import random
from random import randint
from urllib import request
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
        self._localDirectory = os.path.expanduser("~")
        print(os.path.join(self._localDirectory, "Pictures", "PyPics") + "\\test" + ".jpg")
        if not os.path.exists(os.path.join(self._localDirectory, "Pictures", "PyPics")):
            os.makedirs(os.path.join(self._localDirectory, "Pictures", "PyPics"))
            print("Creating Path for pictures...")

    def generate_name(self, size=randint(3, 10), chars=string.ascii_uppercase + string.digits):  # Create random ID
        return ''.join(random.choice(chars) for _ in range(size))

    def get_random_submission(self):
        return self._reddit.subreddit(self._subreddit).random().url

    def process_url(self, url):
        if(not ".jpg" in url and "imgur" in url):
            imgur_url = url.split('/')[-1].split('.')[0]
            pimg.get_image(imgur_url).download(path=os.path.join(self._localDirectory, "Pictures", "PyPics"), name=self.generate_name(), overwrite=False, size=None)
            print("Base Imgur URL")
        if(".jpg" in url):
            request.urlretrieve(url, os.path.join(self._localDirectory, "Pictures", "PyPics") + "{}{}{}".format("\\", self.generate_name(), ".jpg"))
            print(" JPG format ")





