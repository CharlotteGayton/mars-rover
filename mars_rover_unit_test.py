import unittest
from mars_rover import robot
import sys
from io import StringIO

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.mars_rover = robot()

    # Robot should initialise to 0,0 and be facing north 
    def test_initial_position(self):
        self.assertEqual(self.mars_rover.x, 0)
        self.assertEqual(self.mars_rover.y, 0)
        self.assertEqual(self.mars_rover.directions[self.mars_rover.direction_index], "NORTH")

    # Testing place within boundaries 
    def test_command_place(self):
        self.mars_rover = robot()
        self.mars_rover.command_input("PLACE 1,2,EAST")
        self.assertEqual(self.mars_rover.command_report(), "1,2,EAST")

    # Testing place outside of boundaries 
    def test_command_place(self):
        self.mars_rover = robot()
        self.mars_rover.command_input("PLACE 6,2,NORTH")
        self.assertEqual(self.mars_rover.command_report(), "Robot is not on board")

    # Testing robot moving north
    def test_robot_move(self):
        self.mars_rover = robot()
        self.mars_rover.command_input("PLACE 1,1,NORTH")
        self.mars_rover.command_input("MOVE")
        self.assertEqual(self.mars_rover.command_report(), "1,2,NORTH")

    # Testing robot can move in a direction after turning
    def test_robot_move_right(self):
        self.mars_rover = robot()
        self.mars_rover.command_input("PLACE 1,1,NORTH")
        self.mars_rover.command_input("RIGHT")
        self.mars_rover.command_input("MOVE")
        self.assertEqual(self.mars_rover.command_report(), "2,1,EAST")

    # Testing robot can cycle through each rotation clockwise 
    def test_robot_rotate(self):
        self.mars_rover = robot()
        self.mars_rover.command_input("PLACE 1,1,NORTH")
        self.mars_rover.command_input("RIGHT")
        self.assertEqual(self.mars_rover.command_report(), "1,1,EAST")
        self.mars_rover.command_input("RIGHT")
        self.assertEqual(self.mars_rover.command_report(), "1,1,SOUTH")
        self.mars_rover.command_input("RIGHT")
        self.assertEqual(self.mars_rover.command_report(), "1,1,WEST")
        self.mars_rover.command_input("RIGHT")
        self.assertEqual(self.mars_rover.command_report(), "1,1,NORTH")

    # Testing robot can cycle through each rotation anti-clockwise 
    def test_robot_rotate(self):
        self.mars_rover = robot()
        self.mars_rover.command_input("PLACE 1,1,NORTH")
        self.mars_rover.command_input("LEFT")
        self.assertEqual(self.mars_rover.command_report(), "1,1,WEST")
        self.mars_rover.command_input("LEFT")
        self.assertEqual(self.mars_rover.command_report(), "1,1,SOUTH")
        self.mars_rover.command_input("LEFT")
        self.assertEqual(self.mars_rover.command_report(), "1,1,EAST")
        self.mars_rover.command_input("LEFT")
        self.assertEqual(self.mars_rover.command_report(), "1,1,NORTH")

    # Testing whether the robot will stop before moving off the table 
    def test_robot_move_off_board(self):
        self.mars_rover = robot()
        self.mars_rover.command_input("PLACE 1,5,NORTH")
        self.mars_rover.command_input("MOVE")
        self.assertEqual(self.mars_rover.command_report(), "1,5,NORTH")

    # Testing an invalid command 
    def test_invalid_command(self):
        self.mars_rover = robot()
        captured_output = StringIO()      
        sys.stdout = captured_output   
        self.mars_rover.command_input("INVALID_COMMAND")
        sys.stdout = sys.__stdout__          
        self.assertEqual(captured_output.getvalue().strip(), "Please enter a command as demonstrated from the options above")

    # Testing an invalid direction 
    def test_command_place_invalid_direction(self):
        self.mars_rover = robot()
        captured_output = StringIO()         
        sys.stdout = captured_output          
        self.mars_rover.command_place(2, 2, "INVALID_DIRECTION")
        sys.stdout = sys.__stdout__  
        self.assertEqual(captured_output.getvalue().strip(), "f is not a direction")

    def test_invalid_data_type(self):
        self.mars_rover = robot()
        captured_output = StringIO()      
        sys.stdout = captured_output   
        self.mars_rover.command_input("PLACE one,2,NORTH")
        sys.stdout = sys.__stdout__          
        self.assertEqual(captured_output.getvalue().strip(), "x and y values must be numeric")

    def test_run(self):
        self.mars_rover = robot()
        self.mars_rover.command_input("PLACE 1,2,EAST")
        self.mars_rover.command_input("MOVE")
        self.mars_rover.command_input("MOVE")
        self.mars_rover.command_input("LEFT")
        self.mars_rover.command_input("MOVE")
        self.assertEqual(self.mars_rover.command_report(), "3,3,NORTH")

if __name__ == '__main__':
    unittest.main()