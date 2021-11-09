"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

predict_number = np.random.randint(1, 101) # отгадываем число

count = 1


while number != predict_number:
    if predict_number > number:
        predict_number = np.random.randint(1, predict_number)
        count += 1
    elif predict_number < number:
        predict_number = np.random.randint(predict_number + 1, number + 1)
        count += 1
        
print(f"Вы угадали число! Это число = {number}, за {count} попыток")