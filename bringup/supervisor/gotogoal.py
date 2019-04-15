#!/usr/bin/env python
import rospy
import csv
import ast
from bringup.msg import Goal
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt 

class TurtleBot:

    def __init__(self):

	rospy.init_node('custom_listener', anonymous=True)
        rospy.Subscriber("custom_chatter", Goal, self.callback)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
	self.pose = Goal()
        self.rate = rospy.Rate(1)
        rospy.spin()
	
    def get_distance(self, goal_x, goal_y):  
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))  
        return distance 


    def callback(self,data):
        self.id = data.id
	self.x = data.pose.x
	self.y = data.pose.y
	self.x = round(self.x, 4)  
        self.y = round(self.y, 4)
	goals={}
	goals['x']=self.x
	goals['y']=self.y
	myData=[goals]
	print myData
	goal_pose=Goal().pose
	goal_pose.x=self.x
	goal_pose.y=self.y
	self.theta=0
	with open('/home/tayssir/Desktop/goals_point.csv', 'a') as csvFile:
   	 writer = csv.writer(csvFile)
   	 writer.writerows([myData])
	 csvFile.close()
	print goal_pose.x,goal_pose.y

    def move2goal(self):  
	distance_tolerance = 0.2
        vel_msg = Twist() 
	results = []
	goal_x=[]
	goal_y=[]
	goal_pose = Goal().pose
	distance_tolerance = 0.2
        vel_msg = Twist()
	#print self.x 
	with open('/home/tayssir/Desktop/goals_point.csv') as File:
   	 reader = csv.reader(File)
   	 for row in reader: 
       	  results.append(row)
   	 print results
   	 for i in results: 
    	   for j in i :
            j = ast.literal_eval(j)
            for k in j:
              if 'x' == k : 
		goal_x.append(j.get(k))
              else :              
		goal_y.append(j.get(k))
   	 print goal_x
   	 print goal_y
	 v = len(goal_x) - 1 
	 for i in range(len(goal_x)):
	  print "Goal point #"+ str(i+1) + "  : x = " + str(goal_x[i]) + " y = " + str(goal_y[i])
          goal_pose.x = goal_x[i]
          goal_pose.y = goal_y[i]
	  #if (i == v) :
	 	#print "Finish Patrol_Turtle"
	  print "================="
	  print goal_pose.x
	  print goal_pose.y

	
       

if __name__ == '__main__':
    print "======Start Listener==========="
    try:  
        #Testing our function  
        x = TurtleBot()  
        x.move2goal()  
  
    except rospy.ROSInterruptException: 
	pass
