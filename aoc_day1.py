mess = open("day1_input.txt", 'r')
mess_r = mess.read()
mess_list = mess_r.split("\n")

# day 1 part 1
def get_mess_sum(mess_list):
    mess_sum = 0
    for i in mess_list:
        mess_sum += int(int(i)/3)-2
    return mess_sum
#print(get_mess_sum(mess_list))

# day 1 part 2
def mess_w_fuel(mess_list):
    mess_sum = 0
    for i in mess_list:
        mess_sum += get_mess_sum(int(i))
    return mess_sum

def get_mess_sum(mess):
    fuel_need = int(mess/3)-2
    if fuel_need <= 0:
        return 0
    else:
        return get_mess_sum(fuel_need)+ fuel_need
#print(mess_w_fuel(mess_list))

mess.close()
