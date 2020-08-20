import sqlite3
import math
import operator
from matplotlib import pyplot as plt

#create class tree and initialize with parameters: spc, lat, lon
class Tree:
    def __init__(self, spc, lat, lon):
        self.species = spc
        self.latitude = lat
        self.longitude = lon
#connect to sql, assign cursor and ask for user input
conn = sqlite3.connect('./trees.db')
c = conn.cursor()
lat, lon = float(input('Latitude: ')),float(input('Longitude: '))
#start with two empty lists trees and distances, will be updated by loop
trees = []
distances = []
for row in c.execute("select spc_common, latitude, longitude from trees"):
    distance = math.sqrt((lat-float(row[1]))**2 + (lon-float(row[2]))**2)
    trees.append(Tree(row[0],row[1],row[2])) #add to trees list, spcn lat and long
    distances.append(distance) #add to distances all calculates distances using formula distance

value_ignore = max(distances) + 1 #ensures that min value will not be duplicated
found_indexes = [] #start with an empty list, run the loop 10 times, to get 10 lowest distances
for i in range (0,10):
    index, value = min(enumerate(distances), key=operator.itemgetter(1)) #find min value from distances list
    found_indexes.append(index) #add found distance to list
    distances[index] = value_ignore #updates the min value so it doesn't cause problems

species = {} #start with an empty dictionary
for found in found_indexes: #go through the entire found_indexes list
    if trees[found].species in species:
        species[trees[found].species] += 1 #if species appear more than once, update it each time through the loop
    else:
        species[trees[found].species] = 1 #the least amount of times the species appear has to be 1
    print(trees[found].species,trees[found].latitude,trees[found].longitude) #prints out the 10 closest trees, from closest to furthest

most_common_species = 0 #counter starts at 0
mcs_name = '' #will be updated once i figure out the most common species
for key in species: #go through all key value in dictionary species
    if species[key] > most_common_species: #if new species is more than current most common species, make that the new common
        most_common_species = species[key]
        mcs_name = key
print ('\nMost common species is: ',mcs_name)

x = []
y = []

for found in found_indexes:
    x.append(trees[found].latitude)
    y.append(trees[found].longitude)

plt.title('10 Closest Trees Near You!')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.scatter(lat,lon,50)
plt.scatter(x,y,10)

plt.show()

#******************************************************************************
#source link:
#https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
#https://docs.python.org/2/library/operator.html#operator.itemgetter
#https://www.youtube.com/watch?v=aS4WlOJQ4mQ
