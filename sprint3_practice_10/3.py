# Напишите декоратор obfuscator
def obfuscator(func):
    def wrapper():
        lst = func()
        dict = {}

        for a in lst:
            phrase = []
            for i in range(len(lst[a])):
                if a == 'password':
                    phrase.append('*')

                elif i not in (0, len(lst[a])-1):
                    phrase.append('*')
                else:
                    phrase.append(lst[a][i])
            dict[a] = ''.join(phrase)
        return dict
    return wrapper

#            for i in range(1, len(phrase)-1):


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())
