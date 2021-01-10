from utilities import get_articles


def get_slate():
    get_articles('https://slate.com', 'slate')


if __name__ == '__main__':
    get_slate()
