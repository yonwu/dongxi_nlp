import os
import json
import tweepy


def get_all_tweets(username: str, bearer_token: str):
    """Fetch all tweets from a user timeline using Twitter API v2."""
    client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
    user = client.get_user(username=username)
    user_id = user.data.id
    tweets = []
    pagination_token = None
    while True:
        response = client.get_users_tweets(id=user_id, max_results=100, pagination_token=pagination_token)
        if response.data:
            tweets.extend(response.data)
        if response.meta.get("next_token"):
            pagination_token = response.meta["next_token"]
        else:
            break
    return tweets


def main():
    username = os.getenv("TWITTER_USERNAME", "dongxi_nlp")
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    if not bearer_token:
        raise RuntimeError("Set TWITTER_BEARER_TOKEN environment variable with your API bearer token.")
    tweets = get_all_tweets(username, bearer_token)
    for tweet in tweets:
        print(json.dumps(tweet.data, ensure_ascii=False))


if __name__ == "__main__":
    main()
