def vehicle_details(vid, vname, price, yop):
    result = (
        f"Vehicle ID: {vid}\n"
        f"Vehicle Name: {vname}\n"
        f"Price: {price}\n"
        f"Year Of Purchase: {yop}"
    )
    return result


if __name__ == "__main__":
    vid = 101
    vname = "Alto"
    price = 600000
    yop = 2016
    print(vehicle_details(vid, vname, price, yop))
