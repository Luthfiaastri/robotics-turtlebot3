import time
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from std_msgs.msg import Float32


class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.declare_parameter('reliability', 'reliable')
        self.declare_parameter('depth', 10)

        rel_str = self.get_parameter('reliability').value
        depth = self.get_parameter('depth').value
        rel = (ReliabilityPolicy.RELIABLE if rel_str == 'reliable'
               else ReliabilityPolicy.BEST_EFFORT)

        qos = QoSProfile(depth=depth, reliability=rel,
                          history=HistoryPolicy.KEEP_LAST)

        self.count = 0
        self.start_time = time.time()
        self.sub = self.create_subscription(
            Float32, 'sensor_data', self.on_data, qos)

        self.report_timer = self.create_timer(10.0, self.report)

        self.get_logger().info(
            f'subscribing with qos={rel.name}, depth={depth}')

    def on_data(self, msg):
        self.count += 1

    def report(self):
        elapsed = time.time() - self.start_time
        self.get_logger().info(
            f'[t={elapsed:.0f}s] pesan diterima: {self.count}')


def main():
    rclpy.init()
    node = SensorSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        elapsed = time.time() - node.start_time
        node.get_logger().info(
            f'TOTAL AKHIR: {node.count} pesan diterima dalam {elapsed:.1f} detik')
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
