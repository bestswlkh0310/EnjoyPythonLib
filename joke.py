import pyjokes

joke = pyjokes.get_joke()
print(joke)

joke = pyjokes.get_joke(category='neutral')
print(joke)

joke = pyjokes.get_joke(language='en', category='neutral')
print(joke)

import emoji

print(emoji.emojize('Hello World :thumbs_up:'))

emoji_string = emoji.emojize('I love Python! :heart:')
print(emoji_string)

emoji_unicode = emoji.demojize('I am 😊')
print(emoji_unicode)


