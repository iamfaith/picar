from device import Motor
from time import sleep
from two_wheel import TwoWheelController


def test_controller(controller):
    for _ in range(2):
        controller.set_axis(x=-0.3)
        sleep(2)

        controller.set_axis(x=0.3)
        sleep(2)

        controller.set_axis()


if __name__ == "__main__":
    controller = TwoWheelController()
    test_controller(controller)
