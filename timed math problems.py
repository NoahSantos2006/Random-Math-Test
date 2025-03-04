import random
import time

score = 5

user_input = input('Press Enter to Begin ')
print('---------------------------------------------------------------')

start_time = time.time()

operators = ['+', '-', '*', '/']

total_problems = 5

problem_number = 1

def generate_problem():
    if_divisible = True
    first_time = True
    global score
    global problem_number
    left = random.randint(3, 12)
    right = random.randint(3, 12)
    operator = random.choice(operators)
    while if_divisible:
        expr = str(left) + " " + operator + " " + str(right)
        if left % right != 0 and operator == '/':
            left = random.randint(3, 12)
            right = random.randint(3, 12)
            operator = '/'
        else:
            if_divisible = False
            
    answer = eval(expr)
    user_input = input(f'Problem #{problem_number}: {expr} = ')
    while True:
        if int(user_input) == int(answer):
            return 1
        else:
            print('Try again!')
            if first_time:
                score -= 1
                first_time = False
            user_input = input(f'Problem #{problem_number}: {expr} = ')

while problem_number <= 5:
    problem_number += generate_problem()

final_time = time.time()
print('---------------------------------------------------------------')
print(f'Congratulations! Your time is: {(final_time - start_time):.2f}!\nYour score is {score}')