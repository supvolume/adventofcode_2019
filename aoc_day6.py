# day 6 part 1 and 2
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def draw_orbit(orbit_str,start_or_end = "start"):
    day6_all_star = set(orbit_str.replace(")","\n").split("\n"))
    day6_list = orbit_str.split("\n")
    orbit_begin = find_orbit(orbit_str, start_or_end) # object that orbit nothing, begining of the line
    df = pd.DataFrame(0,columns = day6_all_star, index = day6_all_star)
    for i in day6_list:
        orbit = i.split(")")
        df[orbit[0]][orbit[1]] = 1
        df[orbit[1]][orbit[0]] = 1
    print(df)
    
    #create the network
    orbit_network = nx.from_pandas_adjacency(df)
    print(nx.info(orbit_network))
    distance_sum = 0

    for j in day6_all_star:
        if j != orbit_begin:
            distance = nx.resistance_distance(orbit_network, orbit_begin, j)
            distance_sum += distance
    print(distance_sum)
    
    # for part 2
    print(nx.resistance_distance(orbit_network, "YOU", "SAN") - 2)

    """
    # draw the graph, not good for large data
    nx.draw(orbit_network, with_labels=True, node_size=3)
    plt.show()
    """

def find_orbit(orbit_str,start_or_end = "start"):
    day6_all_star = set(orbit_str.replace(")","\n").split("\n"))
    day6_list = orbit_str.split("\n")
    df = pd.DataFrame(0,columns = day6_all_star, index = day6_all_star)
    for i in day6_list:
        orbit = i.split(")")
        df[orbit[0]][orbit[1]] = 1
    if start_or_end == "start":
        df['start'] = df.sum(axis = 1) # to find the bigining of the line
        orbit_start = df['start'] == 0
        return df[orbit_start].index.values[0] # return the name of the bigining of the line
    else:
        df['end'] = df.sum(axis = 0) # to find the end of the line
        orbit_end = df['end'] == 0 
        return df[orbit_end].index.values[0] # return the name of the end of the line

# input
input_day6 = open("day6_input.txt", "r")
day6 = input_day6.read()
draw_orbit(day6)

#test
input_test = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
#draw_orbit(input_test)
