import Trucks
import Packages

# declaring all variables used in this class
first_delivery_distance = []
first_delivery = []
second_delivery_distance = []
second_delivery = []
third_delivery_distance = []
third_delivery = []

first_route_start = ['8:00:00']
second_route_start = ['9:07:00']
third_route_start = ['11:30:00']

# Loop to set first_route_start time to get_first_truck
for index, value in enumerate(Packages.get_first_truck()):
    Packages.get_first_truck()[index][9] = first_route_start[0]
    first_delivery.append(Packages.get_first_truck()[index])

# Loop to compare addresses in the list
for index, outer in enumerate(first_delivery):
    for inner in Trucks.get_address():
        if outer[2] == inner[2]:
            first_delivery_distance.append(outer[0])
            first_delivery[index][1] = inner[0]

# Calling sorting algorithm get_shortest_distance
Trucks.get_shortest_distance(first_delivery, 1, 0)
first_total_distance = 0

# Calculates the total distance of the first trucks deliveries and the distances the truck travels
for index in range(len(Trucks.first_truck_index())):
    try:
        first_total_distance = Trucks.get_distance(int(Trucks.first_truck_index()[index]),
                                                 int(Trucks.first_truck_index()[index + 1]), first_total_distance)

        deliver_package = Trucks.get_times(Trucks.get_current_location(int(Trucks.first_truck_index()[index]),
                                                                          int(Trucks.first_truck_index()[index + 1])),
                                            first_route_start)
        Trucks.first_truck_list()[index][10] = (str(deliver_package))
        Packages.get_hash_table().insert(int(Trucks.first_truck_list()[index][0]), first_delivery)
    except IndexError:
        pass

# Loop to set second_route_start time to get_second_truck
for index, value in enumerate(Packages.get_second_truck()):
    Packages.get_second_truck()[index][9] = second_route_start[0]
    second_delivery.append(Packages.get_second_truck()[index])

# Loop to compare addresses in the list
for index, outer in enumerate(second_delivery):
    for inner in Trucks.get_address():
        if outer[2] == inner[2]:
            second_delivery_distance.append(outer[0])
            second_delivery[index][1] = inner[0]

# Calling sorting algorithm get_shortest_distance
Trucks.get_shortest_distance(second_delivery, 2, 0)
second_total_distance = 0

# Calculates the total distance of the second trucks deliveries and the distances the truck travels
for index in range(len(Trucks.second_truck_index())):
    try:
        second_total_distance = Trucks.get_distance(int(Trucks.second_truck_index()[index]),
                                                 int(Trucks.second_truck_index()[index + 1]), second_total_distance)

        deliver_package = Trucks.get_times(Trucks.get_current_location(int(Trucks.second_truck_index()[index]),
                                                                          int(Trucks.second_truck_index()[
                                                                                  index + 1])), second_route_start)
        Trucks.second_truck_list()[index][10] = (str(deliver_package))
        Packages.get_hash_table().insert(int(Trucks.second_truck_list()[index][0]), second_delivery)
    except IndexError:
        pass

# Loop to set third_route_start time to get_third_truck
for index, value in enumerate(Packages.get_third_truck()):
    Packages.get_third_truck()[index][9] = third_route_start[0]
    third_delivery.append(Packages.get_third_truck()[index])

# Loop to compare addresses in the list
for index, outer in enumerate(third_delivery):
    for inner in Trucks.get_address():
        if outer[2] == inner[2]:
            third_delivery_distance.append(outer[0])
            third_delivery[index][1] = inner[0]

# Calling sorting algorithm get_shortest_distance
Trucks.get_shortest_distance(third_delivery, 3, 0)
third_total_distance = 0

# Calculates the total distance of the third trucks deliveries and the distances the truck travels
for index in range(len(Trucks.third_truck_index())):
    try:
        third_total_distance = Trucks.get_distance(int(Trucks.third_truck_index()[index]),
                                                 int(Trucks.third_truck_index()[index + 1]), third_total_distance)

        deliver_package = Trucks.get_times(Trucks.get_current_location(int(Trucks.third_truck_index()[index]),
                                                                          int(Trucks.third_truck_index()[index + 1])),
                                            third_route_start)
        Trucks.third_truck_list()[index][10] = (str(deliver_package))
        Packages.get_hash_table().insert(int(Trucks.third_truck_list()[index][0]), third_delivery)
    except IndexError:
        pass

# This methods calculates the total distance all three trucks have traveled.
def distance_total():
    return first_total_distance + second_total_distance + third_total_distance
