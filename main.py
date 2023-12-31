import os

from api import reddit
from api import instagram
from dotenv import load_dotenv

load_dotenv()

postsRaw = reddit.get_top_posts(os.getenv("SUBREDDIT"))
posts = reddit.get_post_data(postsRaw)

reddit.download_images(posts)

instagram.post_images(posts)
