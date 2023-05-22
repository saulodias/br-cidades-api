import csv
import random
import os.path

# Define the latitude and longitude constraints
min_latitude = 4.644653
max_latitude = 32.902772
min_longitude = -74.997126
max_longitude = -32.692631

# Define the number of coordinates to generate
num_coordinates = 5000

# Check if the CSV file already exists
csv_file = 'coordinates.csv'
if not os.path.isfile(csv_file):

    # Generate random coordinates
    coordinates = []
    for _ in range(num_coordinates):
        latitude = random.uniform(min_latitude, max_latitude)
        longitude = random.uniform(min_longitude, max_longitude)
        coordinates.append((latitude, longitude))

    # Write coordinates to CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['latitude', 'longitude'])
        writer.writerows(coordinates)

    print('CSV file generation complete.')
else:
    print('CSV file already exists.')
