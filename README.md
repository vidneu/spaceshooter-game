# Space Shooter Game

## Description
This is a simple 2D space shooter game implemented using Python and Pygame. The game features a spaceship that remains stationary on the screen while natural (asteroids) and artificial (satellites) objects move towards it. The player can shoot laser beams to destroy these objects and earn points.

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/githubnext/workspace-blank.git
   ```
2. Navigate to the project directory:
   ```
   cd workspace-blank
   ```
3. Install the Pygame library:
   ```
   pip install pygame
   ```

## How to Run
1. Ensure you are in the project directory.
2. Run the game:
   ```
   python main.py
   ```

## Gameplay Instructions
- The spaceship is located at a fixed position on the screen.
- Natural objects (asteroids) and artificial objects (satellites) will appear from the opposite side and move towards the spaceship.
- Left-click to shoot a laser beam towards the mouse click coordinates.
- If the laser beam hits a natural object, the player earns +20 points.
- If the laser beam hits an artificial object, the player loses -100 points.
- The laser cannon has a cooldown period of 2 seconds after each shot.
- If a natural object collides with the spaceship, the spaceship takes damage.
- After four collisions, the spaceship is destroyed, and the game is over.
- The player's score and the spaceship's health status are displayed at the top left of the screen.
