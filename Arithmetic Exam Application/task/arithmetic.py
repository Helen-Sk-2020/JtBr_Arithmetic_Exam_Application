import random
import math


def check_input():
    while True:
        print('''Which level do you want? Enter a number:
        1 - simple operations with numbers 2-9
        2 - integral squares of 11-29''')
        x = int(input())
        if x == 1 or x == 2:
            return x
            break
        else:
            print('Incorrect format.')


def check_answer(answer):
    while True:
        x = input()
        if x.strip('-').isdigit():
            if int(x) == answer:
                print('Right!')
                return 'Right!'
            else:
                print('Wrong!')
            break
        else:
            print('Incorrect format.')


def simple_operations():
    total = 0
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    operator = random.choice('+-*')
    print(f"{a} {operator} {b}")
    
    if operator == "+":
        total = int(a) + int(b)
    elif operator == "-":
        total = int(a) - int(b)
    elif operator == "*":
        total = int(a) * int(b)
    return total


def integral_squares():
    num = random.randint(11, 29)
    print(num)
    square = math.pow(num, 2)
    return square


def save_result(level, n):
    print("What is your name?")
    name = input()
    if level == 1:
        level_description = 'simple operations with numbers 2-9'
    elif level == 2:
        level_description = 'integral squares of 11-29'
    results = open('results.txt', 'a', encoding='utf-8')
    results.write(f'{name}: {n}/5 in level {level} ({level_description})')
    results.close()
    print('The results are saved in "results.txt".')


level = check_input()
counter = n = 0
while counter < 5:
    if level == 1:
        result = simple_operations()
    elif level == 2:
        result = integral_squares()
    if check_answer(result) == 'Right!':
        n += 1
    counter += 1
    

print(f"Your mark is {n}/5.  Would you like to save the result?")
user_answer = str(input())
if user_answer.lower() == 'yes' or user_answer == 'y':
    save_result(level, n)




