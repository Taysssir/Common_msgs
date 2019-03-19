#!/usr/bin/env python
import rospy
from common_msgs.msg import Goal
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt

def callback(data):
    id = data.id
    #gotogoal = data.pose
    x = data.pose.x
    y = data.pose.y
    gotogoal_x=0
    gotogoal_y=0
    gotogoal_x=x
    gotogoal_y=y
    print gotogoal_x,gotogoal_y
    #j+= 1
    print "Goal point Received :  id = " + str(id) + "  , x = " + str(x) + " , y = " + str(y)

def listener():
    rospy.init_node('custom_listener', anonymous=True)
    rospy.Subscriber("custom_chatter", Goal, callback)
    rospy.spin()

if __name__ == '__main__':
    print "======Start Listener==========="
    listener()
