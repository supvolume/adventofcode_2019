import numpy as np
import matplotlib.pyplot as plt

#day 8 part 1
def space_image(pixel_list, wide, tall):
    layer = int(len(pixel_list)/(tall*wide))
    space_array = np.array(pixel_list).reshape(layer,tall*wide)
    
    # find the layer with fewest 0
    few_zero = 0
    number_of_zero = tall*wide
    num_of_one = 0
    num_of_two = 0
    for i in range(layer):
        if list(space_array[i]).count('0') < number_of_zero:
            few_zero = i
            number_of_zero = list(space_array[i]).count('0')
            num_of_one = list(space_array[i]).count('1')
            num_of_two = list(space_array[i]).count('2')
    print(num_of_one*num_of_two)

# day 8 part 2
def full_image(pixel_list, wide, tall):
    layer = int(len(pixel_list)/(tall*wide))
    space_array = np.array(pixel_list).reshape(layer,tall, wide)
    final_image = np.full((tall, wide),2)
    for i in range(tall):
        for j in range(wide):
            for k in range(layer):
                while final_image[i][j] == 2:
                    if space_array[k][i][j] != '2' or space_array[k][i][j] != 2:
                        final_image[i][j] = int(space_array[k][i][j])
                    break
    print(final_image)
    plt.imshow(final_image)
    plt.savefig("aoc_day8_part2_path_pic.png")
    plt.show()

# input
day8_input = open("day8_input.txt", "r")
day8 = list(day8_input.read())
#space_image(day8, 25, 6) #part 1
full_image(day8, 25, 6) # part 2
