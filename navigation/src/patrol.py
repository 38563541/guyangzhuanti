#!/usr/bin/env python

'''
REMIND: you should roslaunch some of the files before using this code.
This code can control MARS to go to a desired position.
First, you have to set rviz to make MARS realize its position in the room.
By moving MARS to the position and getting its coordinate from "rostopic echo /amcl_pose", then, setting the x, y, z, w to move to the place.  
'''

import rospy
from move_base_msgs.msg import MoveBaseActionGoal

def move():

    # Starts a new node
    rospy.init_node('plat_move', anonymous=True)
    velocity_publisher = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=10)

    cmd = MoveBaseActionGoal()
    #rate = rospy.Rate(0.0636) # 0.1hz

    #Receiveing the user's input
    print("Let's move your marslite.")

    while not rospy.is_shutdown():

        rospy.sleep(2.)
        raw_input("Press Enter to continue...")
        print("room1")
	cmd.goal.target_pose.header.frame_id = 'map'
	cmd.goal.target_pose.pose.position.x = 5.536215497650227
	cmd.goal.target_pose.pose.position.y = 0.08177573062447618
	cmd.goal.target_pose.pose.orientation.z = 0.25496976673834454
	cmd.goal.target_pose.pose.orientation.w = 0.9669490255692873
	velocity_publisher.publish(cmd)
        raw_input("Press Enter to continue...")

	print("room2")
        cmd.goal.target_pose.header.frame_id = 'map'
        cmd.goal.target_pose.pose.position.x = 7.449274231040084
        cmd.goal.target_pose.pose.position.y = -3.0671396754121876
       	cmd.goal.target_pose.pose.orientation.z = 0.2602828412903526
       	cmd.goal.target_pose.pose.orientation.w = 0.9655324140233827
       	velocity_publisher.publish(cmd)
 	raw_input("Press Enter to continue...")
	
	print("room3")
    	cmd.goal.target_pose.header.frame_id = 'map'
       	cmd.goal.target_pose.pose.position.x = 5.140580181718084
     	cmd.goal.target_pose.pose.position.y = -6.368348348425872
    	cmd.goal.target_pose.pose.orientation.z = -0.9545161233579879
       	cmd.goal.target_pose.pose.orientation.w = 0.2981593034765786
       	velocity_publisher.publish(cmd)
        raw_input("Press Enter to continue...")

	'''print("throw_garbage")
    	cmd.goal.target_pose.header.frame_id = 'map'
      	cmd.goal.target_pose.pose.position.x = 3.201936628334113
      	cmd.goal.target_pose.pose.position.y = -2.6811760434055087
       	cmd.goal.target_pose.pose.orientation.z = -0.9607036128284134  
       	cmd.goal.target_pose.pose.orientation.w = 0.2775762387136799
       	velocity_publisher.publish(cmd)
        raw_input("Press Enter to continue...")'''
        print("throw_garbage")
    	cmd.goal.target_pose.header.frame_id = 'map'
      	cmd.goal.target_pose.pose.position.x = 2.5863936013427993
      	cmd.goal.target_pose.pose.position.y = -1.9713277411105223
       	cmd.goal.target_pose.pose.orientation.z = -0.9849364948973641  
       	cmd.goal.target_pose.pose.orientation.w = 0.1729164567624914
       	velocity_publisher.publish(cmd)
        raw_input("Press Enter to continue...")
        
        print("home")
	cmd.goal.target_pose.header.frame_id = 'map'
	cmd.goal.target_pose.pose.position.x = 2.82377151622645337
	cmd.goal.target_pose.pose.position.y = 1.4346376179967024
	cmd.goal.target_pose.pose.orientation.z = -0.5195518968672604
	cmd.goal.target_pose.pose.orientation.w = 0.8544388956863045
	velocity_publisher.publish(cmd)
	raw_input("Press Enter to continue...")

#################################################################

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
