from utilities import get_articles


def get_fox():
    get_articles('https://foxnews.com', 'fox')


if __name__ == '__main__':
    get_fox()
