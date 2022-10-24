import csv
from HashTable import HashTable
# Reads the Package.csv file
with open('./CSV/Package.csv') as file:
    package_reader = csv.reader(file, delimiter=',')
    hash_table = HashTable()
    first_truck = []
    second_truck = []
    third_truck = []

    # Creates package details to insert into the hashtable based off the Package.csv file
    for row in package_reader:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        start_time = ''
        current_location = ''
        current_status = 'At the hub'

        value = [id, current_location, address, city, state, zip, delivery, size, note, start_time, current_status]

        # My way of loading the truck efficiently, this could be tweaked in the future to be more efficient.
        if 'Must be delivered with' in value[8] or 'None' in value[8] and 'Delayed' not in value[6] and 'Can only be' not in value[8] and 'EOD' not in value[6]:
            first_truck.append(value)

        if 'Delayed' in value[8] or 'Can only be' in value[8] or '84111' in value[5] or '84103' in value[5] or '84102' in value[5] or '84104' in value[5] and 'Wrong' not in value[8]:
            second_truck.append(value)

        if value not in first_truck and value not in second_truck:
            third_truck.append(value)

        # inserts value into the Hash Table
        hash_table.insert(id, value)

    # getter for the first truck
    def get_first_truck():
        return first_truck

    # getter for the second truck
    def get_second_truck():
        return second_truck

    # getter for the third truck
    def get_third_truck():
        return third_truck

    # getter for the hash table
    def get_hash_table():
        return hash_table
