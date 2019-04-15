#!/usr/bin/env python
import rospy
import csv
import ast
from bringup.msg import Goal
from turtlesim.msg import Pose  
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt 

class TurtleBot:

    def __init__(self):
	rospy.init_node('custom_listener', anonymous=True)
        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
        rospy.Subscriber("custom_chatter", Goal, self.callback)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback1)  
	#self.pose_subscriber = rospy.Subscriber("custom_chatter", Goal, self.update_pose)
	#self.pose = Goal()
	self.pose = Pose()  
        self.rate = rospy.Rate(1)
        rospy.spin()
	
    def callback1(self, data):  
        self.pose = data  
        self.pose.x = round(self.pose.x, 4)  
        self.pose.y = round(self.pose.y, 4)  

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
	theta =0
	x = data.pose.x
	y = data.pose.y
	goal_pose=Goal().pose
	gotogoal_x=0
	gotogoal_y=0
	gotogoal_x=x
	gotogoal_y=y
	
	#rospy.loginfo(gotogoal_x)
	#rospy.loginfo(gotogoal_y)
	 #j+= 1
	#print "Goal point Received :  id = " + str(id) + "  , x = " + str(x) + " , y = " + str(y)
	goals={}
	goals['x']=x
	goals['y']=y
	#print goals
	myData=[goals]
	with open('/home/tayssir/Desktop/goals_point.csv', 'a') as csvFile:
   	 writer = csv.writer(csvFile)
   	 writer.writerows([myData])
	 csvFile.close()

	goal_pose.x=gotogoal_x
	goal_pose.y=gotogoal_y

    def move2goal(self):  
        distance_tolerance = 0.2
        vel_msg = Twist()
        self.pose = Pose()
	goal_pose=Goal().pose
        results = []
	goal_x=[]
	goal_y=[]
	with open('/home/tayssir/Desktop/goals_point.csv') as File:
   	 reader = csv.reader(File)
    	 for row in reader:
	   results.append(row)
   	 #print results
	 for i in results: 
    	   for j in i :
            j = ast.literal_eval(j)
            for k in j:
              if 'x' == k : 
		goal_x.append(j.get(k))
              else :              
		goal_y.append(j.get(k))
	 #print goal_x
   	 #print goal_y
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
