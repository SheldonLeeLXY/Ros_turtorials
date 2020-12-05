#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from turtlesim.msg import Pose

def poseCallback(msg):
    rospy.loginfo("Turtle psoe: x:%0.6f, 7:%0.6f", msg.x, msg.y)

def pose_subscriber():
    rospy.init_node('pose_subscriber', anonymous = True)

    rospy.Subscriber("/turtle1/pose", Pose, poseCallback)

    rospy.spin()

if __name__ == '__main__':
    pose_subscriber()