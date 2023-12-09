#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from move_base_msgs.msg import MoveBaseActionResult
from std_msgs.msg import Int8
from geometry_msgs.msg import Twist

class plat_move:
	def __init__(self):
		self.mflag=False
		self.room=[]
		self.state=0
		rospy.init_node('plat_move', anonymous=True)
	    	self.velocity_publisher = rospy.Publisher('move_base/goal', MoveBaseActionGoal, queue_size=10)
            	moving = rospy.Subscriber('move_base/result', MoveBaseActionResult, self.callback_move)
    	    	plat_status = rospy.Subscriber('project/state', Int8, self.callback_status)
    	    	self.change_state = rospy.Publisher('project/change_state_request', Int8, queue_size=10)
    	    	go_to_room = rospy.Subscriber('project/line_call', Int8, self.callback_line)
    	    	self.velocity_publisher2 = rospy.Publisher('/mob_plat/cmd_vel', Twist, queue_size=10)
    	    	self.vel_msg = Twist()
    	    	self.cmd = MoveBaseActionGoal()
    	    	self.location1=[5.017923645695738, -0.11096243663423073, 0.28203642527562656, 0.9594036975214062]
    	    	self.location2=[6.995364869708911, -3.3122447811354037, 0.23258927429373988, 0.9725750508230773]
    	    	self.location3=[6.136289233132765, -5.554411782150698, -0.9638450346837353, 0.26646341046287975]
    	    	self.location4=[3.4576214175130433, -2.0638430836043584, -0.9567393195300613, 0.2909465147843417]
    	    	self.home=[2.82377151622645337, 1.4346376179967024, -0.5195518968672604, 0.8544388956863045]
    	    	self.goal=[self.location1, self.location2, self.location3, self.location4, self.home]
    	    	self.cur_goal=-1
    	    	self.speed = 0.1
    	    	self.distance = 1.2
    	    	self.vel_msg.linear.y = 0
	       	self.vel_msg.linear.z = 0
        	self.vel_msg.angular.x = 0
        	self.vel_msg.angular.y = 0
        	self.vel_msg.angular.z = 0
    	    	
	def callback_move(self,data):
		#print(data.status.status)
		if data.status.status == 3:
			self.mflag = True
		else:
			self.cmd.goal.target_pose.header.frame_id = 'map'
	    		self.cmd.goal.target_pose.pose.position.x = self.goal[self.cur_goal][0]
	   		self.cmd.goal.target_pose.pose.position.y = self.goal[self.cur_goal][1]
	    		self.cmd.goal.target_pose.pose.orientation.z = self.goal[self.cur_goal][2]
	    		self.cmd.goal.target_pose.pose.orientation.w = self.goal[self.cur_goal][3]
	    		self.velocity_publisher.publish(self.cmd)
				
	def callback_status(self,msg):
		self.state = msg.data
		#print("status:",msg.data)
	
	def callback_line(self,msg):
		self.room.append(msg.data)
		#print("line:",msg.data)
		#print(len(self.room))
	
	def move(self):
	    	# Starts a new node
	    	
    	    	first_time = True
    	    
    	    	while not rospy.is_shutdown():
	
			rospy.sleep(2.)
    			if first_time:
				'''print("room1")
				self.cur_goal=0
	    			self.cmd.goal.target_pose.header.frame_id = 'map'
	    			self.cmd.goal.target_pose.pose.position.x = self.location1[0]
	   			self.cmd.goal.target_pose.pose.position.y = self.location1[1]
	    			self.cmd.goal.target_pose.pose.orientation.z = self.location1[2]
	    			self.cmd.goal.target_pose.pose.orientation.w = self.location1[3]
	    			self.velocity_publisher.publish(self.cmd)
	    			while not self.mflag:
				    	rospy.sleep(1.)
				    	print('walking')
    				self.mflag = False
    		   		print("room2")
	    			self.cur_goal=1
	        		self.cmd.goal.target_pose.header.frame_id = 'map'
	        		self.cmd.goal.target_pose.pose.position.x = self.location2[0]
	   			self.cmd.goal.target_pose.pose.position.y = self.location2[1]
	    			self.cmd.goal.target_pose.pose.orientation.z = self.location2[2]
	    			self.cmd.goal.target_pose.pose.orientation.w = self.location2[3]
		       		self.velocity_publisher.publish(self.cmd)
				while not self.mflag:
					rospy.sleep(1.)
					print('walking')
				self.mflag = False
				print("room3")
				self.cur_goal=2
    				self.cmd.goal.target_pose.header.frame_id = 'map'
        			self.cmd.goal.target_pose.pose.position.x = self.location3[0]
	   			self.cmd.goal.target_pose.pose.position.y = self.location3[1]
	    			self.cmd.goal.target_pose.pose.orientation.z = self.location3[2]
	    			self.cmd.goal.target_pose.pose.orientation.w = self.location3[3]
			       	self.velocity_publisher.publish(self.cmd)
				while not self.mflag:
					rospy.sleep(1.)
					print('walking')
				self.mflag = False
				print("throw_garbage")
				self.cur_goal=3
    				self.cmd.goal.target_pose.header.frame_id = 'map'
       				self.cmd.goal.target_pose.pose.position.x = self.location4[0]
	   			self.cmd.goal.target_pose.pose.position.y = self.location4[1]
	    			self.cmd.goal.target_pose.pose.orientation.z = self.location4[2]
	    			self.cmd.goal.target_pose.pose.orientation.w = self.location4[3]
       				self.velocity_publisher.publish(self.cmd)
       				while not self.mflag:
		    			rospy.sleep(1.)
					print('walking')'''
				self.mflag = False	
        			print("home")
        			self.cur_goal=4
				self.cmd.goal.target_pose.header.frame_id = 'map'
				self.cmd.goal.target_pose.pose.position.x = self.home[0]
	   			self.cmd.goal.target_pose.pose.position.y = self.home[1]
	    			self.cmd.goal.target_pose.pose.orientation.z = self.home[2]
	    			self.cmd.goal.target_pose.pose.orientation.w = self.home[3]
				self.velocity_publisher.publish(self.cmd)
				while not self.mflag:
					rospy.sleep(1.)
					print('walking')
				self.mflag = False
				print("arrive")
				first_time = False
				self.change_state.publish(0)
				rospy.sleep(2.)	
			else:
				#print("here",self.state)
				if self.state == 0:
					#print("inside",len(self.room))
					if len(self.room) != 0:
						which_room = self.room[0]
						self.room.pop(0)
						self.change_state.publish(1)
						rospy.sleep(2.)
				elif self.state == 1:
					if which_room == 1:
						self.cur_goal=0
	    					self.cmd.goal.target_pose.header.frame_id = 'map'
	    					self.cmd.goal.target_pose.pose.position.x = self.location1[0]
	   					self.cmd.goal.target_pose.pose.position.y = self.location1[1]
	    					self.cmd.goal.target_pose.pose.orientation.z = self.location1[2]
	    					self.cmd.goal.target_pose.pose.orientation.w = self.location1[3]
	    					self.velocity_publisher.publish(self.cmd)
					elif which_room == 2:
						self.cur_goal=1
	    					self.cmd.goal.target_pose.header.frame_id = 'map'
	    					self.cmd.goal.target_pose.pose.position.x = self.location2[0]
	   					self.cmd.goal.target_pose.pose.position.y = self.location2[1]
	    					self.cmd.goal.target_pose.pose.orientation.z = self.location2[2]
	    					self.cmd.goal.target_pose.pose.orientation.w = self.location2[3]
	    					self.velocity_publisher.publish(self.cmd)
					elif which_room == 3:
						self.cur_goal=2
	    					self.cmd.goal.target_pose.header.frame_id = 'map'
	    					self.cmd.goal.target_pose.pose.position.x = self.location3[0]
	   					self.cmd.goal.target_pose.pose.position.y = self.location3[1]
	    					self.cmd.goal.target_pose.pose.orientation.z = self.location3[2]
	    					self.cmd.goal.target_pose.pose.orientation.w = self.location3[3]
	    					self.velocity_publisher.publish(self.cmd)
		    			while not self.mflag:
						rospy.sleep(1.)
						print('walking')
					self.mflag = False
					t0 = rospy.Time.now().to_sec()
        				current_distance = 0
        				self.vel_msg.linear.x = abs(self.speed)
        				while(current_distance < self.distance):
            					self.velocity_publisher2.publish(self.vel_msg)
            					t1=rospy.Time.now().to_sec()
            					current_distance= self.speed*(t1-t0)
            				self.vel_msg.linear.x = 0
        				self.velocity_publisher2.publish(self.vel_msg)
					print("arrive")
		  			self.change_state.publish(2)
		  			rospy.sleep(2.)
				elif self.state == 4:
					self.cur_goal=3
	    				self.cmd.goal.target_pose.header.frame_id = 'map'
	    				self.cmd.goal.target_pose.pose.position.x = self.location4[0]
	   				self.cmd.goal.target_pose.pose.position.y = self.location4[1]
	    				self.cmd.goal.target_pose.pose.orientation.z = self.location4[2]
	    				self.cmd.goal.target_pose.pose.orientation.w = self.location4[3]
	    				self.velocity_publisher.publish(self.cmd)
			        	while not self.mflag:
						rospy.sleep(1.)
						print('walking')
					self.mflag = False
					print("arrive")
			  		self.change_state.publish(5)
					rospy.sleep(2.)
				elif self.state == 6:
					if len(self.room) == 0: 
						self.cur_goal=4
	    					self.cmd.goal.target_pose.header.frame_id = 'map'
	    					self.cmd.goal.target_pose.pose.position.x = self.home[0]
	   					self.cmd.goal.target_pose.pose.position.y = self.home[1]
	    					self.cmd.goal.target_pose.pose.orientation.z = self.home[2]
	    					self.cmd.goal.target_pose.pose.orientation.w = self.home[3]
	    					self.velocity_publisher.publish(self.cmd)
			        		while not self.mflag:
							rospy.sleep(1.)
							print('walking')
						self.mflag = False
						print("arrive")
						self.change_state.publish(0)
						rospy.sleep(2.)
					else:
						which_room = self.room[0]
						self.room.pop(0)
						self.change_state.publish(1)
						rospy.sleep(2.)
               	    
#################################################################

if __name__ == '__main__':
    try:
        #Testing our function
        rob = plat_move()
        rob.move()
    except rospy.ROSInterruptException: pass
