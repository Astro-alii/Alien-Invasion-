# Alien Invasion 🛸👽

A Python-based arcade game inspired by the classic Space Invaders, featuring two unique control schemes: traditional keyboard controls and innovative gesture-based controls using hand detection.

## Overview

Alien Invasion is a space shooter game where players defend Earth from descending alien fleets. The game features engaging visuals, sound effects, progressive difficulty levels, and score tracking. Players can choose between keyboard controls (traditional gameplay) or gesture controls (hand-tracking via webcam) for a modern, interactive experience.

## Features

### Core Gameplay
- **Progressive Difficulty**: Enemy speed increases with each level cleared
- **Two Weapon Types**:
  - Regular bullets (multiple shots allowed)
  - Powerstrike (special high-impact weapon, limited per turn)
- **Health System**: Visual lifeline bar that depletes on collision with aliens
- **Score Tracking**: Real-time scoring with persistent high-score tracking
- **Dynamic Fleet**: Aliens move horizontally, drop when reaching screen edges
- **Collision Detection**: Proper collision handling for bullets, powerstrikes, and ship

### Controls

#### Main Branch (Keyboard Controls)
- **Arrow Keys**: Move ship up/down/left/right
- **Spacebar**: Fire bullets (2 max at a time)
- **Shift**: Fire powerstrike (1 at a time)
- **Q**: Quit game

#### Gesture-Control Branch (Hand Gesture Recognition)
- **Hand Position**: Move ship horizontally and vertically by moving your hand
- **Index Finger Up**: Fire bullets (2 max at a time)
- **All Fingers Up**: Fire powerstrike (1 at a time)
- **Q**: Quit game
- Live webcam feed showing hand detection (top-left corner)

## Branch Structure

### `main` - Traditional Keyboard Controls
The original implementation using classic arcade controls:
- Traditional arrow key movement
- Mouse-click menu interaction
- Standard keyboard input for shooting
- Larger ship sprite (100x100px)
- Fully keyboard-driven gameplay

**To play keyboard version:**
```bash
git checkout main
python alien_invasion.py
```

### `gesture-control` - Hand Gesture Controls
Modern gesture-based control using computer vision:
- Real-time hand detection via webcam (cvzone + MediaPipe)
- Hand position tracking for ship movement
- Gesture recognition for shooting (finger positions)
- Background thread for hand detection (non-blocking)
- Smaller ship sprite (50x50px) for gesture space
- Live camera feed overlay

**To play gesture version:**
```bash
git checkout gesture-control
python alien_invasion.py
```

## Installation

### Prerequisites
- **Python 3.11** (required — mediapipe does not support Python 3.12+)
- Webcam (required for gesture-control branch)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Alien\ Invasion
   ```

2. **Create a virtual environment with Python 3.11**
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Requirements

A `requirements.txt` file is provided. Install all dependencies via:

```bash
pip install -r requirements.txt
```

| Package | Version |
|---|---|
| pygame | 2.6.0 |
| opencv-python | 4.10.0.84 |
| mediapipe | 0.10.14 |
| cvzone | 1.6.1 |

## How to Play

### Starting the Game
```bash
python alien_invasion.py
```

### Gameplay Flow
1. **Menu Screen**: Click "Play" to start or "Quit" to exit
2. **Game Screen**: 
   - Defend against descending alien fleets
   - Use your weapon(s) to destroy enemies before they reach you
   - Each destroyed alien scores 10 points
   - Lose if aliens reach the bottom or collide with your ship
3. **Game Over**: View your score and high score, play again or quit

### Tips for Gesture Control
- Ensure good lighting and clear hand visibility
- Keep your hand within the camera frame
- Make deliberate finger gestures (fully extended or curled)
- The camera window appears in the top-left corner during gameplay
- Relax and enjoy the intuitive control!

## Game Architecture

### Core Classes

**alien_invasion.py** - Main game controller
- Initializes pygame and game objects
- Manages game states (menu, playing, game over)
- Handles collision detection and game logic
- Coordinates sprite updates and rendering

**ship.py** - Player's spaceship
- Keyboard version: responds to key input events
- Gesture version: position updated via hand detection
- Manages collision with aliens
- Health/damage tracking

**alien.py** - Enemy sprites
- Moves horizontally in formation
- Drops down when reaching screen edges
- Direction reversal on edge detection

**bullet.py** & **powerstrike.py** - Weapon projectiles
- Bullet: fast, multiple allowed, standard damage
- Powerstrike: slower, limited quantity, powerful

**gestures.py** (gesture-control branch only)
- Hand detection via cvzone + MediaPipe
- Background thread for non-blocking detection
- Gesture recognition (finger positions)
- `_ensure_initialized()` guard prevents premature sensor access
- Safe `fingersUp()` calls with null checks and try/except to handle race conditions between the detection thread and main game thread
- Camera feed management

**settings.py** - Game configuration
- Screen dimensions (1000x800)
- Sprite speeds and spawn rates
- Difficulty multipliers
- Point values

**hud.py** - Heads-up display
- Score rendering and persistence
- Lifeline bar visualization
- Game UI elements

**gamestats.py** - Game state tracking
- Current score, high score
- Lives remaining
- Game flags

## File Structure
```
Alien Invasion/
├── alien_invasion.py      # Main game loop and logic
├── ship.py                # Player ship class
├── alien.py               # Enemy alien class
├── bullet.py              # Regular bullet weapon
├── powerstrike.py         # Special weapon
├── gestures.py            # Hand detection (gesture-control branch)
├── settings.py            # Game configuration
├── hud.py                 # UI and score display
├── gamestats.py           # Game statistics
├── button.py              # Menu button UI
├── requirements.txt       # Python dependencies
├── scores.txt             # High score tracking (generated)
├── Images/                # Game sprites and assets
│   ├── starship.bmp
│   ├── alien.png
│   ├── spacebg.png
│   ├── hp_filled.gif
│   ├── hp_empty.gif
│   └── hp_heart.gif
└── Sounds/                # Audio effects
    ├── bullet.wav
    ├── powerstrike.wav
    ├── start.wav
    ├── game_over.wav
    └── Bg.mp3
