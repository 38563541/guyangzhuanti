#!/usr/bin/env python

'''
REMIND: you should roslaunch some of the files before using this code.
This code can control MARS to go to a desired position.
First, you have to set rviz to make MARS realize its position in the room.
By moving MARS to the position and getting its coordinate from "rostopic echo /amcl_pose", then, setting the x, y, z, w to move to the place.  
'''

import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from move_base_msgs.msg import MoveBaseActionResult
from std_msgs.msg import Int8

mflag = False

def callback_move(data):
	global mflag
	mflag = True
	#print(data.status_list[0].status)
	#while data.status_list[0].status!=3 and data.status_list[0]!=4:
	#	rospy.sleep(2.)
	#	print('walking')
	#print(mflag.status_list[0].status)

def move():
	global mflag
    	# Starts a new node
    	rospy.init_node('plat_move', anonymous=True)
    	velocity_publisher = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=10)
    	moving = rospy.Subscriber('/move_base/result',MoveBaseActionResult, callback_move)
    	plat_status = rospy.Publisher('move_status',Int8,queue_size=10)
    	cmd = MoveBaseActionGoal()
    	#rate = rospy.Rate(0.0636) # 0.1hz

    	#Receiveing the user's input
    	print("Let's move your marslite.")
	
	while not rospy.is_shutdown():

        	rospy.sleep(2.)
        	raw_input("Press Enter to continue...")
        	print("room1")
		status = 1
        	cmd.goal.target_pose.header.frame_id = 'map'
        	cmd.goal.target_pose.pose.position.x = 5.536215497650227
        	cmd.goal.target_pose.pose.position.y = 0.08177573062447618
        	cmd.goal.target_pose.pose.orientation.z = 0.25496976673834454
        	cmd.goal.target_pose.pose.orientation.w = 0.9669490255692873
        	velocity_publisher.publish(cmd)
		plat_status.publish(status)
  	
		raw_input("Press Enter to continue...")
		print("room2")
		status = 1
        	cmd.goal.target_pose.header.frame_id = 'map'
        	cmd.goal.target_pose.pose.position.x = 7.449274231040084
        	cmd.goal.target_pose.pose.position.y = -3.0671396754121876
        	cmd.goal.target_pose.pose.orientation.z = 0.2602828412903526
        	cmd.goal.target_pose.pose.orientation.w = 0.9655324140233827
        	velocity_publisher.publish(cmd)
		plat_status.publish(status)

		raw_input("Press Enter to continue...")
		print("room3")
		status = 1
        	cmd.goal.target_pose.header.frame_id = 'map'
        	cmd.goal.target_pose.pose.position.x = 5.140580181718084
        	cmd.goal.target_pose.pose.position.y = -6.368348348425872
        	cmd.goal.target_pose.pose.orientation.z = -0.9545161233579879
        	cmd.goal.target_pose.pose.orientation.w = 0.2981593034765786
        	velocity_publisher.publish(cmd)
		plat_status.publish(status)

		raw_input("Press Enter to continue...")
		print("throw_garbage")
		status = 3
        	cmd.goal.target_pose.header.frame_id = 'map'
        	cmd.goal.target_pose.pose.position.x = 3.201936628334113
        	cmd.goal.target_pose.pose.position.y = -2.6811760434055087
        	cmd.goal.target_pose.pose.orientation.z = -0.9607036128284134  
        	cmd.goal.target_pose.pose.orientation.w = 0.2775762387136799
        	velocity_publisher.publish(cmd)
		plat_status.publish(status)
		rospy.sleep(5.)
		while not mflag:
			rospy.sleep(1.)
			print('walking')
		mflag = False
		#raw_input("Press Enter to continue...")
		#print(mflag.status_list)
		print("home")
		status = 4
		cmd.goal.target_pose.header.frame_id = 'map'
		cmd.goal.target_pose.pose.position.x = 2.6851784313357605
		cmd.goal.target_pose.pose.position.y = 1.336868505240544
		cmd.goal.target_pose.pose.orientation.z = -0.5026667969661016
		cmd.goal.target_pose.pose.orientation.w = 0.8644802433993735
		velocity_publisher.publish(cmd)
		plat_status.publish(status)

#################################################################

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
