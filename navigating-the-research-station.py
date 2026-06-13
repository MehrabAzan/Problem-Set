def navigate_research_station(station_layout, observations):
    dictionary = dict()

    for i, point in enumerate(station_layout):
        dictionary[i] = point

    

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))