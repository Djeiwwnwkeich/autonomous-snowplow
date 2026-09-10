import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
from std_msgs.msg import Int32

import serial


class SnowplowArduinoControl(Node):

    def __init__(self):
        super().__init__('snowplow_arduino_control')

        self.ser = serial.Serial(
            '/dev/ttyACM0',
            115200,
            timeout=1.0
        )

        self.create_subscription(
            Bool,
            '/snowplow/screw_enable',
            self.screw_callback,
            10
        )

        self.create_subscription(
            Int32,
            '/snowplow/chimney_angle',
            self.chimney_callback,
            10
        )

        self.create_subscription(
            Int32,
            '/snowplow/updown_angle',
            self.updown_callback,
            10
        )

        self.get_logger().info(
            'Snowplow Arduino control node started'
        )

    def send_command(self, command):
        self.ser.write(command.encode())

    def screw_callback(self, msg):
        if msg.data:
            self.send_command('1')
        else:
            self.send_command('0')

    def chimney_callback(self, msg):
        if msg.data > 0:
            self.send_command('d')
        elif msg.data < 0:
            self.send_command('a')
        else:
            self.send_command('c')

    def updown_callback(self, msg):
        if msg.data > 0:
            self.send_command('w')
        elif msg.data < 0:
            self.send_command('s')
        else:
            self.send_command('x')


def main(args=None):
    rclpy.init(args=args)

    node = SnowplowArduinoControl()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
