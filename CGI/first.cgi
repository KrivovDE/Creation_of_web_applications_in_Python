#!/usr/bin/env python3

import os

print("Content-Type: text/html")
print()

# Получаем путь из URL, например /hello или /goodbye
path = os.environ.get('PATH_INFO', '/')

if path == '/hello':
    print("<h1>Привет, мир!</h1>")
elif path == '/goodbye':
    print("<h1>Пока, мир!</h1>")
else:
    print("<h1>404 — Страница не найдена</h1>")