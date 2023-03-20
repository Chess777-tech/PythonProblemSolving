d = {1: 10, 2: 20, 3: 30, 4: 40}

def is_key_present(x):
    if x in d:
        print('Key is present in dictionary')
    else:
        print('Key does not exist')

is_key_present(4)
is_key_present(7)