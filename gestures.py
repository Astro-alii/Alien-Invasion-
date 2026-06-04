import cv2 
from cvzone.HandTrackingModule import HandDetector
import threading

class Gestures:
    def __init__(self, game):
        self.game = game
        self.capture = cv2.VideoCapture(0)
        self.detector = HandDetector(0.8, 2)
        self.detection_on = True
        
        #opencv window resize
        cv2.namedWindow("Alien Invasion", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Alien Invasion", 380, 180)
        cv2.moveWindow("Alien Invasion", 20, 20)
        
        self.img = None 
        self.thread = threading.Thread(target=self._detection_loop, daemon=True)
        self.thread.start()

    
    def _detection_loop(self):
        """Runs continuously in background"""
        while self.detection_on:
            success, img = self.capture.read()
            if not success:
                continue
            self.img = cv2.flip(img, 1)
            self.hands, self.img = self.detector.findHands(self.img)
            self.set_hand_detection()
            
    
    def camera_screen_on(self):
        """Makes the camera screen visible"""
        cv2.imshow("Alien Invasion", self.img)
        cv2.waitKey(1)
    
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
    
    def horizontal_movement_sensor(self):
        """Detects the horizntal movement of ship"""
        self.currentx = self.game.ship.rect.centerx
        hand_centerx , hand_centery =  self.left_hand["center"]
        self.currentx = hand_centerx
        self.game.ship.rect.centerx = self.currentx

    def vertical_movement_sensor(self):
        """Detects the horizntal movement of ship"""
        self.currenty = self.game.ship.rect.centery
        hand_centerx , hand_centery =  self.left_hand["center"]
        self.currenty = hand_centery
        self.game.ship.rect.centery = self.currenty



            


        