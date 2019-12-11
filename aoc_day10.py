# not finish
class Monitor:
    def __init__(self, input_txt):
        input_t = open(input_txt,"r")
        text = input_t.read().split("\n")
        text_array = []
        for i in text:
            text_array.append(list(i))
        self.text_array = text_array
        input_t.close()

    # count the number of asteroids
    def total(self):
        count = 0
        for i in self.text_array:
            for j in i:
                if j == "#":
                    count += 1
        return count

    # find the number of asteroids that visible from the given asteroid coordinate
    def visible(self,x,y):
        width = len(self.text_array[y])
        tall = len(self.text_array)
        # north
        count_n = -1
        for i in range(y):
            if self.text_array[i][x] == "#":
                count_n += 1
        if count_n < 0:
            count_n = 0
            
        # east
        count_e = -1
        for i in range(x+1,width):
            if self.text_array[y][i] == "#":
                count_e += 1
        if count_e < 0:
            count_e = 0
        
        # west
        count_w = -1
        for i in range(x):
            if self.text_array[y][i] == "#":
                count_w += 1
        if count_w < 0:
            count_w = 0
        
        # south
        count_s = -1
        for i in range(y+1,tall):
            if self.text_array[i][x] == "#":
                count_s += 1
        if count_s < 0:
            count_s = 0
        
        # NE
        count_ne = -1
        ne_x = x
        ne_y = y
        while ne_x < width-1 and ne_y-1 >= 0:
            ne_x += 1
            ne_y -= 1
            if self.text_array[ne_y][ne_x] == "#":
                    count_ne += 1
        if count_ne < 0:
            count_ne = 0
            
        # SE
        count_se = -1
        se_x = x
        se_y = y
        while se_x < width-1 and se_y < tall-1:
            se_x += 1
            se_y += 1
            if self.text_array[se_y][se_x] == "#":
                    count_se += 1
        if count_se < 0:
            count_se = 0

        # SW
        count_sw = -1
        sw_x = x
        sw_y = y
        while sw_x-1 >= 0 and sw_y < tall-1:
            sw_x -= 1
            sw_y += 1
            if self.text_array[sw_y][sw_x] == "#":
                    count_sw += 1
        if count_sw < 0:
            count_sw = 0
            
        # NW
        count_nw = -1
        nw_x = x
        nw_y = y
        while nw_x-1 >= 0 and nw_y-1 >= 0:
            nw_x -= 1
            nw_y -= 1
            if self.text_array[nw_y][nw_x] == "#":
                    count_nw += 1
        if count_nw < 0:
            count_nw = 0
        
        return self.total()- (1 + count_n + count_e + count_w + count_s + count_ne + count_nw + count_se + count_sw)
    

    
# input
def main():
    mon = Monitor("day10_input.txt")
    print(mon.visible(6,3))

if __name__ == "__main__":
    main()
