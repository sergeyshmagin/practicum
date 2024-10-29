voting = {}

def voting_get(name):

    if voting.get('name'):
        print('not ok')
    else:
        voting[name] = True
        print('ok')

voting_get('tom')
voting_get('tom')
