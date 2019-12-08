# day 3 part 1
# return every coordinate wire path
def wires_path(wire):
    x = 0
    y = 0
    path = []
    for i in wire:
        if i[0] == "R":
            x_next = x + int(i[1:])
            for j in range(x+1,x_next+1):
                path.append((j,y))
            x = x_next
        elif i[0] == "L":
            x_next = x - int(i[1:])
            for j in range(x-1,x_next-1,-1):
                path.append((j,y))
            x = x_next
        elif i[0] == "U":
            y_next = y + int(i[1:])
            for j in range(y+1,y_next+1):
                path.append((x,j))
            y = y_next
        elif i[0] == "D":
            y_next = y - int(i[1:])
            for j in range(y-1,y_next-1,-1):
                path.append((x,j))
            y = y_next
    return path

# return coordinate where two paths cross
def wires_cross(path1,path2):
    path_cross = []
    for i in path2:
        if i in path1:
            path_cross.append(i)
    return path_cross

# return shortest coordinate
def short_distance(cross):
    distance = []
    for i in cross:
        distance.append(abs(i[0])+abs(i[1]))
    distance.sort()
    return distance[0]


# test day 3 part 1

eg1_wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
eg1_wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"
eg1_w1 = eg1_wire1.split(',')
eg1_w2 = eg1_wire2.split(',')
eg1_path1 = wires_path(eg1_w1)
eg1_path2 = wires_path(eg1_w2)
eg1_cross = wires_cross(eg1_path1,eg1_path2)
#print(short_distance(eg1_cross))

eg2_wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
eg2_wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
eg2_w1 = eg2_wire1.split(',')
eg2_w2 = eg2_wire2.split(',')
eg2_path1 = wires_path(eg2_w1)
eg2_path2 = wires_path(eg2_w2)
eg2_cross = wires_cross(eg2_path1,eg2_path2)
#print(short_distance(eg2_cross))

eg3_wire1 = "R8,U5,L5,D3"
eg3_wire2 = "U7,R6,D4,L4"
eg3_w1 = eg3_wire1.split(',')
eg3_w2 = eg3_wire2.split(',')
eg3_path1 = wires_path(eg3_w1)
eg3_path2 = wires_path(eg3_w2)
eg3_cross = wires_cross(eg3_path1,eg3_path2)
#print(short_distance(eg3_cross))

