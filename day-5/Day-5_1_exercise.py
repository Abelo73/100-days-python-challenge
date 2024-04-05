# Average Height Exercise

# heights = [156, 178, 165, 171, 187]

heights = (input("Input a list of student heights: ")).split()

total_height = 0
total_length = len(heights)

for height in heights:
    # print(int(height))
    total_height = int(total_height )+ int(height)
average_height = total_height / total_length
print(round(average_height))

    

