#!/usr/bin/env python
import rospy
from bringup.msg import Goal
from turtlesim.msg import Pose  
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt 


class TurtleBot:

    def __init__(self):
	rospy.init_node('custom_listener', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
        rospy.Subscriber("custom_chatter", Goal, self.callback)
        #self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback1)  
	#self.pose_subscriber = rospy.Subscriber("custom_chatter", Goal, self.update_pose)
	self.pose = Goal()  
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
	rospy.loginfo("Actual Pose")
	rospy.loginfo("===========")
	rospy.loginfo(self.pose.pose.x)
	rospy.loginfo(self.pose.pose.y)

	#print "Goal point Received :  id = " + str(id) + "  , x = " + str(x) + " , y = " + str(y)
	distance_tolerance = 0.2
        vel_msg = Twist()

	#self.pose.pose.x = round(self.pose.pose.x, 4)
        #self.pose.pose.y = round(self.pose.pose.y, 4)
        #self.pose = Pose()
	#pose_actual_x =gotogoal_x
	#pose_actual_y =gotogoal_y
  	#print pose_actual_x,pose_actual_y
	vel_msg.linear.x = 1.5 * sqrt(pow((gotogoal_x - self.pose.pose.x), 2) + pow((gotogoal_y - self.pose.pose.y), 2))  
	vel_msg.angular.z = 4 * (atan2(gotogoal_y - self.pose.pose.y, gotogoal_x - self.pose.pose.x) - theta)  
	#Publishing our vel_msg  
	self.velocity_publisher.publish(vel_msg)
	rospy.loginfo("Point atteint x= %s", gotogoal_x)
	rospy.loginfo("Point atteint y= %s", gotogoal_y)
	rospy.loginfo("===========")
	self.pose = data
	rospy.Rate(10)
       

if __name__ == '__main__':
    print "======Start Listener==========="
x = TurtleBot()
