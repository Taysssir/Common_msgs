#!/usr/bin/env python  
import yaml
import roslib
roslib.load_manifest("rosparam")
import rosparam
import rospy
import rospkg
from common_msgs.msg import Goal
from common_msgs.msg import Patrol

def Parser():
	j=0
	rospack = rospkg.RosPack()
	# get the file path for common_msgs
	#pkg=rospack.get_path('common_msgs')+'/config/'
	#with open(rospack.get_path('package_name')+'/config/patrol.yaml') 
	#print pkg
	print "Loading Yaml File :"
	print ""
	data = yaml.load(open(rospack.get_path('common_msgs')+'/config/patrol.yaml'))
	print data
	print ""
	print "================="
	print "Parsing Yaml File : "
	print "================="
	name= rospy.get_param('/name')
	print "name : "+ str(name) 
	#print "================="
	print ""
	duration_minutes= rospy.get_param('/duration_minutes')
	print "duration_minutes : "+ str(duration_minutes)
	#print "================="
	goals= rospy.get_param('/goals')
	#print "goals : "+ str(goals)
	#t = type(goals)
	#print t
	#i = len(goals) 
	#print i: 3 objects.
	pub = rospy.Publisher('custom_chatter', Goal, queue_size=10)
	rospy.init_node('custom_talker',anonymous=True)
	r = rospy.Rate(10) #10hz
	msg = Goal()
	for item in goals:
	   position = item['position']
	   id_string = item['id']
	   id = int (id_string)
	   #print "position # "+ str(position)
	   x =position['x']
	   y =position['y']
	   j+= 1
	   #v=type(id)
	   #print v
	   print "Goal point #"+ str(j) +"  id = " + str(id) + "  , x = " + str(x) + " y = " + str(y)
	   #print "x = "+ str(x)
	   #print "y = "+ str(y)
	   print "================="
	#p = type(position)
	#print p
        #print id
	   msg.id= id
	   msg.pose.x= x
	   msg.pose.y= y
	#while not rospy.is_shutdown():
	#rospy.loginfo(msg)
	   print msg
	   pub.publish(msg)
	   r.sleep()
	print "======================================================Talker==========================================================="


if __name__ == '__main__':
    try:
 #Testing our function  
        Parser()
        #talker()
    except rospy.ROSInterruptException: pass
