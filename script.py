# this is a recommendation system as a project for codecademy
# test data
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China',['historical site', 'art']]

#method -- get destination index number
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# test print for get_destination_index -- uncomment to test
# print(get_destination_index("Los Angeles, USA"))
# print(get_destination_index("Paris, France"))
# test print for get destination index -- not in list error
# print(get_destination_index("Hyderabad, India"))  

#method -- get travelers location
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

#test for get_traveler_location method
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
