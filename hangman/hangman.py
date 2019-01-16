import random, os

catalog = ['1.Sport', '2.Drinking water brand']
temp = True
score = 0
remain = 10
word = ''
hint = ''
path = ''
wrong_pick = []
correct_pick = []

def selecting(path):
    """
    selecting category and random the word from selected category.
    """
    #  showing choice
    print('Selecting Category:')
    for category in catalog:
        print(category)
    
    #  processing name to select file
    while path == '':
        choice = int(input('Category number: '))
        if choice == 1:
            path = os.getcwd()+f'/category/sport.txt'
        elif choice == 2:
            path = os.getcwd()+f'/category/water.txt'
    
    #  file processing
    cate_n = open(path, "r", encoding='UTF-8').read().splitlines()
    cate_n = [x.split('#') for x in cate_n]
    #  random word and hint from selected file
    temp = random.choice(cate_n)
    word = list(temp[0])
    hint = temp[1]
    return word, hint


def show(word):
    """
    show '_ _ _ _ _ _ _ _    score 0, remaining wrong guess 10'.
    """
    for char in list(word):
        if char.isalpha():
            if char not in correct_pick:
                print('_', end=' ')
            else:
                print(char, end=' ')
    if wrong_pick:
        print(f'score {score}, remaining wrong guess {remain} wrong guess: {" ".join(wrong_pick)}')
    else:
        print(f'score {score}, remaining wrong guess {remain}')


def guess(word, score, remain):
    """
    check if player guess correct letter and add scores or deduct remaining guess.
    """
    character = input('Choose your letter!: ')
    if character in list(word):
        if character not in correct_pick:
            correct_pick.append(character)
        score += remain
        return remain, score
    else:
        if character not in wrong_pick:
            wrong_pick.append(character)
        remain -= 1
        return remain, score


def is_won(word, correct_pick, temp):
    """
    check if the game should end.
    """
    return set(word) == set(correct_pick)


word, hint = selecting(path)
print(f'Hint: {hint}')

#  main Loop
while not is_won(word, correct_pick, temp) or temp:
    temp = False
    show(word)
    remain, score = guess(word,score, remain)
print('You win!',f'Your score: {score}')