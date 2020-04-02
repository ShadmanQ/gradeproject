import rospy
from geometry_msgs.msg import Twist


class allCommands():
    def __init__(self):
        rospy.loginfo("Commands have started")

    def command_move(self, input):
        rospy.loginfo("This move command is currently under construction")
        number = 0
        for element in input.split():
            if element.isnumeric():
             #   rospy.loginfo(element)
                number = int(element)
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        twist = Twist()
        twist.linear.x = 0; twist.linear.y = number; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        print(twist)
        # work that out in a second
        pub.publish(twist)

    def command_grab(self):
        rospy.loginfo("This grab command is currently under construction")
