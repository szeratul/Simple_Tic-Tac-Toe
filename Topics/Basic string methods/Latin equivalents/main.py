replacing_list = {'é': 'e', 'ë': 'e', 'á': 'a', 'å': 'a', 'œ': "oe", 'æ': "ae"}
name = input()


def normalize(name):
    new_name = name
    for c in name:
        if c in replacing_list:
            new_name = name.replace(c, replacing_list[c])
    return new_name


print(normalize(name))
