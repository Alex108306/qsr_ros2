import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from custom_package import mem

class MyNode(Node):
    def __init__(self):
        super().__init__('test_node')
        mem.func()

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()