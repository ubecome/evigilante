#!/usr/bin/env python
import rospy
import csv

from bringup.msg import Goal
from bringup.msg import Patrol
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt

def listener():
	rospy.init_node('custom_listener', anonymous=True)
        rospy.Subscriber("custom_chatter", Goal, callback)
	pose = Goal()
        rospy.spin()

def callback(data):
        id = data.id
	x = data.pose.x
    	y = data.pose.y
	distance_tolerance = 0.2
	#list =[]
	#list_x =[]
	#list_y =[]
        vel_msg = Twist()
	pose = Goal()
	#print data
	#list_x.append(x)
	#print id ,x,y
	goals={}
	goals['x']=x
	goals['y']=y
	#print goals
	myData=[goals]
	print myData
	goal_pose=Goal().pose
	goal_pose.x=x
	goal_pose.y=y
	
	
	#a = open('/home/tayssir/Desktop/goals.txt', 'w+')
   	#a.write(str(int(id)))
	#data_to_save = str(data.pose.x) + "\t" + str(data.pose.y) + "\n"
	#a.write(data_to_save)

	with open('/home/tayssir/Desktop/goals_point.csv', 'a') as csvFile:
   	 writer = csv.writer(csvFile)
   	 writer.writerows([myData])
	 csvFile.close()

	
	#velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
	print goal_pose.x,goal_pose.y
	

	
        	
       

if __name__ == '__main__':
 print "======Start Listener==========="
listener()
