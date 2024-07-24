# mars-rover

Moves on a tile set of size 5x5 units. Any commands made that would mean the robot is out of range will be ignored.

To be used from the command line, can use these commands:
- PLACE X,Y,F 
- MOVE
- LEFT
- RIGHT 
- REPORT

X is the x-coordinate, Y is the y-coordinate and f is the direction that the robot will be facing (NORTH, EAST, SOUTH, WEST)
Example:

```
PLACE 1,2,NORTH
MOVE
RIGHT
MOVE 
REPORT
```

There are attached unit tests that demonstrate and check the functionality of the code. 

## Running locally

To install dependencies run:
```
pip install requirements
```