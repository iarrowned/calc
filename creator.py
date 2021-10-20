from random import uniform

with open("test.txt", 'w') as f:
    for i in range(100):
        f.write(str(uniform(0, 100))[:5] + " ")
