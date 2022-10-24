# Tylor Menegay
# ID: 001481631
# July 29, 2022

import Deliveries
import Packages
import HashTable
import Trucks
import datetime

class Main:
# this is the main display message when the program runs
    splash_screen = input('''
    ----------------------------------------------------
     Hello, please choose an option from below:
         -To view total mileage please type:         1
         -To view any package details type:          2
         -To view packages from at a given time:     3
         -To leave the program at any time type:     4
    ----------------------------------------------------
    ''')
# While loop breaks if the user inputs 4
    while splash_screen != '4':
        #if the user presses 1 this calls the distance_total() method in Deliveries and displays the total distance traveled
        if splash_screen == '1':
            print(f'Route was completed in {Deliveries.distance_total():.2f} miles.\n')
            exit()
        # If the user presses 2 the user is prompted to enter the packageID and time to see a packages status at a given time
        elif splash_screen == '2':
            try:
                id_lookup = input('Please enter the package ID that you are seeking: ')
                departure_location = Packages.get_hash_table().search(str(id_lookup))[9]
                current_location = Packages.get_hash_table().search(str(id_lookup))[10]
                current_time = input('Please enter a time: ')
                (h, m, s) = current_time.split(':')
                convert_general_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = departure_location.split(':')
                convert_departure_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = current_location.split(':')
                convert_current_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                if convert_departure_time >= convert_general_time:

                    Packages.get_hash_table().search(str(id_lookup))[10] = 'At Hub'
                    Packages.get_hash_table().search(str(id_lookup))[9] = 'Leaves at ' + departure_location
                    print('Package ID:', Packages.get_hash_table().search(str(id_lookup))[0], '   Street address:',
                        Packages.get_hash_table().search(str(id_lookup))[2], Packages.get_hash_table().search(str(id_lookup))[3],
                        Packages.get_hash_table().search(str(id_lookup))[4], Packages.get_hash_table().search(str(id_lookup))[5],
                        '  Required delivery time:', Packages.get_hash_table().search(str(id_lookup))[6],
                        ' Package weight:', Packages.get_hash_table().search(str(id_lookup))[7], '  Truck status:',
                        Packages.get_hash_table().search(str(id_lookup))[9], '  Delivery status:',
                        Packages.get_hash_table().search(str(id_lookup))[10])
                elif convert_departure_time <= convert_general_time:

                    if convert_general_time < convert_current_time:
                        Packages.get_hash_table().search(str(id_lookup))[10] = 'In transit'
                        Packages.get_hash_table().search(str(id_lookup))[9] = 'Left at ' + departure_location
                        print('Package ID:', Packages.get_hash_table().search(str(id_lookup))[0], '   Street address:',
                              Packages.get_hash_table().search(str(id_lookup))[2], Packages.get_hash_table().search(str(id_lookup))[3],
                              Packages.get_hash_table().search(str(id_lookup))[4], Packages.get_hash_table().search(str(id_lookup))[5],
                              '  Required delivery time:', Packages.get_hash_table().search(str(id_lookup))[6],
                              ' Package weight:', Packages.get_hash_table().search(str(id_lookup))[7], '  Truck status:',
                              Packages.get_hash_table().search(str(id_lookup))[9], '  Delivery status:',
                              Packages.get_hash_table().search(str(id_lookup))[10])

                    else:
                         Packages.get_hash_table().search(str(id_lookup))[10] = 'Delivered at ' + current_location
                         Packages.get_hash_table().search(str(id_lookup))[9] = 'Left at ' + departure_location
                         print('Package ID:', Packages.get_hash_table().search(str(id_lookup))[0], '   Street address:',
                               Packages.get_hash_table().search(str(id_lookup))[2], Packages.get_hash_table().search(str(id_lookup))[3],
                               Packages.get_hash_table().search(str(id_lookup))[4], Packages.get_hash_table().search(str(id_lookup))[5],
                               '  Required delivery time:', Packages.get_hash_table().search(str(id_lookup))[6],
                               ' Package weight:', Packages.get_hash_table().search(str(id_lookup))[7], '  Truck status:',
                               Packages.get_hash_table().search(str(id_lookup))[9], '  Delivery status:',
                               Packages.get_hash_table().search(str(id_lookup))[10])
            except ValueError:
                print("Incorrect Entry")
                exit()
        # If the user presses 3 the user is prompted to enter the time to see all packages at a given time
        elif splash_screen == '3':
            try:
                package_status_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                for id_lookup in range(1, 41):
                    try:
                        departure_location =  Packages.get_hash_table().search(str(id_lookup))[9]
                        current_location =  Packages.get_hash_table().search(str(id_lookup))[10]
                        (h, m, s) = departure_location.split(':')
                        convert_departure_location = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = current_location.split(':')
                        convert_current_location = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass

                    if convert_departure_location >= convert_user_time:
                        Packages.get_hash_table().search(str(id_lookup))[10] = 'At Hub'
                        Packages.get_hash_table().search(str(id_lookup))[9] = 'Leaves at ' + departure_location
                        print('Package ID:',  Packages.get_hash_table().search(str(id_lookup))[0], '   Street address:',
                              Packages.get_hash_table().search(str(id_lookup))[2],  Packages.get_hash_table().search(str(id_lookup))[3],
                              Packages.get_hash_table().search(str(id_lookup))[4],  Packages.get_hash_table().search(str(id_lookup))[5],
                              '  Required delivery time:',  Packages.get_hash_table().search(str(id_lookup))[6],
                              ' Package weight:', Packages.get_hash_table().search(str(id_lookup))[7], '  Truck status:',
                              Packages.get_hash_table().search(str(id_lookup))[9], '  Delivery status:',
                              Packages.get_hash_table().search(str(id_lookup))[10])
                    elif convert_departure_location <= convert_user_time:

                        if convert_user_time < convert_current_location:
                            Packages.get_hash_table().search(str(id_lookup))[10] = 'In transit'
                            Packages.get_hash_table().search(str(id_lookup))[9] = 'Left at ' + departure_location
                            print('Package ID:',  Packages.get_hash_table().search(str(id_lookup))[0], '   Street address:',
                                  Packages.get_hash_table().search(str(id_lookup))[2],  Packages.get_hash_table().search(str(id_lookup))[3],
                                  Packages.get_hash_table().search(str(id_lookup))[4],  Packages.get_hash_table().search(str(id_lookup))[5],
                                  '  Required delivery time:',  Packages.get_hash_table().search(str(id_lookup))[6],
                                  ' Package weight:',  Packages.get_hash_table().search(str(id_lookup))[7], '  Truck status:',
                                  Packages.get_hash_table().search(str(id_lookup))[9], '  Delivery status:',
                                  Packages.get_hash_table().search(str(id_lookup))[10])

                        else:
                            Packages.get_hash_table().search(str(id_lookup))[10] = 'Delivered at ' + current_location
                            Packages.get_hash_table().search(str(id_lookup))[9] = 'Left at ' + departure_location
                            print('Package ID:',  Packages.get_hash_table().search(str(id_lookup))[0], '   Street address:',
                                  Packages.get_hash_table().search(str(id_lookup))[2], Packages.get_hash_table().search(str(id_lookup))[3],
                                  Packages.get_hash_table().search(str(id_lookup))[4], Packages.get_hash_table().search(str(id_lookup))[5],
                                  '  Required delivery time:',  Packages.get_hash_table().search(str(id_lookup))[6],
                                  ' Package weight:',  Packages.get_hash_table().search(str(id_lookup))[7], '  Truck status:',
                                  Packages.get_hash_table().search(str(id_lookup))[9], '  Delivery status:',
                                  Packages.get_hash_table().search(str(id_lookup))[10])
            except IndexError:
                print(IndexError)
                exit()

