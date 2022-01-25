import random

def game():

    # загадываем случайное число сами и поехали
    k = 1
    x = 100
    number = random.randint(k, x)
    flag = 0
    while flag == 0:
        answer = int(input('введите число: '))
        if answer == number:
            flag = 1
        elif answer > number:
            print('введенное число больше загаданного.')
        elif answer < number:
            print('введенное число меньше загаданного.')
    print('Победа')

if __name__ == '__main__':
    game()