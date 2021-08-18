from collections import namedtuple

class Robot:
    """
    Robot class to represent the toy robot and methods to aid its movements
    ...
    Attributes
    ----------
    max_x : int
        x coord in n * n dimention of the square table top
    max_y : int
        y coord in n * n dimention of the square table top
    cur_pos : namedtuple
        current position of the toy robot
    valid_actions : list
        valid moves accepted by the robot as input
    debug : bool
        debug flag to start robot in debug mode
    """
    def __init__(self, max_x=5, max_y=5):
        Pos = namedtuple('Pos', ['x', 'y', 'd'])
        self.cur_pos = Pos(-1, -1, 'NORTH')
        self.max_x = max_x
        self.max_y = max_y
        self.directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        self.valid_actions = ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']
        self.action = None
        self.x = 0
        self.y = 0
        self.d = None

    def move(self):
        """
        Make a single step move in the facing direction, ignore any invalid 
        moves which will result in failover.
        """
        new_pos = self.cur_pos
        
        if self.cur_pos.d == 'NORTH':
            new_pos = new_pos._replace(y=self.cur_pos.y + 1)
        if self.cur_pos.d == 'SOUTH':
            new_pos = new_pos._replace(y=self.cur_pos.y - 1)
        if self.cur_pos.d == 'WEST':
            new_pos = new_pos._replace(x=self.cur_pos.x - 1)
        if self.cur_pos.d == 'EAST':
            new_pos = new_pos._replace(x=self.cur_pos.x + 1)
        if (-1 < new_pos.x < self.max_x) and (-1 < new_pos.y < self.max_y):
            self.cur_pos = self.cur_pos._replace(x=new_pos.x, y=new_pos.y, d=new_pos.d)
        else:
            raise Exception(f'Invalid move x: {self.cur_pos.x} y: {self.cur_pos.y} d: {self.cur_pos.d}')

    def turn_left(self):
        """
        Rotate the robot 90 degrees left without changing the position
        """
        x = self.directions.index(self.cur_pos.d)
        self.cur_pos = self.cur_pos._replace(d=self.directions[(x - 1) % len(self.directions)])

    def turn_right(self):
        """
        Rotate the robot 90 degrees right without changing the position
        """
        x = self.directions.index(self.cur_pos.d)
        self.cur_pos = self.cur_pos._replace(d=self.directions[(x + 1) % len(self.directions)])

    def place(self, x=-1, y=-1, d='NORTH'):
        """
        Place the robot on the table in position x, y and facing d
        d is either NORTH, SOUTH, EAST or WEST. Ignore any invalid placement 
        which will result in failover
        """
        if (-1 < x < self.max_x) and (-1 < y < self.max_y) and d in self.directions:
            self.cur_pos = self.cur_pos._replace(x=x, y=y, d=d)
        else:
            raise Exception(f'Invalid placement x: {x} y: {y} d: {d}')

    def validate_move(self, move):
        """
        Check if the next move is a valid move. Only the action is validated and not the actual move.
        If yes, assign the next action and (x, y, d) in case the action is 'PLACE'
        """
        status = True

        try:
            action = move.split()

            if action[0] not in self.valid_actions:
                raise

            self.action = action[0]

            if self.action == 'PLACE':
                x, y, d = action[1].split(',')
                self.x = int(x)
                self.y = int(y)
                self.d = d
            elif len(action) > 1:
              raise  
        except:
            status = False
        return status

    def run(self):
        """"
        Main running loop
        """
        while True:
            try:
                move = input()

                if not self.validate_move(move):
                    continue

                if self.action == 'PLACE':
                    self.place(x=self.x, y=self.y, d=self.d)

                if self.action == 'MOVE':
                    self.move()

                if self.action == 'LEFT':
                    self.turn_left()
                    
                if self.action == 'RIGHT':
                    self.turn_right()

                if self.action == 'REPORT' and self.cur_pos.x != -1:
                    print(f'Output: {self.cur_pos.x},{self.cur_pos.y},{self.cur_pos.d}')
                    break
            except Exception as e:
                pass

if __name__ == '__main__':
    i_robot = Robot()
    i_robot.run()