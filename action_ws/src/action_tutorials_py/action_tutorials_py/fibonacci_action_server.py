import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import time

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionServer(Node):

    def __init__(self, no_feedback = False):
        super().__init__('fibonacci_action_server')
        self._NO_FEEDBACK = no_feedback
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        result = Fibonacci.Result()

        # define without feedback
        if self._NO_FEEDBACK:
            sequence = [0, 1]
            for i in range(1, goal_handle.request.order):
                sequence.append(sequence[i] + sequence[i-1])
            result.sequence = sequence
        else:
            feedback_msg = Fibonacci.Feedback()
            feedback_msg.partial_sequence = [0, 1]
            for i in range(1, goal_handle.request.order):
                feedback_msg.partial_sequence.append(
                    feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
                self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(1)
            result.sequence = feedback_msg.partial_sequence

        goal_handle.succeed()

        return result


def main(args=None):
    rclpy.init(args=args)

    fibonacci_action_server = FibonacciActionServer()

    rclpy.spin(fibonacci_action_server)


if __name__ == '__main__':
    main()
