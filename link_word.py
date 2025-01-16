import json
import re
import random

MAX_TRIALS = 10
CHECK_COMMON = True
FREQUENCY_THRESHOLD = 0

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

def is_common_word(word, common_chars):
    if (not CHECK_COMMON): return True

    assert len(word) == 2

    return word[0] in common_chars and word[1] in common_chars

# read json
with open('char_common.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

common_chars = [d['char'] for d in data if d['frequency'] <= FREQUENCY_THRESHOLD]

with open('word.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

valid_words = [w for w in (d['word'] for d in data)
               if (re.fullmatch(r'[\u4e00-\u9fff]{2}', w) is not None and is_common_word(w, common_chars))]

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