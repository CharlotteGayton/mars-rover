class robot:

    # Initialise the robot's state
    def __init__(self) -> None:
        # Initialise whether the robot is on the table or not
        self.on_table = False 

        # Robot's default coordinates, defining it not on the table 
        self.x = 0
        self.y = 0

        # The directions in which the robot can face
        self.directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        # Initialise where the robot will be facing before placement
        self.direction_index = 0

    def command_input(self, input):
        # Process the command given to the robot
        remove_grammar = input.replace(',', ' ')
        command = remove_grammar.split(' ')

        # Sort the different commands
        if command[0].upper() == "PLACE":
            # Check whether the digits entered are numerical or not
            if not command[1].isdigit() or not command[2].isdigit():
                print("x and y values must be numeric")
                return
            self.command_place(int(command[1]), int(command[2]), command[3])
        elif command[0].upper() == "MOVE":
            self.command_move()
        elif command[0].upper() == "LEFT":
            self.command_left()
        elif command[0].upper() == "RIGHT":
            self.command_right()
        elif command[0].upper() == "REPORT":
            print(self.command_report())
        else:
            print("\nPlease enter a command as demonstrated from the options above")

    def command_place(self, x, y, f):
        # Check whether the robot can be placed within the bounds of the board
        if (x <= 5) and (x >= 1):
            if (y <= 5) and (y >= 1):
                # Check that the direction the robot will be facing matches the pre-defined ones 
                if f.upper() in self.directions:        
                    self.x = x
                    self.y = y 
                    # Find the index of the direction specified by the user 
                    self.direction_index = self.directions.index(f.upper())
                    print("Robot place successful")
                else:
                    print("f is not a direction")
            else:
                print(f"y value {y} not on table")
        else:
            print(f"x value {x} not on table")

    def command_move(self):
        # Move the robot depending on the current direction it is facing 
        if self.directions[self.direction_index] == "NORTH":
            # Check whether the new coordinates are possible within the board's dimensions
            if self.check_new_coordinates(self.x, self.y + 1):
                self.y += 1
        elif self.directions[self.direction_index] == "EAST":
            if self.check_new_coordinates(self.x + 1, self.y):
                self.x += 1
        elif self.directions[self.direction_index] == "SOUTH":
            if self.check_new_coordinates(self.x, self.y - 1):
                self.y -= 1
        elif self.directions[self.direction_index] == "WEST":
            if self.check_new_coordinates(self.x - 1, self.y):
                self.x -= 1
        else: 
            print("robot could not move") 

    def check_new_coordinates(self, x, y):
        # Checking whether the coordinates are possible within the board's dimensions 
        if (x > 5) or (x < 1):
            return False
        if (y > 5) or (y < 1):
            return False
        else:
            return True

    def command_report(self):
        # Check whether the robot is on the board or not
        if (self.x == 0) and (self.y == 0):
            return "Robot is not on board"
        else:
            # Return a report on the robots current location and direction
            return f"{self.x},{self.y},{self.directions[self.direction_index]}"

    def command_left(self):
        # Take the modulus of four to determine the index of the robot's direction 
        # The modulus ensures that the numbers wrap round if the robot were to cross from the end to the start of the list (and the opposite )
        self.direction_index = (self.direction_index + 3) % 4 

    def command_right(self):
        self.direction_index = (self.direction_index + 1) % 4 

def main():
    running = True
    mars_rover = robot()
    print("You can enter a series of commands from the following: \nPLACE X,Y,F\nMOVE\nLEFT\nRIGHT\nREPORT\n\n")
    while running == True:
        mars_rover.command_input(input("Command: "))  

if __name__ == "__main__":
    main()