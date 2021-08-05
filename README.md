# Robot App

This application is a simulation of a toy robot moving on a square table top, of dimensions n units x n units. It is assumed that there are no other obstructions on the table surface. The robot will roam around freely on the surface of the table, but will not fall to destruction. Any movement that would result in the robot falling from the table is prevented, however further valid movement commands are still be allowed.

## Usage
This application takes input from the console. PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0) can be considered to be the SOUTH WEST most corner. It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application will discard all commands in the sequence until a valid PLACE command has been executed. MOVE will move the toy robot one unit forward in the direction it is currently facing. LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot. REPORT will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient. A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands.

### Run
```bash
py main.py
```

### Examples of use

a)----------------
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH
