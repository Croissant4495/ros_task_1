from robot_control_class import RobotControl
import math

def get_highest_lowest():
    robot = RobotControl()
    laser_list = robot.get_laser_full()
    highest_lowest_index = [0, 0]
    for i in range(len(laser_list)):
        if not(math.isinf(laser_list[i])):
            if laser_list[i] > laser_list[highest_lowest_index[0]]:
                highest_lowest_index[0] = i
            elif laser_list[i] < laser_list[highest_lowest_index[1]]:
                highest_lowest_index[1] = i

    return highest_lowest_index[0], highest_lowest_index[1]
        

