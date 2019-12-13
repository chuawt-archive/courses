def add_punctuation(phrase):
    interrogatives = ('Who', 'What', 'Why', 'Where', 'How')
    phrase_capitalized = phrase.capitalize()
    if phrase_capitalized.startswith(interrogatives):
        return '{}?'.format(phrase_capitalized)
    else:
        return '{}.'.format(phrase_capitalized)

text_list = []
while True:
    user_input = input('Say something: ')
    if user_input == '\end':
        break
    else:
        text_list.append(add_punctuation(user_input))

text = ' '.join(text_list)
print(text)