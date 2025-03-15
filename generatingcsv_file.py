#  programme to generate a csv file which contains some random names, eamils, age, cities

import random
import csv
import os

Names = ['Pavan', 'Abhishek', 'Venu', 'Kishore', 'Pardhu', 'Mani', 'Vasanth', 'Kalyani', 'Sravani', 'Jayaprakash', 'AKhil']
Cities = ['Hyderabad', 'Kolkata', 'Chennai', 'Bangalore', 'Mumbai', 'Pune', 'Delhi', 'Kochi', 'Noida', 'Gurgaon']

for i in range(100):
    name = random.choice(Names)
    city = random.choice(Cities)
    email = f'{name}@gmail.com'
    age = random.randint(20, 51)
    entry_list = [name, age, email, city]
    with open('random_csv.csv', 'a', newline= '') as file:
        csv_writer = csv.writer(file, delimiter= ',')
        if (not os.path.exists('random_csv.csv') or os.stat('random_csv.csv').st_size == 0):
            csv_writer.writerow(['Name', 'Age', 'Emaiil', 'City'])
        csv_writer.writerow(entry_list)