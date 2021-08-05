import unittest
from io import StringIO
from unittest.mock import patch
from main import Robot

class TestRobot(unittest.TestCase):

    def setUp(self):
        self.test_robot = Robot(max_x=4, max_y=4, debug=True)

    def test_place_1(self):
        self.test_robot.place(x=3, y=2, d='NORTH')
        self.assertEqual(self.test_robot.cur_pos.x, 3)
        self.assertEqual(self.test_robot.cur_pos.y, 2)

    def test_move_2(self):
        self.test_robot.place(x=0, y=2, d='EAST')   
        self.test_robot.move()
        self.assertEqual(self.test_robot.cur_pos.x, 1)
        self.assertEqual(self.test_robot.cur_pos.y, 2)
        self.assertEqual(self.test_robot.cur_pos.d, 'EAST')

    def test_turn_right_north_3(self):
        self.test_robot.place(x=0, y=2, d='NORTH')   
        self.test_robot.turn_right()
        self.assertEqual(self.test_robot.cur_pos.x, 0)
        self.assertEqual(self.test_robot.cur_pos.y, 2)
        self.assertEqual(self.test_robot.cur_pos.d, 'EAST')

    def test_turn_right_east_4(self):
        self.test_robot.place(x=0, y=2, d='EAST')   
        self.test_robot.turn_right()
        self.assertEqual(self.test_robot.cur_pos.x, 0)
        self.assertEqual(self.test_robot.cur_pos.y, 2)
        self.assertEqual(self.test_robot.cur_pos.d, 'SOUTH')

    def test_turn_right_south_5(self):
        self.test_robot.place(x=0, y=2, d='SOUTH')   
        self.test_robot.turn_right()
        self.assertEqual(self.test_robot.cur_pos.x, 0)
        self.assertEqual(self.test_robot.cur_pos.y, 2)
        self.assertEqual(self.test_robot.cur_pos.d, 'WEST')

    def test_turn_right_west_6(self):
        self.test_robot.place(x=0, y=2, d='WEST')   
        self.test_robot.turn_right()
        self.assertEqual(self.test_robot.cur_pos.x, 0)
        self.assertEqual(self.test_robot.cur_pos.y, 2)
        self.assertEqual(self.test_robot.cur_pos.d, 'NORTH')


    def test_turn_left_west_7(self):
        self.test_robot.place(x=3, y=0, d='WEST')   
        self.test_robot.turn_left()
        self.assertEqual(self.test_robot.cur_pos.x, 3)
        self.assertEqual(self.test_robot.cur_pos.y, 0)
        self.assertEqual(self.test_robot.cur_pos.d, 'SOUTH')

    def test_turn_left_south_8(self):
        self.test_robot.place(x=3, y=0, d='SOUTH')   
        self.test_robot.turn_left()
        self.assertEqual(self.test_robot.cur_pos.x, 3)
        self.assertEqual(self.test_robot.cur_pos.y, 0)
        self.assertEqual(self.test_robot.cur_pos.d, 'EAST')

    def test_turn_left_east_9(self):
        self.test_robot.place(x=3, y=0, d='EAST')   
        self.test_robot.turn_left()
        self.assertEqual(self.test_robot.cur_pos.x, 3)
        self.assertEqual(self.test_robot.cur_pos.y, 0)
        self.assertEqual(self.test_robot.cur_pos.d, 'NORTH')

    def test_turn_left_north_10(self):
        self.test_robot.place(x=3, y=0, d='NORTH')   
        self.test_robot.turn_left()
        self.assertEqual(self.test_robot.cur_pos.x, 3)
        self.assertEqual(self.test_robot.cur_pos.y, 0)
        self.assertEqual(self.test_robot.cur_pos.d, 'WEST')

    def test_validate_move_11(self):
        for move in ['LEFT', 'RIGHT', 'MOVE', 'PLACE 6,6,NORTH']:
            ret = self.test_robot.validate_move(move)
            self.assertEqual(ret, True)
        for move in ['INVALID', 'PLACE 3,NORTH', 'RIGHT 6', 'MOVE NORTH']:
            ret = self.test_robot.validate_move(move)
            self.assertEqual(ret, False)

    def test_place_x_y_ex_12(self):
        with self.assertRaises(Exception) as cm:
            self.test_robot.place(x=4, y=4, d='NORTH')
        self.assertEqual(str(cm.exception), 'Invalid placement x: 4 y: 4 d: NORTH')

    def test_place_y_ex_13(self):
        with self.assertRaises(Exception) as cm:
            self.test_robot.place(x=3, y=4, d='NORTH')
        self.assertEqual(str(cm.exception), 'Invalid placement x: 3 y: 4 d: NORTH')

    def test_place_x_ex_14(self):
        with self.assertRaises(Exception) as cm:
            self.test_robot.place(x=4, y=3, d='NORTH')
        self.assertEqual(str(cm.exception), 'Invalid placement x: 4 y: 3 d: NORTH')

    def test_place_d_ex_15(self):
        with self.assertRaises(Exception) as cm:
            self.test_robot.place(x=4, y=3, d='NORT')
        self.assertEqual(str(cm.exception), 'Invalid placement x: 4 y: 3 d: NORT')

    def test_place_x_y_d_ex_16(self):
        with self.assertRaises(Exception) as cm:
            self.test_robot.place(x=4, y=4, d='NORT')
        self.assertEqual(str(cm.exception), 'Invalid placement x: 4 y: 4 d: NORT')

    def test_move_n_ex_17(self):
        self.test_robot.place(x=0, y=3, d='NORTH')
        with self.assertRaises(Exception) as cm:
            self.test_robot.move()
        self.assertEqual(str(cm.exception), 'Invalid move x: 0 y: 3 d: NORTH')

    def test_move_e_ex_18(self):
        self.test_robot.place(x=3, y=3, d='EAST')
        with self.assertRaises(Exception) as cm:
            self.test_robot.move()
        self.assertEqual(str(cm.exception), 'Invalid move x: 3 y: 3 d: EAST')

    def test_move_s_ex_19(self):
        self.test_robot.place(x=3, y=0, d='SOUTH')
        with self.assertRaises(Exception) as cm:
            self.test_robot.move()
        self.assertEqual(str(cm.exception), 'Invalid move x: 3 y: 0 d: SOUTH')

    def test_move_w_ex_20(self):
        self.test_robot.place(x=0, y=0, d='WEST')
        with self.assertRaises(Exception) as cm:
            self.test_robot.move()
        self.assertEqual(str(cm.exception), 'Invalid move x: 0 y: 0 d: WEST')

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_21(self, mock_stdout):
        action_list = ['PLACE 1,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 3,3,NORTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_22(self, mock_stdout):
        action_list = ['PLACE 0,0,NORTH', 'LEFT', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,0,WEST\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_23(self, mock_stdout):
        action_list = ['PLACE 0,0,NORTH', 'RIGHT', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,0,EAST\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_24(self, mock_stdout):
        action_list = ['PLACE 0,0,EAST', 'LEFT', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,0,NORTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_25(self, mock_stdout):
        action_list = ['PLACE 0,0,EAST', 'RIGHT', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,0,SOUTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_26(self, mock_stdout):
        action_list = ['PLACE 0,0,SOUTH', 'LEFT', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,0,EAST\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_27(self, mock_stdout):
        action_list = ['PLACE 0,0,SOUTH', 'RIGHT', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,0,WEST\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_28(self, mock_stdout):
        action_list = ['PLACE 0,0,WEST', 'LEFT', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,0,SOUTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_29(self, mock_stdout):
        action_list = ['PLACE 0,0,WEST', 'RIGHT', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,0,NORTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_30(self, mock_stdout):
        action_list = ['MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_31(self, mock_stdout):
        action_list = ['MOVE', 'PLACE 0,3,SOUTH', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,2,SOUTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_32(self, mock_stdout):
        action_list = ['MOVE', 'PLACE 0,0,WEST', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,0,WEST\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_33(self, mock_stdout):
        action_list = ['MOVE', 'PLACE 3,3,WEST', 'MOVE', 'RIGHT', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 2,3,NORTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_34(self, mock_stdout):
        action_list = ['MOVE', 'PLACE 0,0,EAST', 'MOVE', 'LEFT', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 1,1,NORTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_35(self, mock_stdout):
        action_list = ['INVALID', 'PLACE 0,0,EAST', 'MOVE', 'LEFT', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 1,1,NORTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_36(self, mock_stdout):
        action_list = ['MOVE', 'PLACE 0,0,SOUTH', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,0,SOUTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_37(self, mock_stdout):
        action_list = ['MOVE', 'PLACE 0,3,NORTH', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 0,3,NORTH\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_38(self, mock_stdout):
        action_list = ['MOVE', 'PLACE 3,0,EAST', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 3,0,EAST\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_39(self, mock_stdout):
        action_list = ['MOVE', 'PLACE 3,3,EAST', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 3,3,EAST\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_robot_run_40(self, mock_stdout):
        action_list = ['MOVE', 'PLACE 3,3,NORTH', 'MOVE', 'REPORT']
        self.test_robot.run(action_list=action_list)
        self.assertEqual('Output: 3,3,NORTH\n', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()