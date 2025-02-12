from util import distance_to_lat_long

# distance_to_lat_long(distance_km, bearing_degrees, start_lat, start_long)
 
# Fernando: 3.24km to Rancho Dois Sabinos
# Coordinates: -23.4858936,-49.9752268
fernando_points = []
for bearing in range(360):
    point = distance_to_lat_long(3.24, bearing, -23.4858936, -49.9752268)
    fernando_points.append(point)

# Eduardo: 2.35 km to R.B. Equitação
# Coordinates: -23.482922,-49.9664249
eduardo_points = []
for bearing in range(360):
    point = distance_to_lat_long(2.35, bearing, -23.482922, -49.9664249)
    eduardo_points.append(point)

# Felipe: 2.83 km Bibi Bronze
# Coordinates: -23.4835539,-49.9707452
felipe_points = []
for bearing in range(360):
    point = distance_to_lat_long(2.83, bearing, -23.4835539, -49.9707452)
    felipe_points.append(point)


print("test")
    # Find points that are common to all three circles (intersection)
    # Convert lists to sets for set operations
fernando_set = set(fernando_points)
eduardo_set = set(eduardo_points)
felipe_set = set(felipe_points)

# Find intersection of all three sets
meeting_points = fernando_set.intersection(eduardo_set, felipe_set)

print(f"Found {len(meeting_points)} potential meeting points")
# Generate Google Maps URLs for meeting points
for point in meeting_points:
    lat, long = point
    maps_url = f"https://www.google.com/maps?q={lat},{long}"
    print(maps_url)

import code
code.interact(local=locals())

index_location_raw = input("Please enter chosen coordinate from the search.")

final_location_raw = input("Please enter the location of prospective final location")

bearing_fernando = fernando_points.index((-23.485,-49.943))
bearing_felipe = felipe_points.index((-23.485,-49.943))
bearing_eduardo = eduardo_points.index((-23.485,-49.943))

final_location = (-23.485,-49.9455749)

# reverse and double check
point = distance_to_lat_long(3.24, -bearing_fernando, *final_location)
point = distance_to_lat_long(2.83, -bearing_felipe, *final_location)
point = distance_to_lat_long(2.35, -bearing_eduardo, *final_location)