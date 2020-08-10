import datetime  # imports the module to access real time

invoice = 0  # Variable 'invoice' used to print unique receipt numbers
c = 0  # Variable 'c' is used to reference the car instances in the 'my_cars' list
car_parks_available = 20  # variable 'car_parks_available' used to keep count of available car spaces
my_cars = []  # list of cars that are in the car park, which we can add to and delete from
response = "Yes"  # variable 'response' which will accept user input. set to 'yes' initially so a pre-tesp loop below in the program is initaited


# Below is a object class called 'Car'. Everytime we want a car instance in the program we refer to this class

class Car:
    def __init__(self, rego, size,
                 dt_started):  # This function creates a new car instance with three attributes; 'rego', 'size', 'time'
        self.rego = rego
        self.size = size
        self.time = dt_started

    def carpays(self):
        dt_ended = datetime.datetime.utcnow()  # This function calculates the difference between the car's entry time and exit time and returns the 'cost' back to the main program
        dt_started = self.time
        Time_Spent = ((dt_ended - dt_started).total_seconds())
        cost = 10 / 60 / 60 * Time_Spent  # The cost is calculated by the second based on $10 per hour - Your assignment is different. You could change the data type to reflect better decimal places if you like
        return cost

    def produce_receipt(self, cost, my_cars, invoice,
                        plate):  # This function is called when payment is made. It produces a recipt (Text in the CLS)
        invoice = invoice + 1  # Increments the invoice variable to use as the recipt number
        print("Thankyou for staying with George's Family Carpark")
        print("The cost of your stay was $ ", cost)
        print("You recipt number is ", invoice)

        for c in my_cars:  # This code searches the car list 'my_cars' for the instance of the rego number of the car that just exited.
            if c.rego == plate:
                this_one = plate
                delete_instance = my_cars.index(
                    c)  # This code finds the index of the array list that the car is stored in
                my_cars.pop(delete_instance)  # This deletes the correct car from the 'my_cars' list
                del self  # This deletes the instance of the object. Which means that once payment is made therre is no historical evidence. You may like to change this and add code to amend a file before the instance is deleted


# Below is the main program. It is a WHILE loop (Pre test loop) that will continue until a user enters 'Quit'. NB Case sensitive
while response != "Quit":
    print("Type 'New' to enter a new car")  # These print lines create the menu the user can choose from
    print("Type 'Pay' to exit a car and complete payment")
    print("Type 'Quit' to quit the program")
    response = input()  # Waits for the user to input an option. If anything else is entered than the three options, the loop will repeat
    if response == "New":
        if car_parks_available > 0:  # Checks to see if a car park is available before entering a new car
            car_parks_available = car_parks_available - 1
            print("Enter rego")
            rego = input()
            print("Enter size")
            size = input()
            dt_started = datetime.datetime.utcnow()  # Creates a variable that reads the time from the computer. This is the entry time for the car
            c = Car(rego, size,
                    dt_started)  # This calls the class 'Car' to create a new car. We pass variab;e 'rego', 'size' and 'dt_started' to the class to create the new car instance
            my_cars.append(c)  # This code adds the new car instance to our list of cars in the list array 'my_cars'
        else:
            print("No car spaces available")
    if response == "Pay":
        print(
            "Enter Rego")  # The user needs to enter the rego of a car that is in the carpark. This unique identifier will let us distinguish between all the cars in the carpark
        payment = input()
        for c in my_cars:
            if c.rego == payment:
                cost = c.carpays()  # This calls the function 'carpays' in our car class and returns the cost
                print("The cost will be $", cost)
                print("Type Yes to proceed with payment")
                recipting = input()  # This is where you would assume payment is being made
                if recipting == "Yes":
                    plate = c.rego
                    c.produce_receipt(cost, my_cars, invoice,
                                      plate)  # This calls the function 'produce_recipt' in the car class. We pass it variables that the function needs to complete a recipt and delete the instance of the car
                    car_parks_available = car_parks_available + 1  # Once a car leaves the car park we need to increment the number of available spaces

for c in my_cars:  # This is purely for test purposes to see what cars are left in the carpark when the user Quits
    print(c.rego)

for c in my_cars:  # This is purely for test purposes to see what time cars entered into the carpark when the user Quits
    print(c.time)

