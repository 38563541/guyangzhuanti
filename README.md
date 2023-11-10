# guyangzhuanti

##run goods detection and grasp

// in marslite kyy  
>bringup  
// in catkin_ws  
>roslaunch depthimage_to_laserscan realsense_all_edited.launch   
// in scanner_py3_ws  
>source docker_run.sh cuda10  
>roslaunch scanner detection.launch
// in patrol_y
>rosrun patrol warehouse_action (use key 'w')
