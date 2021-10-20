from random import uniform

with open("test.txt", 'w') as f:
    for i in range(100): # здесь 100 это количество цифр, которые будут записаны в файл
        f.write(str(uniform(0, 100))[:5] + " ") # здесь (0, 100) - диапазон цифр, [:5] - до какого знака обрезать
