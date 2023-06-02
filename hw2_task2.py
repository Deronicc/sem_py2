""" Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа. """

s = int(input("Введите сумму числе S: "))
p = int(input("Введите произедение P: ")) 

count = 0

for x in range(0, 1001):
    for y in range(0, 1001):
        if s == x + y and p == x * y:
            print(x, y)
            count += 1

if count == 0:
    print("Ошибка! Нет таких числе, которые дают такую сумму S и произведение P")

        