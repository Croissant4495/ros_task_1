from robot_control_class import RobotControl
import math

class ExamControl:
    def __init__(self):
        self.lasers = [0, 0]
        self.robot = RobotControl()
    
    def get_laser_readings(self):
        return [self.robot.get_laser(719), self.robot.get_laser(0)]
    
    def main(self):
        self.lasers = self.get_laser_readings()
        while not math.isinf(self.lasers[0]) or not math.isinf(self.lasers[1]):
            self.robot.move_straight()
            self.lasers = self.get_laser_readings()

        self.robot.stop_robot()
    
my = ExamControl()

my.main()