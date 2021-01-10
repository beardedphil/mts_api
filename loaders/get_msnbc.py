from utilities import get_articles


def get_msnbc():
    get_articles('https://msnbc.com', 'msnbc')


if __name__ == '__main__':
    get_msnbc()
