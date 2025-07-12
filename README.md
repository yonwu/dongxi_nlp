# dongxi_nlp

For knowledge sharing.

## Twitter crawler

The repository includes `twitter_crawler.py`, a simple script that collects tweets from a public Twitter account using the official Twitter API.

### Setup

1. Install dependencies:
   ```bash
   pip install tweepy
   ```
2. Set the required environment variable with your API bearer token:
   ```bash
   export TWITTER_BEARER_TOKEN="<your_token>"
   ```
3. (Optional) Override the default username by setting `TWITTER_USERNAME`.

### Usage

Run the script to fetch all tweets for the configured user:
```bash
python twitter_crawler.py > tweets.json
```
This will print each tweet's JSON on a separate line.
