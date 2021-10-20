from random import randint

with open("test.txt", 'w') as f:
    for i in range(100):
        f.write(str(randint(0, 100)) + " ")
