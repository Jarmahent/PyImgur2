import click
from clients import reddit
from clients import ApplicationInfo

@click.command()
@click.option('--repeat', type=bool, default=False, help="Run in loop?")
@click.option('--sleep', type=click.IntRange(10, 100), default=30, help='How long should we sleep for?')
@click.option('--subreddit', help='Where should we download images from?', default='pics')
def start_download(repeat, sleep, subreddit):
    reddit_app_id = ApplicationInfo.REDDIT_APP_ID
    reddit_app_secret = ApplicationInfo.REDDIT_APP_SECRET
    pimg_id = ApplicationInfo.PIMGUR_APP_ID
    pimg_secret = ApplicationInfo.PIMGUR_APP_SECRET

    r = reddit.Reddit(reddit_app_id, reddit_app_secret, subreddit, pimg_id, pimg_secret)
    while True:
        url = r.get_random_submission()
        r.process_url(url)
        print(url)
        r.sleep(sleep)
        if repeat is False:
            break

if __name__ == '__main__':
    start_download()
