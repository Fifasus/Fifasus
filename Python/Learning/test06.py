
car_command = ""
started = False

while True:
    car_command = input("> ").lower()

    if car_command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
              """)

    elif car_command == "start":
        if started:
            print("The car is already started.")
        else:
            started = True
            print("car started...")
        
    elif car_command == "stop":
        if not started:
            print("The car is already stopped.")
        else:
            started = False
            print("Car stopped.")
            
    elif car_command == "quit":
        break

    else:
        print("I don't understand that...")
