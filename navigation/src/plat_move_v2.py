#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from move_base_msgs.msg import MoveBaseActionResult
from std_msgs.msg import Int8

def callback_move(data):
	global	mflag
	mflag = True
	#while data.status_list[0].status !=3 and data.status_list[0].status !=4:
	#	rospy.sleep(2.)
	#	print("walking")
	#	if status == 4 and room != 0:
	#		status = 1
	#		plat_status.publish(status)
	#		break
		
def callback_status(msg):
	global state
	state = msg.data
	
def callback_line(msg):
	global	room
	room.append(msg.data)
	
def move():
    global mflag,state,room
    room = []
    # Starts a new node
    rospy.init_node('plat_move', anonymous=True)
    velocity_publisher = rospy.Publisher('move_base/goal', MoveBaseActionGoal, queue_size=10)
    moving = rospy.Subscriber('move_base/result', MoveBaseActionResult, callback_move)
    plat_status = rospy.Subscriber('project/state', Int8, callback_status)
    change_state = rospy.Publisher('project/change_state_request', Int8, queue_size=10)
    go_to_room = rospy.Subscriber('project/line_call', Int8, callback_line)
    cmd = MoveBaseActionGoal()
    
    mflag = False
    first_time = True

    while not rospy.is_shutdown():
	
	rospy.sleep(2.)
    	if first_time:
		print("room1")
	    	cmd.goal.target_pose.header.frame_id = 'map'
	    	cmd.goal.target_pose.pose.position.x = 5.536215497650227
	   	cmd.goal.target_pose.pose.position.y = 0.08177573062447618
	    	cmd.goal.target_pose.pose.orientation.z = 0.25496976673834454
	    	cmd.goal.target_pose.pose.orientation.w = 0.9669490255692873
	    	velocity_publisher.publish(cmd)
	    	while not mflag:
		    	rospy.sleep(1.)
		    	print('walking')
    		mflag = False
	    	print("room2")
	        cmd.goal.target_pose.header.frame_id = 'map'
	        cmd.goal.target_pose.pose.position.x = 7.449274231040084
	        cmd.goal.target_pose.pose.position.y = -3.0671396754121876
	       	cmd.goal.target_pose.pose.orientation.z = 0.2602828412903526
	       	cmd.goal.target_pose.pose.orientation.w = 0.9655324140233827
	       	velocity_publisher.publish(cmd)
		while not mflag:
			rospy.sleep(1.)
			print('walking')
		mflag = False
		print("room3")
    		cmd.goal.target_pose.header.frame_id = 'map'
        	cmd.goal.target_pose.pose.position.x = 5.140580181718084
     		cmd.goal.target_pose.pose.position.y = -6.368348348425872
    		cmd.goal.target_pose.pose.orientation.z = -0.9545161233579879
	       	cmd.goal.target_pose.pose.orientation.w = 0.2981593034765786
	       	velocity_publisher.publish(cmd)
		while not mflag:
			rospy.sleep(1.)
			print('walking')
		mflag = False
		print("throw_garbage")
    		cmd.goal.target_pose.header.frame_id = 'map'
       		cmd.goal.target_pose.pose.position.x = 3.201936628334113
       		cmd.goal.target_pose.pose.position.y = -2.6811760434055087
       		cmd.goal.target_pose.pose.orientation.z = -0.9607036128284134  
       		cmd.goal.target_pose.pose.orientation.w = 0.2775762387136799
       		velocity_publisher.publish(cmd)
       		while not mflag:
	    		rospy.sleep(1.)
			print('walking')
		mflag = False	
        	print("home")
		cmd.goal.target_pose.header.frame_id = 'map'
		cmd.goal.target_pose.pose.position.x = 2.82377151622645337
		cmd.goal.target_pose.pose.position.y = 1.4346376179967024
		cmd.goal.target_pose.pose.orientation.z = -0.5195518968672604
		cmd.goal.target_pose.pose.orientation.w = 0.8544388956863045
		velocity_publisher.publish(cmd)
		while not mflag:
			rospy.sleep(1.)
			print('walking')
		mflag = False
		first_time = False	
	else:
		if state == 0:
			if len(room) != 0:
				which_room = room[0]
				room.pop(0)
				change_state.publish(1)
				rospy.sleep(1.)
		elif state == 1:
			if which_room == 1:
				cmd.goal.target_pose.header.frame_id = 'map'
	   			cmd.goal.target_pose.pose.position.x = 5.536215497650227
	    	   		cmd.goal.target_pose.pose.position.y = 0.08177573062447618
	    	   		cmd.goal.target_pose.pose.orientation.z = 0.25496976673834454
	    	   		cmd.goal.target_pose.pose.orientation.w = 0.9669490255692873
	    	   		velocity_publisher.publish(cmd)
			elif which_room == 2:
				cmd.goal.target_pose.header.frame_id = 'map'
        			cmd.goal.target_pose.pose.position.x = 7.449274231040084
	    			cmd.goal.target_pose.pose.position.y = -3.0671396754121876
	    	   		cmd.goal.target_pose.pose.orientation.z = 0.2602828412903526
	    	   		cmd.goal.target_pose.pose.orientation.w = 0.9655324140233827
	      			velocity_publisher.publish(cmd)
			elif which_room == 3:
				cmd.goal.target_pose.header.frame_id = 'map'
        			cmd.goal.target_pose.pose.position.x = 5.140580181718084
        			cmd.goal.target_pose.pose.position.y = -6.368348348425872
        			cmd.goal.target_pose.pose.orientation.z = -0.9545161233579879
        			cmd.goal.target_pose.pose.orientation.w = 0.2981593034765786
        			velocity_publisher.publish(cmd)
	    		while not mflag:
				rospy.sleep(1.)
				print('walking')
			mflag = False
	  		change_state.publish(2)
	  		rospy.sleep(1.)
		elif state == 4:
			cmd.goal.target_pose.header.frame_id = 'map'
	        	cmd.goal.target_pose.pose.position.x = 3.201936628334113
	        	cmd.goal.target_pose.pose.position.y = -2.6811760434055087
	        	cmd.goal.target_pose.pose.orientation.z = -0.9607036128284134  
	        	cmd.goal.target_pose.pose.orientation.w = 0.2775762387136799
	        	velocity_publisher.publish(cmd)
	        	while not mflag:
				rospy.sleep(1.)
				print('walking')
			mflag = False
	  		change_state.publish(5)
			rospy.sleep(1.)
		elif state == 6:
			if len(room) == 0: 
				print("home")
				cmd.goal.target_pose.header.frame_id = 'map'
				cmd.goal.target_pose.pose.position.x = 2.82377151622645337
				cmd.goal.target_pose.pose.position.y = 1.4346376179967024
				cmd.goal.target_pose.pose.orientation.z = -0.5195518968672604
				cmd.goal.target_pose.pose.orientation.w = 0.8544388956863045
				velocity_publisher.publish(cmd)
	        		while not mflag:
					rospy.sleep(1.)
					print('walking')
				mflag = False
				change_state.publish(0)
				rospy.sleep(1.)
			else:
				which_room = room[0]
				room.pop(0)
				change_state.publish(1)
				rospy.sleep(1.)
                   
#################################################################

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
