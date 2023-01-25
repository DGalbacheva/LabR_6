#!/user/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    for i, v in enumerate(s[:-1]):
        if v == s[i+1]:
            print(i+1, i+2)
            break
    else:
         print("Таких символов нет")