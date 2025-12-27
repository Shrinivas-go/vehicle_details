from vehicle import vehicle_details
expected_output = (
    "Vehicle ID: 101\n"
    "Vehicle Name: Alto\n"
    "Price: 1\n"
    "Year Of Purchase: 2016"
)
assert vehicle_details(101,"Alto",1, 2016) == expected_output
