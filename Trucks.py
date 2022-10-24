import csv
import datetime

# Reads the Distance.csv file
with open('./CSV/Distance.csv') as distance_csv:
    distance_file = list(csv.reader(distance_csv, delimiter=','))

# Reads the Address.csv file
with open('./CSV/Address.csv') as address_csv:
    address_file = list(csv.reader(address_csv, delimiter=','))

    # Method to calculate the total distance from row and column values
    def get_distance(row, col, totals):
        distances = distance_file[row][col]
        if distances == '':
            distances = distance_file[col][row]

        return totals + float(distances)

    # Method to get the Address.csv data
    def get_address():
        return address_file

    # Method to calculate the current distance from the row and column values
    def get_current_location(row, col):
        distances = distance_file[row][col]
        if distances == '':
            distances = distance_file[col][row]
        return float(distances)

    # Method to calculate time it takes for the trucks to complete their route
    def get_times(distances, all_trucks):
        speed = 18
        time = distances / speed
        distance_minutes = '{0:02.0f}:{1:02.0f}'.format( *divmod(time * 60, 60))
        full_time = distance_minutes + ':00'
        all_trucks.append(full_time)
        totals = datetime.timedelta()
        for i in all_trucks:
            (hrs, mins, secs) = i.split(':')
            totals += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

        return totals

    first_trucks = []
    first_truck_indexes = []
    second_trucks = []
    second_truck_indexes = []
    third_trucks = []
    third_truck_indexes = []

    # Greedy Algorithm that recursively loops through the truck_package_list to determine the next best location to visit
    def get_shortest_distance(truck_package_list, truck_num, current_location):
        if len(truck_package_list) == 0:
            return truck_package_list
        else:
            try:
                max_packages = 16.0
                location = 0

                for i in truck_package_list:
                    if get_current_location(current_location, int(i[1])) <= max_packages:
                        max_packages = get_current_location(current_location, int(i[1]))
                        location = int(i[1])
                for i in truck_package_list:
                    if get_current_location(current_location, int(i[1])) == max_packages:
                        if truck_num == 1:
                            first_trucks.append(i)
                            first_truck_indexes.append(i[1])
                            value = truck_package_list.index(i)
                            truck_package_list.pop(value)
                            current_location = location
                            get_shortest_distance(truck_package_list, 1, current_location)
                        elif truck_num == 2:
                            second_trucks.append(i)
                            second_truck_indexes.append(i[1])
                            value = truck_package_list.index(i)
                            truck_package_list.pop(value)
                            current_location = location
                            get_shortest_distance(truck_package_list, 2, current_location)
                        elif truck_num == 3:
                            third_trucks.append(i)
                            third_truck_indexes.append(i[1])
                            value = truck_package_list.index(i)
                            truck_package_list.pop(value)
                            current_location = location
                            get_shortest_distance(truck_package_list, 3, current_location)
            except IndexError:
                pass

    first_truck_indexes.insert(0, '0')

    # getter for first_truck_index
    def first_truck_index():
        return first_truck_indexes

    # getter for first_truck_list
    def first_truck_list():
        return first_trucks

    second_truck_indexes.insert(0, '0')

    # getter for second_truck_index
    def second_truck_index():
        return second_truck_indexes

    # getter for second_truck_list
    def second_truck_list():
        return second_trucks

    third_truck_indexes.insert(0, '0')

    # getter for third_truck_index
    def third_truck_index():
        return third_truck_indexes

    # getter for third_truck_list
    def third_truck_list():
        return third_trucks