# input
input_wire1 = "R990,U803,R777,U157,R629,D493,R498,D606,R344,U241,L708,D403,R943,U961,L107,D755,R145,D77,L654,D297,L263,D904,R405,U676,R674,U139,L746,U935,R186,U433,L739,D774,R470,D459,R865,D209,L217,U525,R747,D218,R432,U769,L876,D477,R606,D161,R991,D338,R647,D958,R777,D148,R593,D873,L95,U707,R468,U518,R845,U285,R221,U771,R989,D107,R44,U833,L343,D420,R468,D954,L604,D270,L691,U401,R850,U70,R441,U461,R638,D743,R65,U673,L999,U110,R266,U759,R768,U569,L250,D577,R247,U420,L227,U437,L80,D647,L778,U935,R585,U35,L735,D201,R694,U635,L597,U215,R743,D542,L701,U946,L503,U589,R836,D687,L444,U409,L473,U132,L570,U374,R193,D908,L800,U294,L252,U851,R947,D647,L37,D20,L27,U620,L534,D356,L291,U611,L128,D670,L364,U200,L749,D708,R776,U99,R606,D999,L810,D373,R212,D138,R856,D966,L206,D23,L860,D731,L914,U716,L212,U225,R766,U348,L220,D69,L766,D15,L557,U71,R734,D295,R884,D822,R300,D152,L986,D170,R764,U24,R394,D710,L860,U830,L305,U431,R201,D44,R882,U667,R37,D727,R916,U460,L834,D771,R373,U96,L707,D576,R607,D351,R577,D200,L402,U364,L32,D512,L152,D283,L232,U804,R827,U352,R104,D323,L254,U273,L451,D967,R739,D53,L908,D866,R998,U897,L581,U538,R206,U644,L70,D17,L481,U912,L377,D922,L286,U547,R35,U292,L318,U256,R79,D52,R92,U160,R763,U428,R663,D634,R212,D325,R460,U142,L375,U382,R20,D321,L220,D578,R915,D465,L797,D849,L281,D491,L911,D624,R800,U629,L675,U428,L219,U694,R680,U350,R113,D903,L22,D683,L787,D1,R93,U315,L562,U756,R622,D533,L587,D216,L933,U972,R506,U536,R797,U828,L12,D965,L641,U165,R937,D675,R259"
input_wire2 = "L998,D197,L301,D874,L221,U985,L213,D288,R142,D635,R333,D328,R405,D988,L23,D917,R412,D971,R876,U527,R987,D884,R39,D485,L971,U200,R931,U79,L271,U183,R354,D18,R346,D866,L752,D204,L863,U784,R292,U676,R811,U721,L53,U983,L993,U822,R871,U539,L782,D749,R417,U667,R882,U467,R321,U894,R912,U756,L102,U154,L57,D316,R200,U372,L44,U406,L426,D613,R847,U977,R303,U469,R509,U839,L633,D267,L487,D976,R325,U399,L359,U161,L305,U935,R522,D848,R784,D273,L337,D55,L266,U406,L858,D650,L176,D124,R231,U513,L462,U328,L674,D598,R568,D742,L39,D438,L643,D254,R577,U519,R325,U124,R91,U129,L79,D52,R480,D46,R129,D997,R452,D992,L721,U490,L595,D666,R372,D198,R813,U624,L469,U59,R578,U184,R117,D749,L745,U302,R398,D951,L683,D360,R476,D788,R70,U693,R295,D547,L61,U782,R440,D818,L330,D321,L968,U622,R160,U571,L886,D43,L855,U272,R530,D267,L312,D519,L741,D697,R206,U148,L445,U857,R983,D192,L788,U826,R805,U932,R888,D250,L682,D52,R406,D176,R984,D637,L947,D416,L687,U699,L544,D710,L933,D171,L357,D134,L968,D538,R496,D240,L730,U771,R554,U708,R265,D748,L839,U668,L333,U335,R526,U809,L653,D6,R234,D130,R871,U911,R538,U372,L960,D535,L196,U236,L966,D185,L166,U789,L885,U453,R627,D586,R501,U222,L280,U124,R755,D159,L759,U78,R669,D889,L150,D888,L71,D917,L126,D97,L138,U726,R160,D971,R527,D988,R455,D413,R539,U923,R258,U734,L459,D954,R877,U613,R343,D98,R238,U478,R514,U814,L274,U119,L958,U698,R761,U693,R367,D111,L800,D531,L91,U616,R208,D255,R169,U145,R671,U969,L468,U566,R589,D455,R323,D303,R374,D890,R377,D262,L40,U85,L719"
input_w1 = input_wire1.split(',')
input_w2 = input_wire2.split(',')
input_path1 = wires_path(input_w1)
input_path2 = wires_path(input_w2)
input_cross = wires_cross(input_path1,input_path2)
#print(short_distance(input_cross))


# day 3 part 2
def step2cross(path1,path2,cross):
    step_dis = []
    for c in cross:
        count1 = 0
        count2 = 0
        for i in path1:
            if i != c:
                count1 += 1
            else:
                count1 += 1
                break
        for j in path2:
            if j != c:
                count2 += 1
            else:
                count2 += 1
                break
        step_dis.append(count1+count2)
    step_dis.sort()
    return step_dis[0]
        

# test day 3 part 2
print(step2cross(eg1_path1, eg1_path2, eg1_cross))
print(step2cross(eg2_path1, eg2_path2, eg2_cross))
print(step2cross(eg3_path1, eg3_path2, eg3_cross))
print(step2cross(input_path1, input_path2, input_cross))

# plot graph
import numpy as np
from matplotlib import pyplot as plt
path1 = np.array([input_path1])
path2 = np.array([input_path2])
x1, y1 = path1.T
x2,y2 = path2.T
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.savefig("aoc_day3_part2_path_pic.png")
