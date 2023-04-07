from pprint import pprint

import requests
import datetime as DT


def get_questions():
    questions_url = ('https://api.stackexchange.com/2.3/questions')
    today = DT.datetime.today()
    two_days_ago = DT.datetime.today() - DT.timedelta(days=2)
    params = {
        'fromdate': int(two_days_ago.timestamp()),
        'todate': int(today.timestamp()),
        'order': 'desc',
        'sort': 'activity',
        'tagged': 'Python',
        'site': 'stackoverflow'
    }
    pprint(params)
    response = requests.get(questions_url, params=params)
    return response.json()


if __name__ == '__main__':
    questions = get_questions()
    print('Количество вопросов:', len(questions))
    pprint(questions)
