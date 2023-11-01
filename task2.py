from robot_control_class import RobotControl

my_robot = RobotControl()

def move_till_wall(robot):
    dist = robot.get_laser(360)
    while dist > 1:
        robot.move_straight()
        dist = robot.get_laser(360)
    robot.stop_robot()

def turn_90(robot, dir="clockwise"):
    robot.turn(dir, 0.3, 5)
    robot.stop_robot()

move_till_wall(my_robot)
turn_90(my_robot)

