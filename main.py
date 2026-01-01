def convert_distance(distance):
    mile_from_km = distance * 1.6
    km_from_mile = distance * 0.62
    print(f"{distance} miles are equal to {mile_from_km} kilometers and {distance} kilometers are equal to {km_from_mile} miles")
# For the future: figure out how to get user input
distance = 4
convert_distance(distance)
