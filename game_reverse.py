import random

def game_reverse():

    # загадываем случайное число сами и поехали
    k = 1
    x = 100
    number = random.randint(k, x)

    print(number)
    flag = 0
    while flag == 0:
        answer = input()
        if answer == '>':
            k = number
        elif answer == '<':
            x = number
        elif answer == '=':
            flag == 1
            break

        number = random.randint(k, x)
        print(number)
    print('end')

if __name__ == '__main__':
    game_reverse()