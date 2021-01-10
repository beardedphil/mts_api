import requests
import newspaper
import sys


def get_articles(url, source, ignore_strings=None):
    if ignore_strings is None:
        ignore_strings = []
    paper = newspaper.build(url)
    print(len(paper.articles))

    for article in paper.articles:
        try:
            article.download()
            print('Downloaded')
        except:
            print('Article failed to download')
            continue

        try:
            article.parse()
            print('Parsed')
        except:
            print('Article failed to parse')
            continue

        if validate_article(article, ignore_strings):
            try:
                article.nlp()
            except:
                print(article)
                print('Article failed to nlp:', sys.exc_info()[0])
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

    if not article.publish_date:
        return False

    return True


def post_article(article):
    api = 'https://mytrustedsourceapi.herokuapp.com/articles/'
    r = requests.post(api, data=article)

    print(r.text)
