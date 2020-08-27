#!/usr/bin/env python

"""
  @author Roberto Zegers
  @brief  Reinitializes AMCL particles to a new estimated mean and covariance
  @date   Aug 27, 2020
"""

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

rospy.init_node('amcl_init_pose')
pub_pose = rospy.Publisher('/initialpose',PoseWithCovarianceStamped, latch=True, queue_size=10)
rospy.sleep(1.0)
rospy.loginfo("(Reinitializing AMCL particles...")

initialpose_msg = PoseWithCovarianceStamped()
initialpose_msg.header.seq = 0
initialpose_msg.header.stamp.secs = 0
initialpose_msg.header.stamp.nsecs = 0
initialpose_msg.header.frame_id = "map"
initialpose_msg.pose.pose.position.x = -3.5
initialpose_msg.pose.pose.position.y = 5.0
initialpose_msg.pose.pose.position.z = 0
initialpose_msg.pose.pose.orientation.x = 0
initialpose_msg.pose.pose.orientation.y = 0
initialpose_msg.pose.pose.orientation.z = 0
initialpose_msg.pose.pose.orientation.w = 1
initialpose_msg.pose.covariance[0]= 4.00
initialpose_msg.pose.covariance[7]= 4.00
# initial_cov_aa default (PI/12)*(PI/12) radian = 0.0685
# PI*PI radian = 9.8696
initialpose_msg.pose.covariance[35]= 9.8696

pub_pose.publish(initialpose_msg)
rospy.loginfo("Done")
