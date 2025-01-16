import json
import re
import random

MAX_TRIALS = 10

def is_valid_trail(trial, valid_words, cur_word):
    # check if trial in valid word list
    if trial not in valid_words:
        print('不是有效的词语。')
        return False
    
    # check if trial is one character different from cur_word
    diff = 0
    for i in range(len(cur_word)):
        if cur_word[i] != trial[i]:
            diff += 1

    if diff != 1:
        print('不是一个字的差异。')
        return False
    
    return True

# read json
with open('word.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

valid_words = [w for w in (d['word'] for d in data) if re.fullmatch(r'[\u4e00-\u9fff]{2}', w) is not None]

# start the game
start_word, end_word = random.sample(valid_words, 2)

cur_trail = 0

trail_list = [start_word]

print('从「' + start_word + '」到「' + end_word + '」。变化次数：' + str(cur_trail) + ' / ' + str(MAX_TRIALS))
print('→'.join(trail_list))

# every trial
cur_word = start_word

while cur_trail < MAX_TRIALS:
    trial = input('猜测:')
    while not is_valid_trail(trial, valid_words, cur_word):
        trial = input('猜测:')

    if trial == end_word:
        print('恭喜你，猜对了！')
        break
    else:
        cur_word = trial
        cur_trail += 1
        trail_list.append(trial)

        print('从「' + start_word + '」到「' + cur_word + '」到「' + end_word + '」。变化次数：' + str(cur_trail) + ' / ' + str(MAX_TRIALS))
        print('→'.join(trail_list))