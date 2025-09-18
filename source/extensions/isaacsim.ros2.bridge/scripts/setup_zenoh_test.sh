#!/bin/bash
# Setup script for testing rmw_zenoh_cpp with Isaac Sim

echo "Setting up Zenoh RMW test environment..."

# Set ROS2 distribution
export ROS_DISTRO=humble

# Set RMW implementation to Zenoh
export RMW_IMPLEMENTATION=rmw_zenoh_cpp

# Add Isaac Sim ROS2 bridge libraries to LD_LIBRARY_PATH
ISAAC_SIM_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
BRIDGE_EXT_PATH="$ISAAC_SIM_ROOT/exts/isaacsim.ros2.bridge"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$BRIDGE_EXT_PATH/$ROS_DISTRO/lib"

echo "Environment variables set:"
echo "  ROS_DISTRO=$ROS_DISTRO"
echo "  RMW_IMPLEMENTATION=$RMW_IMPLEMENTATION"
echo "  LD_LIBRARY_PATH updated to include ROS2 bridge libraries"
echo ""

echo "To test the integration:"
echo "  1. Install rmw_zenoh_cpp: sudo apt install ros-humble-rmw-zenoh-cpp"
echo "  2. Start a Zenoh router: ros2 run rmw_zenoh_cpp rmw_zenohd"
echo "  3. Run the test: python $(dirname "${BASH_SOURCE[0]}")/../tests/test_zenoh_integration.py"
echo ""

echo "Press Enter to continue..."
read
