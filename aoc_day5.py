# not finish

def aircon_intcode(code_list, input_value):
    position = 0
    while position < len(code_list):
        if code_list[position] == '1':
            num1 = int(code_list[int(code_list[position+1])])
            num2 = int(code_list[int(code_list[position+2])])
            code_list[int(code_list[position+3])] = str(num1 + num2)
            position += 4
        elif code_list[position] == '2':
            num1 = int(code_list[int(code_list[position+1])])
            num2 = int(code_list[int(code_list[position+2])])
            code_list[int(code_list[position+3])] = str(num1 * num2)
            position += 4
        elif code_list[position] == '3':
            code_list[int(code_list[position+1])] = input_value
            position += 2
        elif code_list[position] == '4':
            print(code_list[int(code_list[position+1])])
            position += 2
        elif code_list[position] == '99':
            break
    return code_list

# input
day5_input = open("day5_input.txt", "r")
day5 = day5_input.read().split(",")
print(aircon_intcode(['3','0','4','0','99'],"9999999"))
