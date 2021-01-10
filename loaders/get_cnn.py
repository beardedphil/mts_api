from utilities import get_articles


def get_cnn():
    ignore_strings = [
        'cnnespanol.cnn',
        'arabic.cnn'
    ]
    get_articles('https://cnn.com', 'cnn', ignore_strings)


if __name__ == '__main__':
    get_cnn()
