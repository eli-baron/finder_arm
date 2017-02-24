#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
def listener():
	#En ros , los nodos tienen nombre unicos. si dos nodos con el mismo
	#nombre son lanzados, el anterior es echado. El anonymous=True
	#significa que rospy elegira un unico nombre para nuestro nodo
	#'listener' tal que multiples nodos llamados 'listener' puedan se 
	#lanzados simultaneamente
	rospy.init_node('listener',anonymous=True)
	rospy.Subscriber("chatter",String,callback)
	rospy.spin()
if __name__=='__main__':
	listener()

