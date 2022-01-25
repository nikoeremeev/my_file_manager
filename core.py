import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть!')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть! ')
    else:
            shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    #print(result)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')
    print()


def change_dir(name):
    os.chdir(name)
    print(os.getcwd())

if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some_text')
    create_folder('new_f1')
    get_list()
    get_list(True)
    delete_file('new_f1')
    delete_file('text.dat')
    copy_file('new_f', 'new2')
    create_file('text.dat')
    copy_file('text.dat', 'text2.dat')
    save_info('abc')