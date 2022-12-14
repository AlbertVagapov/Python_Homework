from random import randint
from typing import List
from typing import Optional


def give_int(input_string: str, min_num: Optional[int] = None, max_num: Optional[int] = None) -> int:
    '''
    Takes an int number from user
    Takes: string
    Returns: int number or a message about an error
    '''
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше{min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите больше{max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')
def get_list_data(filename: str) -> List[str]:
    '''
    Возвращает список из строк файла
    Args:
    filename - имя файла
    Returns:
    List[str]
    '''
    with open(filename, encoding='utf-8') as file:
        return file.read().split('\n')

def random_list(listlen: int) -> list:
    '''
    Gives list with random values
    :param listlen: list's length
    :return: list with random values
    '''

    datalist = list()
    for i in range(listlen):
        datalist.append(randint(1, 100))
    return datalist