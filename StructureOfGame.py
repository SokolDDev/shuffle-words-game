import random

levels = {0: 'EASY', 1: 'MEDIUM', 2: 'HARD', 3: 'EXPERT'}
lifes = {0: 4, 1: 3, 2: 2, 3: 1}

words_easy_id = {0: 'ананас', 1: 'альбом', 2: 'ворота', 3: 'возить', 4: 'память'}
words_medium_id = {0: 'вирус', 1: 'волос', 2: 'сокол', 3: 'слово', 4: 'столб'}
words_hard_id = {0: 'болт', 1: 'риск', 2: 'слух', 3: 'урок', 4: 'клуб'}
words_expert_id = {0: 'лоб', 1: 'рис', 2: 'рот', 3: 'три', 4: 'сок'}

name = ''
age = ''

level = 0
life = 4
mixed_from_original_word = None
original_word = None
word_to_compare_with_the_original = None


def user_input_and_initialize_variables():
    global name
    global age
    global level
    global life
    global mixed_from_original_word
    global original_word
    name = input(f'Введите ваше имя: ')
    age = int(input(f'Введите ваш возраст: '))
    print("Выбирете уровень сложности, введите цифру: ")
    level = int(input(levels))
    life = lifes.get(level)
    original_word = set_original_word_by_level(level)
    list_shuffled_word = shuffle_letters_in_word(original_word)
    mixed_from_original_word = "".join(list_shuffled_word)


def set_original_word_by_level(level):
    if level == 0:
        return random.choice(words_easy_id)
    elif level == 1:
        return random.choice(words_medium_id)
    elif level == 2:
        return random.choice(words_hard_id)
    elif level == 3:
        return random.choice(words_expert_id)
    else:
        print("Error")
        return 'Error'


def shuffle_letters_in_word(original_word):
    tmp_list = list(original_word)
    random.shuffle(tmp_list)
    return tmp_list


def input_your_permisson_word():
    global word_to_compare_with_the_original
    word_to_compare_with_the_original = str(input('Введите предполагаемое слово: '))
    word_comparison()


def start_game():
    print(f'Здравия желаю, {name}!')
    print(f'Ваш уровень - {levels.get(level)}, у Вас есть {life} жизни(ь)...')
    print(f'Начнём? good luck have fun!!!')
    print(f'Перед вами перемешанное слово: "{mixed_from_original_word}", введите его в правильном порядке :)')


def word_comparison():
    global life
    is_equls = words_is_equals(original_word, word_to_compare_with_the_original)
    if is_equls:
        print("Поздравляем. Вы выиграли!")
    else:
        life -= 1
        if life == 0:
            print("Вы изчерпали попытки, испытайте свою удачу ещё раз :)")
        elif life > 0:
            print(f'У вас осталось {life} попыток ')
            input_your_permisson_word()


def words_is_equals(ori_word, user_input_word):
    if ori_word == user_input_word:
        return True
    else:
        return False


def main():
    user_input_and_initialize_variables()
    set_original_word_by_level(level)
    shuffle_letters_in_word(original_word)
    start_game()
    input_your_permisson_word()


if __name__ == '__main__':
    main()
