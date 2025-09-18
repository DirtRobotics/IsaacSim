@echo off
REM Setup script for testing rmw_zenoh_cpp with Isaac Sim

echo Setting up Zenoh RMW test environment...

REM Set ROS2 distribution
set ROS_DISTRO=humble

REM Set RMW implementation to Zenoh
set RMW_IMPLEMENTATION=rmw_zenoh_cpp

REM Add Isaac Sim ROS2 bridge libraries to PATH
set ISAAC_SIM_ROOT=%~dp0..\..\..\..
set BRIDGE_EXT_PATH=%ISAAC_SIM_ROOT%\exts\isaacsim.ros2.bridge
set PATH=%PATH%;%BRIDGE_EXT_PATH%\%ROS_DISTRO%\lib

echo Environment variables set:
echo   ROS_DISTRO=%ROS_DISTRO%
echo   RMW_IMPLEMENTATION=%RMW_IMPLEMENTATION%
echo   PATH updated to include ROS2 bridge libraries
echo.

echo To test the integration:
echo   1. Install rmw_zenoh_cpp: sudo apt install ros-humble-rmw-zenoh-cpp
echo   2. Start a Zenoh router: ros2 run rmw_zenoh_cpp rmw_zenohd
echo   3. Run the test: python %~dp0..\tests\test_zenoh_integration.py
echo.

echo Press any key to continue...
pause >nul
