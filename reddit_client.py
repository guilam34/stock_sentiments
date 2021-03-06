import praw
import config

if __name__ == "__main__":
    reddit = praw.Reddit(
        client_id=config.client_id,
        client_secret=config.client_secret,
        password=config.password,
        user_agent=config.user_agent,
        username=config.username,
    )
    print(reddit.user.me())
