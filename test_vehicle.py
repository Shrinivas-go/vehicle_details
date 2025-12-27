from vehicle import vehicle_details
expected_output = (
    "Vehicle ID: 101\n"
    "Vehicle Name: Alto\n"
    "Price: 600000\n"
    "Year Of Purchase: 2016"
)
assert vehicle_details(101,"Alto",600000, 2016) == expected_output