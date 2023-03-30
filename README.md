# Dodge-the-Obstacles
This is a simple game called "Dodge the Obstacles". In this game, the player controls a character that can move left or right at the bottom of the screen, while obstacles fall from the top of the screen. The player's goal is to dodge the obstacles by moving the character left or right. Each time the player successfully dodges an obstacle, their score is incremented. If the player collides with an obstacle, the game ends.

The game is built using the Pygame library, which provides a way to handle graphics and user input in Python. The game window is set up with a resolution of 400x400 pixels, and the character and obstacles are represented as rectangles that can be drawn on the screen using Pygame's draw module. The game loop continuously handles user input, updates the game state, and redraws the screen until the game is over.

The speed of the character and obstacles can be adjusted by modifying the character_speed and obstacle_speed variables. In this code, the speed of both is set to 0.09, which may be too fast for some players. Slowing down the speed can make the game easier to play.
