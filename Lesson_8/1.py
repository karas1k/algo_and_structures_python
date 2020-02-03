"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

MY_STRING = input("Введите слова для кодирования: ")
print(f"Исходная строка: {MY_STRING}")


class Node:
    '''Класс распределения символов по двоичному древу'''
    def __init__(self, left=None, right=None):
        '''функция распределения символов по двоичному древу'''
        self.left = left
        self.right = right

    def children(self):
        '''функция распределения символов по двоичному древу'''
        return self.left, self.right


def make_haffman_tree(node, code=""):
    '''Рекурсия распределения'''
    if isinstance(node, str):
        return {
            node: code
        }

    left, right = node.children()

    result = {}
    # 0 - налево, 1 - направо
    result.update(make_haffman_tree(left, code + "0"))
    result.update(make_haffman_tree(right, code + "1"))

    return result


FREQUENCIES = {}
for char in MY_STRING:
    if char not in FREQUENCIES:
        FREQUENCIES[char] = 0

    FREQUENCIES[char] += 1

TREE = FREQUENCIES.items()

while len(TREE) > 1:
    TREE = sorted(TREE, reverse=True, key=lambda x: x[1])
    CHAR1, COUNT1 = TREE[-1]
    CHAR2, COUNT2 = TREE[-2]
    TREE = TREE[:-2]
    TREE.append(
        (Node(CHAR1, CHAR2), COUNT1 + COUNT2)
    )

CODE_TABLE = make_haffman_tree(TREE[0][0])

CODED = []
for char in MY_STRING:
    CODED.append(CODE_TABLE[char])

print('Закодированная строка: ', end="")
for i in CODED:
    print(i, end='')
