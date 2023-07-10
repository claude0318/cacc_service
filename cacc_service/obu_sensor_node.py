import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class OBUSensor(Node):

    def __init__(self):
        super().__init__('obu_sensor')
        self.publisher_ = self.create_publisher(String, 'acceleration_topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Desired Acceleration: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing random data: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    obu_sensor = OBUSensor()

    rclpy.spin(obu_sensor)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    obu_sensor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()