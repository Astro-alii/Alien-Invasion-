import cv2 
from cvzone.HandTrackingModule import HandDetector


class Gestures:
    def __init__(self, game):
        self.capture = cv2.VideoCapture(0)
        self.detector = HandDetector(0.8, 2)
        self.detection_on = True

    def detect_gesture(self):
        """Starts Main loop to capture Image on each frame"""
        if self.detection_on:
            success , img =self.capture.read()
            if not success:
                return
            self.img = cv2.flip(img,1)
            self.hands , img = self.detector.findHands(img)
            self.set_hand_detection()
            cv2.imshow ("Alien Invasion", self.img)
        
    def close_detection(self):
        """Stops the detect_gesture loop"""
        self.detection_on = False
        self.capture.release()
        cv2.destroyAllWindows()
        
    def set_hand_detection(self):
        """Assigns Identifier to each hand"""
        if len(self.hands)>= 1:
            self.left_hand = self.hands[0]
        if len(self.hands)>= 2:
            self.right_hand = self.hands[1]
            
        

    def index_finger_up_sensor(self):
        """Senses Index finger for bullet fire"""
        if not hasattr(self, "left_hand"):
            return False
        left_fingers = self.detector.fingersUp(self.left_hand)
        if left_fingers == [0,1,0,0,0]:
            return True
        
    def all_finger_up_sensor(self):
        """Senses Index finger for bullet fire"""
        if not hasattr(self, "left_hand"):
            return False
        left_fingers = self.detector.fingersUp(self.left_hand)
        if left_fingers == [1,1,1,1,1]:
            return True
        


            


        