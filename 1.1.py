i=0
while True:
    user_name = input("What is your name? \n >> ")
    user_origin = input("Where are you departing from? \n >> ")
    user_destination = input("Where is your destination? \n >> ")

    user_tuple = (user_name, user_origin, user_destination)
    i+=1
    print(f"Itinerary {i}: {user_name} - From {user_origin} to {user_destination}.")
    if again.lower() == "yes":
        continue
    else:
        break