#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import speech_recognition as sr

class VoiceInput(Node):

    def __init__(self):
        super().__init__('mic_input')
        self.publisher_ = self.create_publisher(String,'mic_input',10)
        self.r = sr.Recognizer()
    
    def voicerecord(self):
        self.get_logger().info('text')
        while rclpy.ok():
            with sr.Microphone() as source:
                self.r.adjust_for_ambient_noise(source, duration=10)
                audio = self.r.listen(source)

            try:
                text = self.r.recognize_google(audio)
                self.get_logger().info(text)

                msg = String()
                msg.data = text
                self.publisher_.publish(msg.data)
            except sr.UnknownValueError:
                self.get_logger().warn('error')
            except sr.RequestError as e:
                self.get_logger().error(f"Could not request results; {e}")

def main(args=None):
    rclpy.init(args=args)

    node = VoiceInput()

    node.voicerecord()

    rclpy.spin(node)

if __name__=="__main__":
    main()
