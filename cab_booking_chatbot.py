import secrets

routes = {
    1: ("Pune Station", "Shivajinagar", 5),
    2: ("Swargate", "Kothrud", 8),
    3: ("Hinjawadi", "Wakad", 10)
}

cabs = {
    1: ("Auto", 12),
    2: ("Sedan", 18),
    3: ("SUV", 25)
}

while True:
    print("\nMain Menu")
    print("1. Book Ride")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter 1 or 2.")
        continue

    if choice == 2:
        print("Thank you. Goodbye!")
        break
    elif choice != 1:
        print("Invalid choice. Please select 1 or 2.")
        continue

    print("\nChoose Cab Type")
    print("1. Auto")
    print("2. Sedan")
    print("3. SUV")

    try:
        cab_choice = int(input("Enter cab choice: "))
    except ValueError:
        print("Invalid cab choice. Returning to main menu.")
        continue

    if cab_choice not in cabs:
        print("Invalid cab choice. Returning to main menu.")
        continue

    print("\nChoose Route")
    for number, (source, destination, distance) in routes.items():
        print(f"{number}. {source} to {destination} - {distance} km")

    try:
        route_choice = int(input("Enter route choice: "))
    except ValueError:
        print("Invalid route choice. Returning to main menu.")
        continue

    if route_choice not in routes:
        print("Invalid route choice. Returning to main menu.")
        continue

    cab_name, rate = cabs[cab_choice]
    source, destination, distance = routes[route_choice]
    fare = rate * distance

    print("\nRide Details")
    print(f"Cab Type: {cab_name}")
    print(f"Source: {source}")
    print(f"Destination: {destination}")
    print(f"Distance: {distance} km")
    print(f"Rate: Rs. {rate}/km")
    print(f"Total Fare: Rs. {fare}")

    while True:
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        try:
            confirm_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        if confirm_choice == 2:
            print("Ride cancelled. No OTP was shared.")
            break
        elif confirm_choice == 1:
            otp = secrets.randbelow(9000) + 1000
            print(f"Your OTP is: {otp}")
            print("Booking confirmed.")
            print("Cancellation is not allowed after OTP sharing.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")