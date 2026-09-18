# Лабораторная работа 3. Хэш-таблицы

Решить следующие задачи

## A. Подмножество массива

Нужно определить, служит ли один массив (меньший) подмножеством другого (большего). Реализуйте с использованием хэш-таблиц.

**Пример 1**

```
["a", "b", "c", "d", "e", "f"]
["b", "d", "f"]
```

Второй массив — подмножество первого

**Пример 2**

```
["a", "b", "c", "d", "e", "f"]
["b", "d", "f", "h"]
```

Второй массив не будет подмножеством первого

## B. Первый неповторяющийся символ

Напишите функцию, которая возвращает первый неповторяющийся символ в строке. Реализуйте с использованием хэш-таблиц.

**Пример**

В строке `"minimum"` есть два неповторяющихся символа — `"n"` и `"u"`, поэтому ваша функция должна возвратить `"n"`, так как он встречается первым. Временная сложность вашей функции должна быть равна O(N).

## C. Самый длинный палиндром из букв строки

Дана строка `s`, состоящая из строчных или заглавных букв. Нужно вернуть длину самого длинного палиндрома, который можно построить с помощью этих букв. Можно использовать не все буквы в строке `s`. Буква в палиндроме может встречаться только столько же или меньше раз, сколько встречается в строке.

Буквы чувствительны к регистру, например, `"Aa"` не считается палиндромом. Реализуйте с использованием хэш-таблиц.

**Пример 1**

Ввод: `s = "abccccdd"`

Вывод: `7`

Пояснение: Самый длинный палиндром, который можно построить, — это `"dccaccd"`, длина которого равна 7.

**Пример 2**

Ввод: `s = "a"`

Вывод: `1`

Пояснение: Самый длинный палиндром, который можно построить, — это `"a"`, длина которого равна 1.

**Тест-кейсы**

| Вход                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Ожидаемый результат |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| `"aAbBABba"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 8                   |
| `"abcdefghijklmnoPQrstuvwxyz"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1                   |
| `"wasitacaroracatisaw"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 19                  |
| `"bbbabab"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 7                   |
| `"abcdeedcba"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 10                  |
| `"looooooongestpalindrOme"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 13                  |
| `"abcdeedcbaxyz"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 11                  |
| `"abbbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbab"` | 1122                |

## D. Проверка анаграммы

Даны две строки `s` и `t`. Вернуть `true`, если `t` — это анаграмма `s`, и `false` в противном случае. Анаграммы — это слова, содержащие одни и те же символы в разном порядке. Реализуйте с использованием хэш-таблиц.

**Пример 1**

Ввод: `s = "анаграмма"`, `t = "амгармана"`

Вывод: `истина`

**Пример 2**

Ввод: `s = "анаграмма"`, `t = "грамм"`

Вывод: `ложь`

**Тест-кейсы**

| s           | t           | Ожидаемый результат |
| ----------- | ----------- | ------------------- |
| `"нора"`    | `"рано"`    | true                |
| `"монета"`  | `"отмена"`  | true                |
| `"мышка"`   | `"камыш"`   | true                |
| `"тормони"` | `"монитор"` | true                |
| `"тоемони"` | `"монитор"` | false               |
