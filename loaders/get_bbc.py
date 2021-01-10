from utilities import get_articles


def get_bbc():
    get_articles('https://bbc.com/news', 'bbc')


if __name__ == '__main__':
    get_bbc()
