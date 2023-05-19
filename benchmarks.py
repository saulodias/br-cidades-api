import timeit
import random

# Define the data file path
data_file = 'BR_Municipios_2022.zip'

# Example usage

# Define the range for random coordinates
min_latitude = 4.644653
max_latitude = 32.902772
min_longitude = -74.997126
max_longitude = -32.692631

# Generate random coordinates within the specified range
random_coordinates = [(random.uniform(min_latitude, max_latitude), random.uniform(min_longitude, max_longitude)) for _ in range(1000)]

print(random_coordinates)

# Using MunicipalityQueryGenerator
generator_setup = f'''
from municipality_query import MunicipalityQueryGenerator
query_generator = MunicipalityQueryGenerator("{data_file}")
'''

generator_code = '''
for latitude, longitude in random_coordinates:
    query_generator.query_municipality(latitude, longitude)
'''

generator_time = timeit.timeit(generator_code, setup=generator_setup, number=1, globals=globals())

# Using MunicipalityQueryList
list_setup = f'''
from municipality_query import MunicipalityQueryList
query_list = MunicipalityQueryList("{data_file}")
'''

list_code = '''
for latitude, longitude in random_coordinates:
    query_list.query_municipality(latitude, longitude)
'''

list_time = timeit.timeit(list_code, setup=list_setup, number=1, globals=globals())

fraction = list_time / generator_time * 100

print(f"Generator Approach Time: {generator_time} seconds")
print(f"List Approach Time: {list_time} seconds")
print(f"List Time as a Fraction of Generator Time: {fraction:.2f}%")