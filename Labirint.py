quest = {  # пути в квесте
    'налево'.lower(): {
        'левую'.lower(): 'text #1',
        'правую'.lower(): 'Но за ней вас подстерегала гигантская подземная жаба, которая проглотила вас целиком!'
    },
    'направо'.lower(): {
        'левую'.lower(): 'text #3',
        'правую'.lower(): 'text #4'
    },
    'прямо'.lower(): {
        'левую'.lower(): 'text #5',
        'правую'.lower(): 'text #6'
    }
}

question = [  # вопросы
    'Вы находитесь в пещере на развилке. Вы можете пойти "налево", "направо" или "прямо".',
    'Вы направились {}. Через некоторое время вы дошли до двух дверей. Вы выберете "левую" или "правую"?'
]

ans = [None, None]  # ответы игрока

entry = '> '  # приглашение на ввод


def check_key(key, data):
    return True if key in data else False


import sys

try:
    ans[0] = input(question[0] + '\n' + entry).lower()
    if not check_key(ans[0], quest): raise KeyError

    ans[1] = input(question[1].format(ans[0]) + '\n' + entry).lower()
    if not check_key(ans[1], quest[ans[0]]): raise KeyError

    text = quest[ans[0]][ans[1]]
    print('Вы смело открыли {} дверь. {}'.format(ans[1], text))
except KeyError:
    sys.exit('KeyError')