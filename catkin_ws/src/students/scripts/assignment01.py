#!/usr/bin/env python3
#


import rospy
from sensor_msgs.msg   import LaserScan
from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped

NAME = "FULL NAME"

def callback_movement_detected(msg):
    global movement_detected
    movement_detected = msg.data
    return

def main():
    print("ASSIGNMENT 01 - " + NAME)
    rospy.init_node("assignment01")
    rospy.Subscriber("/movement_detected", Bool, callback_movement_detected)
    pub_goal_pose = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)
    loop = rospy.Rate(10)
    
    global movement_detected
    movement_detected = False

    goal = PoseStamped()
    goal.pose.position.x = 0
    goal.pose.position.y = 0
    while not rospy.is_shutdown():
        if movement_detected:
            movement_detected = False;
            pub_goal_pose.publish(goal)
        loop.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    
