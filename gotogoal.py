#!/usr/bin/env python
import rospy
from common_msgs.msg import Goal
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt 

class TurtleBot:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
	rospy.init_node('custom_listener', anonymous=True)
        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called when a message of type Pose is received.
        rospy.Subscriber("custom_chatter", Goal, self.callback)
	self.pose_subscriber = rospy.Subscriber("custom_chatter", Goal, self.update_pose)
	self.pose = Goal()
        self.rate = rospy.Rate(1)
        rospy.spin()
	#self.pose = Goal.pose()
        #self.pose = Goal()

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.pose.x = round(self.pose.pose.x, 4)
        self.pose.pose.y = round(self.pose.pose.y, 4)

    def get_distance(self, goal_x, goal_y):  
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))  
        return distance 


    def callback(self,data):
        id = data.id
    	#gotogoal = data.pose
	theta =0
	x = data.pose.x
	y = data.pose.y
	goal_pose=Goal().pose
	gotogoal_x=0
	gotogoal_y=0
	gotogoal_x=x
	gotogoal_y=y
	print goal_pose.x
	print gotogoal_x,gotogoal_y
	 #j+= 1
	print "Goal point Received :  id = " + str(id) + "  , x = " + str(x) + " , y = " + str(y)
	goal_pose.x=gotogoal_x
	goal_pose.y=gotogoal_y
	print goal_pose.x,goal_pose.y
# Please, insert a number slightly greater than 0 (e.g. 0.01).
        distance_tolerance = 0.2
        vel_msg = Twist()
	self.pose = Goal()
	while sqrt(pow((goal_pose.x - self.pose.pose.x), 2) + pow((goal_pose.y - self.pose.pose.y), 2)) >= distance_tolerance:  
	#Porportional Controller  
		    #linear velocity in the x-axis:  
		    vel_msg.linear.x = 1.5 * sqrt(pow((goal_pose.x - self.pose.pose.x), 2) + pow((goal_pose.y - self.pose.pose.y), 2))  
		    vel_msg.linear.y = 0  
		    vel_msg.linear.z = 0  
  
		    #angular velocity in the z-axis:  
		    vel_msg.angular.x = 0  
		    vel_msg.angular.y = 0  
		    vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.pose.y, goal_pose.x - self.pose.pose.x) - self.pose.pose.theta)  
	  
		    #Publishing our vel_msg  
		    self.velocity_publisher.publish(vel_msg)
  		    #print "="
		    
	#Stopping our robot after the movement is over  
	vel_msg.linear.x = 0  
	vel_msg.angular.z =0  
	self.velocity_publisher.publish(vel_msg)
	rospy.spin()  
       

if __name__ == '__main__':
    print "======Start Listener==========="
    x = TurtleBot()
