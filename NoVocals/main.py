def language(name):
    result = ''
    for letter in name:
        if letter.lower() in 'aeiouy':
            if letter.isupper():
                result += 'G'
            else:
                result += 'g'
        else:
            result += letter
    return result


print(language(input('Enter a name: ')))
