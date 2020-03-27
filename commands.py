import rospy
from geometry_msgs.msg import Twist


class allCommands():

    def command_move():
        rospy.loginfo("This move command is currently under construction")
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    def command_grab():
        rospy.loginfo("This grab command is currently under construction")
