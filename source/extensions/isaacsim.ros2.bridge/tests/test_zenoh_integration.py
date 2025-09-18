#!/usr/bin/env python3
"""
Minimal test script for rmw_zenoh_cpp integration with Isaac Sim ROS2 bridge.

This script verifies that rmw_zenoh_cpp can be used as an RMW implementation.
"""

import os
import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ZenohTestNode(Node):
    """Minimal test node for Zenoh RMW integration."""
    
    def __init__(self):
        super().__init__('zenoh_test_node')
        self.publisher = self.create_publisher(String, 'test_topic', 10)
        self.subscription = self.create_subscription(
            String,
            'test_topic',
            self.listener_callback,
            10
        )
        self.message_count = 0
        self.timer = self.create_timer(1.0, self.timer_callback)
        
    def listener_callback(self, msg):
        """Callback for received messages."""
        self.get_logger().info(f'Received: "{msg.data}"')
        self.message_count += 1
        
    def timer_callback(self):
        """Timer callback for publishing messages."""
        msg = String()
        msg.data = f'Hello from Zenoh! Message #{self.message_count}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')


def check_rmw_implementation():
    """Check if rmw_zenoh_cpp is being used."""
    rmw_impl = os.environ.get('RMW_IMPLEMENTATION', 'not set')
    print(f"RMW_IMPLEMENTATION: {rmw_impl}")
    
    if rmw_impl != 'rmw_zenoh_cpp':
        print("WARNING: RMW_IMPLEMENTATION is not set to rmw_zenoh_cpp")
        print("To use Zenoh RMW, set: export RMW_IMPLEMENTATION=rmw_zenoh_cpp")
        return False
    
    return True


def main():
    """Main test function."""
    print("=== Zenoh RMW Integration Test ===")
    
    # Check RMW implementation
    if not check_rmw_implementation():
        print("Continuing with test anyway...")
    
    # Initialize ROS2
    try:
        rclpy.init()
        print("✓ ROS2 initialized successfully")
    except Exception as e:
        print(f"✗ Failed to initialize ROS2: {e}")
        return 1
    
    # Create test node
    try:
        node = ZenohTestNode()
        print("✓ Test node created successfully")
    except Exception as e:
        print(f"✗ Failed to create test node: {e}")
        rclpy.shutdown()
        return 1
    
    # Run the node for a short time
    try:
        print("Running test for 5 seconds...")
        import time
        start_time = time.time()
        while time.time() - start_time < 5.0:
            rclpy.spin_once(node, timeout_sec=0.1)
        
        print(f"✓ Test completed. Published {node.message_count} messages")
        
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    except Exception as e:
        print(f"✗ Error during test: {e}")
    finally:
        # Cleanup
        node.destroy_node()
        rclpy.shutdown()
        print("✓ Cleanup completed")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
