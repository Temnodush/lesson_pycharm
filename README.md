# Домашнее задание 10_1

## Описание:

Домашнее создание включает в себя создания нового модуля с двумя функциями а так же, создание веток, работу с репозиторием GitHub и так далее.

## Этапы работы:

 1. Создание веток.
 2. Создание файла README.md и его оформление:
 3. Создание модуля и функций.
 4. Проверка кода с помощью линтеров.
 5. Написание docstrings к функциям.

## Использование:

В проекте реализованы 4 функции которые позволяют проводить следующие операции:

### 1. Маскировка номера банковской карты.
```
Функция mask_account_card принимает счёт или карту и шифрует в
зависимости от содержимого.
Если введена карта - то выводится полный номер карты с 6
зашифрованными цифрами.
Например: 1234 12** **** 1234

Если введён счёт, то выводится последние 4 цифры и две цифры
которые были зашифрованы.
```

### 2. Вывод даты в читаемом формате.
```
Функция get_date принимает строку с датой и возвращает часть
содержимого в нужной последовательности.
```

### 3. Сортировка по значению ключа state.
```
Функция filter_by_state принимает список словарей и возвращает новый список
со словарями у которых ключ state равен значению EXECUTED
```

### 4. Сортировка по дате.
```
Функция sort_by_date сортирует принимаемый список словарей и возвращает
отсортированный в порядке убывания.
```