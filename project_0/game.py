"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

predict_number = np.random.randint(1, 101) # отгадываем число

min_number = 1
max_number = 100
count = 1


while number != predict_number:
    
    if predict_number > number:
        max_number = predict_number

    elif predict_number < number:
        min_number = predict_number
    
    predict_number = round((max_number + min_number)/2)
    count += 1
        
print(f"Вы угадали число! Это число = {number}, за {count} попыток")