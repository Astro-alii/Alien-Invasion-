import cv2
from cvzone.HandTrackingModule import HandDetector
import threading

class Gestures:
    def __init__(self, game):
       self.game = game
       self.capture = None
       self.detector = None
       self.detection_on = False
       self.img = None
       self.thread = None
       self._initialized = False

    def _initialize_camera(self):
        self.capture = cv2.VideoCapture(0)
        self.detector = HandDetector(0.8, 2)
        self.detection_on = True

        self.thread = threading.Thread(target=self._detection_loop, daemon=True)
        self.thread.start()
        self._initialized = True

    def _ensure_initialized(self):
        if not self._initialized:
            self._initialize_camera()
    def _detection_loop(self):
        """Runs continuously in background"""
        if not self.detection_on:
            return
        while self.detection_on:
            success, img = self.capture.read()
            if not success :
                continue
            self.img = cv2.flip(img, 1)
            self.hands, self.img = self.detector.findHands(self.img)
            self.set_hand_detection()
            
    
    def camera_screen_on(self):
        """Makes the camera screen visible"""
        self._ensure_initialized()
        if self.img is not None:
            cv2.imshow("Alien Invasion", self.img)
            cv2.waitKey(1)
    
    def close_detection(self):
        """Stops the detect_gesture loop"""
        self.detection_on = False
        if self.capture is not None:
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
        self._ensure_initialized()
        if not hasattr(self, "left_hand"):
            return False
        if not hasattr(self.detector, 'results') or self.detector.results is None:
            return False
        if not self.detector.results.multi_hand_landmarks:
            return False
        try:
            fingers = self.detector.fingersUp(self.left_hand)
            return fingers == [0,1,0,0,0]
        except (AttributeError, IndexError):
            return False
        
    def all_finger_up_sensor(self):
        """Senses all fingers up for powerstrike"""
        self._ensure_initialized()
        if not hasattr(self, "left_hand"):
            return False
        if not hasattr(self.detector, 'results') or self.detector.results is None:
            return False
        if not self.detector.results.multi_hand_landmarks:
            return False
        try:
            fingers = self.detector.fingersUp(self.left_hand)
            return fingers == [1,1,1,1,1]
        except (AttributeError, IndexError):
            return False
    
    def horizontal_movement_sensor(self):
        """Detects the horizntal movement of ship"""
        self._ensure_initialized()
        if not hasattr(self, "left_hand"):
            return False
        hand_centerx , hand_centery =  self.left_hand["center"]
        self.game.ship.rect.centerx = hand_centerx

    def vertical_movement_sensor(self):
        """Detects the vertical movement of ship"""
        self._ensure_initialized()
        if not hasattr(self, "left_hand"):
            return False
        hand_centerx , hand_centery =  self.left_hand["center"]
        self.game.ship.rect.centery = hand_centery
