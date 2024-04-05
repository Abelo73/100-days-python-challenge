#Day 8.1 Area Calculator

import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

coverage = 5



# print(result)

def point_calc(height, width, coverage):
    # number_of_cans = (test_h * test_w) / coverage
    # result = round(number_of_cans)
    area = height * width
    number_of_cans = area / coverage
    result = math.ceil(number_of_cans)

    print(f"You will need {result} cans of point.")
point_calc(height=test_h, width=test_w, coverage = coverage)


    
    

