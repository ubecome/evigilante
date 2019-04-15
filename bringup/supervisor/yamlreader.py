#!/usr/bin/env python  
import yaml
import roslib
roslib.load_manifest("rosparam")
import rosparam
import rospy
import rospkg
from bringup.msg import Goal
from bringup.msg import Patrol

def Parser():
	j=0
	rospack = rospkg.RosPack()
	# get the file path for common_msgs
	#pkg=rospack.get_path('common_msgs')+'/config/'
	#with open(rospack.get_path('package_name')+'/config/patrol.yaml') 
	#print pkg
	print "Loading Yaml File :"
	print ""
	data = yaml.load(open(rospack.get_path('bringup')+'/config/patrol.yaml'))
	#print data
	#print ""
	#print "================="
	#print "Parsing Yaml File : "
	#print "================="
	name= rospy.get_param('/name')
	#print "name : "+ str(name) 
	#print "================="
	#print ""
	duration_minutes= rospy.get_param('/duration_minutes')
	#print "duration_minutes : "+ str(duration_minutes)
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
	msg = Patrol()
	goal=Goal()
	list_goal=msg.patrol
	#t=type(list_goal)
	#print t
	list_id =[]
	list_x =[]
	list_y =[]

	for item in goals:
	   position = item['position']
	   id_string = item['id']
	   id = int (id_string)
	   #print "position # "+ str(position)
	   x =position['x']
	   y =position['y']
	   #goal.id=id
	   #goal.pose.x=x
	   #goal.pose.y=y
	   list_id.append(id)
	   list_x.append(x)
	   list_y.append(y)
	   #print x , y
	   #print "goal"
	   #print goal
	   
	   #list_goal.append(goal)
	   #for i in range(id) :
	      #print goal
	   #pub.publish(goal)

	   #list_goal.append(goal)
	   #print list_goal
	   
	
	#print list_id
	#print list_x
	#print list_y
	for i in list_id:
	 goal.id=list_id[i]
	 goal.pose.x=list_x[i]
	 goal.pose.y=list_y[i]
	 #print goal.pose.x,goal.pose.y
	 print goal
	 list_goal.insert(i+1,goal)
	 #print list_goal
	 #while not rospy.is_shutdown():
	 pub.publish(goal)
	 #r = rospy.Rate(10) #10hz
	   #r.sleep()

	#goal.id=list_id
	#goal.pose.x=x
	#goal.pose.y=y

	#pub.publish(list_x)
	#pub.publish(list_y)
	#print goal
	#list_goal.append(goal)
	#print list_goal
	#while not rospy.is_shutdown():
	#rospy.loginfo(msg)
	#print msg

	#pub.publish(list_goal)
	#r.sleep()

	print "==============================Finish================================="


if __name__ == '__main__':
    try:
 #Testing our function  
        Parser()
        #talker()
    except rospy.ROSInterruptException: pass
