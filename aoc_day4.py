# day 4 part 1
def find_pass(pw_range):
    count = 0
    for i in range(pw_range[0],pw_range[1]+1):
        pw_list = list(str(i))
        pw_sort = sorted(pw_list)
        # password only increasing
        if pw_list == pw_sort:
            # when password have double, set will have less number than list
            if len(pw_list) != len(set(pw_list)):
                count += 1
    return count
    
# input
input_range = [152085, 670283]
#print(find_pass(input_range))

# day 4 part 2
def find_pass2(pw_range):
    count = 0
    for i in range(pw_range[0],pw_range[1]+1):
        pw_list = list(str(i))
        pw_sort = sorted(pw_list)
        # password only increasing
        if pw_list == pw_sort:
            # when password have double, set will have less number than list
            if len(pw_list) != len(set(pw_list)):
                for j in set(pw_list):
                    if pw_list.count(j) == 2:
                        count += 1
                        break
    return count

# input part 2
print(find_pass2(input_range))
