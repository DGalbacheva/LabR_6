#!/user/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = list(input("Введите прежение: ").split())
    n = input("Какой символ проверить на вхождение: ")
    for i, v in enumerate(s):
        if n in v:
            print(i + 1, v)