```

## Development Notes

### Gesture Control Implementation
- Uses cvzone's HandDetector for real-time hand tracking
- Background thread (`_detection_loop`) runs detection without blocking game render
- Hand center coordinates map directly to ship position
- Finger configurations detected for different actions:
  - `[0,1,0,0,0]`: Index finger up (shoot)
  - `[1,1,1,1,1]`: All fingers up (powerstrike)
- All sensor methods call `_ensure_initialized()` before accessing the detector
- `fingersUp()` is guarded with `hasattr` checks and wrapped in `try/except (AttributeError, IndexError)` to prevent crashes when the background thread hasn't finished populating `results` yet

### Performance Considerations
- 120 FPS target frame rate
- Hand detection runs on separate thread for smooth gameplay
- Camera feed resize (380x180) to reduce processing
- Sprite collision uses pygame's built-in groupcollide for efficiency

### Known Differences Between Branches
- Ship size: 100x100 (keyboard) vs 50x50 (gesture)
- Movement system: Event-driven flags vs real-time position tracking
- Input method: Key events vs hand position/gestures
- Camera requirements: None (keyboard) vs webcam required (gesture)

## Future Enhancements

- [ ] Mobile support for gesture controls via phone camera
- [ ] Multiplayer mode
- [ ] Additional weapon types and power-ups
- [ ] Enemy behavior variations
- [ ] Customizable difficulty settings
- [ ] Controller/joystick support
- [ ] Animated sprites and particles
- [ ] Online leaderboards

## Troubleshooting

### Gesture Control Issues
- **Camera not detected**: Check system permissions and camera availability
- **Hand not detected**: Ensure good lighting and clear hand visibility
- **Jerky movement**: Camera may be slow; try reducing detection window or closing other apps
- **Performance issues**: Lower gesture detection resolution or check system CPU usage
- **`AttributeError: 'HandDetector' object has no attribute 'results'`**: Ensure you are using **Python 3.11** and the exact dependency versions in `requirements.txt`. This error occurs due to a race condition between the detection thread and the main thread; the current codebase handles this with null guards and try/except in `gestures.py`.

### General Issues
- **Assets not loading**: Ensure Images/ and Sounds/ directories exist with required files
- **Game crashes**: Verify all dependencies installed correctly with `pip install -r requirements.txt`
- **Import errors**: Activate virtual environment with `source .venv/bin/activate`
- **mediapipe install fails**: Make sure you are using Python 3.11 — mediapipe does not support Python 3.12 or later

## License

This project is open-source and available for educational and personal use.

## Credits

- Game concept inspired by classic Space Invaders arcade game
- Built with Python, Pygame, and cvzone/MediaPipe for computer vision
- Hand gesture recognition powered by Google's MediaPipe

---

**Choose your control scheme and defend Earth! 🌍✨**
