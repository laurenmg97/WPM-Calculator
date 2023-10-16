import time

phrase = 'Sally sells shells by the seashore'

word_count = len(phrase.split())

begin = input('Please type: ' + phrase + '\n' + 'Press enter when ready.')

t0 = time.time()
attempt = input('\n')
t1 = time.time()
attempt_time = (t1 - t0) / 60
wpm = str(round(word_count / attempt_time, 2))

if attempt == phrase:
    print('\n' + 'Your WPM: ' + wpm)
else:
    print('\n' + 'Phrase typed incorrectly. Please try again')
