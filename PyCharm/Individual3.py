#!/user/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    r = ''
    for i in range(len(s)-1):
         if s[i] != 'о':
             r += s[i]
         elif i % 2 == 1:
             r += s[i]
    print(f"Новое предложение: {r}")



