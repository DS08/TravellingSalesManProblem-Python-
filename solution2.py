class City():


    def __init__(self, index, name, p, neighbours):
        self.index = index
        self.name = name
        self.p = p
        self.neighbours = neighbours
        self.distance = 2000001




s = input('Enter the number of test cases:')


index = 1
while(s):
    n = input('Enter the number of cities')
    list_of_cities = []
    while(n):

        name = raw_input('Enter the name of city')
        p = input('Enter the number of neighbours')
        neighbours = {}
        x = p
        while(x):
            nr_cost = raw_input('Index Cost')
            l = nr_cost.split(' ')
            neighbours[int(l[0])] = int(l[1])

            x -=1

        city = City(index, name, p, neighbours)
        list_of_cities.append(city)
        
        index +=1    
        n -=1
    r = input('Enter the number of routes to find')

    while(r):
        flag = 0
        source_destination = raw_input('source destination: ')
        source = source_destination.split(' ')[0]
        destination = source_destination.split(' ')[1]
        
        for elm in list_of_cities:
            if elm.name == source:
                city_source = elm
            if elm.name == destination:
                city_destination = elm
        
        city_source.distance = 0
        not_visited_cities = list_of_cities
        not_visited_cities.remove(city_source)
        visited_cities = [city_source]
        
        while(not_visited_cities):
            
            neighbours = city_source.neighbours
            for index in neighbours:
                for elm in list_of_cities:
                    if elm.index == index:
                        neighbour_city = elm
                        break
                if (neighbour_city in not_visited_cities):
                    if(neighbour_city.distance>neighbours[index]+city_source.distance):
                        neighbour_city.distance = neighbours[index]+city_source.distance
            min_distance_city = not_visited_cities[0]

            for elm in not_visited_cities[1:len(not_visited_cities)]:
                if elm.distance < min_distance_city.distance:
                    min_distance_city = elm

            city_source = min_distance_city
            not_visited_cities.remove(city_source)
            visited_cities = visited_cities+[city_source]
            
        print("The cost of path from source to destination is: "+str(city_destination.distance))
        
        r -=1
        
    print('\n')
    s -=1

