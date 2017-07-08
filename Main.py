import click
from clients import reddit
from clients import AppInfo


@click.command()
@click.option('--repeat', type=bool, default=False, help="Run in loop?")
@click.option('--sleep', type=click.IntRange(10, 100), default=30, help='How long should we sleep for?')
@click.option('--subreddit', help='Where should we download images from?', default='pics')
def start_download(repeat, sleep, subreddit):
    while True:
        reddit_app_id = AppInfo.REDDIT_APP_ID
        reddit_app_secret = AppInfo.REDDIT_APP_SECRET
        pimg_id = AppInfo.REDDIT_APP_SECRET
        pimg_secret = AppInfo.REDDIT_APP_ID

        r = reddit.Reddit(reddit_app_id, reddit_app_secret, subreddit, pimg_id, pimg_secret)

        url = r.get_random_submission()
        r.process_url(url)
        print(url)
        r.sleep(sleep)
        if repeat is False:
            break

if __name__ == '__main__':
    start_download()