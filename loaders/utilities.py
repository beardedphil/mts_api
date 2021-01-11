import requests
import time
from datetime import datetime, timedelta
import pytz
import newspaper
import nltk
nltk.download('punkt')


def get_articles(url, source, ignore_strings=None):
    if ignore_strings is None:
        ignore_strings = []
    paper = newspaper.build(url)
    print(len(paper.articles))

    for article in paper.articles:
        try:
            article.download()
        except:
            print('Article failed to download')
            continue

        try:
            time.sleep(1)
            article.parse()
        except:
            print('Article failed to parse')
            continue

        if validate_article(article, ignore_strings):
            try:
                article.nlp()
            except:
                print('Article failed to nlp')
                continue

            if not article.keywords:
                continue

            pub_date = article.publish_date.strftime("%Y-%m-%d")

            parsed_article = {
                'title': article.title,
                'source': source,
                'article_link': article.url,
                'image_link': article.top_image,
                'pub_date': pub_date,
                'keywords': article.keywords,
            }

            post_article(parsed_article)


def validate_article(article, ignore_strings):
    if not article.title:
        return False

    if not article.url:
        return False

    for ignore_string in ignore_strings:
        if ignore_string in article.url:
            return False

    if not article.top_image:
        return False

    if not article.publish_date:
        return False

    utc = pytz.UTC
    article_date = utc.localize(article.publish_date)
    expiration = datetime.now() - timedelta(days=2)
    expiration_date = utc.localize(expiration)

    if article_date < expiration_date:
        return False

    return True


def post_article(article):
    api = 'https://mytrustedsourceapi.herokuapp.com/articles/'
    r = requests.post(api, data=article)

