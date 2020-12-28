from device import Motor
from time import sleep
import math


class TwoWheelController:
    """The class represents the controller for a two-wheeled robot. The controller
    class must implement set_axis function.
    """

    def __init__(self):
        # super(TwoWheelController, self).__init__()
        self.right_motor = Motor(22, 23, 19)
        self.left_motor = Motor(17, 27, 18)
        self.right_motor.set_throttle(None)
        self.left_motor.set_throttle(None)


    def set_axis(self, x=0.0, y=0.0):
        """The function both control the forward / backward speed and the rotation
        speed of a two wheeled robot.

        Args:
            x (float, optional): the rotational speed of the robot. Defaults to 0.0.
            y (float, optional): the forward / backward speed of the robot. Defaults to 0.0.
        """

        # for val in [-0.5, -1]:
        #     self.right_motor.set_throttle(val)
        #     sleep(1)
        # # Set motor to stop mode.
        # self.right_motor.set_throttle(None)

        left = x + y
        left = max(-1.0, min(1.0, left))  # Clamp to [-1, 1]
        left = None if math.isclose(left, 0.0) else left
        

        right = -x + y
        right = max(-1.0, min(1.0, right))  # Clamp to [-1, 1]
        right = None if math.isclose(right, 0.0) else right
        print(left, right)

        self.left_motor.set_throttle(left)
        self.right_motor.set_throttle(right)

    def close(self):
        self.left_motor.close()
        self.right_motor.close()


if __name__ == "__main__":
    print('test--')
    car = TwoWheelController()
    car.set_axis(0.5)
    sleep(3)

    
    # left_motor = Motor(22, 23, 19)
    # for val in [-0.5, -1]:
    #     left_motor.set_throttle(val)
    #     sleep(1)

    # # Set motor to stop mode.
    # left_motor.set_throttle(None)
    # left_motor.close()