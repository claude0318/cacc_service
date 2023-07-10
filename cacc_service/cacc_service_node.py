import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .cacc import CACC

class CACC_Service(Node):

    def __init__(self):
        super().__init__('cacc_service')
        self.declare_parameter('my_parameter', 'set value')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        # subscribe to data published by a obu sensor node
        self.subscription = self.create_subscription(String,'acceleration_topic', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def timer_callback(self):
        msg = String()
        msg.data = 'Data: %d' % self.i
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing output: "%s"' % msg.data)
        self.get_logger().info(CACC.output_msg() + msg.data)
        self.i += 1

        my_new_param = rclpy.parameter.Parameter(
            'my_parameter',
            rclpy.Parameter.Type.STRING,
            'world'
        )
        all_new_parameters = [my_new_param]
        self.set_parameters(all_new_parameters)

    # here we would run computations from CACC.py
    def listener_callback(self, msg):
        self.get_logger().info('I catched from OBU: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    cacc_service = CACC_Service()

    rclpy.spin(cacc_service)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    cacc_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()