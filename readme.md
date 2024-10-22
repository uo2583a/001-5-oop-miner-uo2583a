In this assignment, you'll be designing several classes using the tenets of object-oriented programming. All of these classes will be used in a Pygame application to produce a heavily-simplified version of a popular game. 

## 1. Player Character 

Create a Python class called `Player` in a file called `Player.py` that represents a player character in a game. Here's a concise description of its methods:

1. `__init__(self, window, windowWidth, windowHeight)`: Initializes the player object with attributes such as the game window, window width, window height, image, position, and explicitly private score.

2. `update(self)`: Updates the player's position based on keyboard input. It moves the player left, right, up, or down based on which arrow key is pressed. The player should continue to move in that direction as long as a key is being held down.

3. `check_collide(self, other_character)`: Checks collision between the player and another character in the game. Returns True if they collide, False otherwise.

4. `get_rect(self)`: Returns a rectangle representing the player's current position and dimensions.

5. `score` (property): Gets the player's score.

6. `score` (setter): Sets the player's score. Ensures that the score is an integer.

7. `draw(self)`: Draws the player on the game window at its current position.


## 2. Minecraft Characters

Create four Minecraft Character Classes: `Creeper`, `Zombie`, `Cow`, and `Chicken` all in separate files matching the name of the class. 

1. All classes should have the same interface:

   1. `__init__(self, window, windowWidth, windowHeight)`: Initializes the character object with attributes such as the game window, window width, window height, image, position, and speed.
   2. `update(self)`: Updates the character's position based on its current speed. It also checks if the character hits the boundaries of the game window and changes direction accordingly.
   3. `draw(self)`: Draws the character on the game window at its current position.
   4. `get_rect(self)`: Returns a rectangle representing the character's current position and dimensions.

2. Each of these four classes are represented on screen by the image that matches the class name. They will bounce around the screen in different ways.
   -  The `Creeper` and `Zombie` objects will bounce randomly in any direction. When they hit any side of the screen they reverse direction. The `Creeper` always moves more slowly (1 or 2 pixels in a direction per frame) than the `Zombie` (3 or 4 pixels per frame). 
   - The `Cow` and `Chicken` objects only move in one direction. Cow objects only bounce vertically up and down. Chicken objects only move horizontally. 

## 3. Mob Base Class:

1. Create a base class called `Mob`. As you may notice, each of the classes above are extremely similar to each other. To receive full credit for this assignment, one or more of your classes must extend the base class.
2. The interface for Mob is left up to you. Some methods might make more sense to be implemented in the base class, some in the child classes. You may also have a named method in both the base and the child class, with common code in the base and differentiating code in the child, and rely on the super() method call to get the best of both worlds. To receive full credit for this assignment, the child class must override and extend at least one method in the parent. 


## 4. Game Loop:

Create a new file `Launch.py` in which you will build an interactive application using the classes defined here. Start with the 12-step template defined in the textbook and write your own code to the following requirements:
1. Initialize 1 player, 3 creepers, 5 chickens, 2 zombies, and 3 cows in random positions. Place all non-player objects into a single list for update and draw. You may update and draw the player separately.
2. Each frame, check to see if the player collides with any other characters. The goal of the game is to have the player collide with as many zombies as possible while avoiding collisions with chickens, cows, or creepers.
   1. If a player collides with a creeper, the game ends and the player's current score is printed out to the console. 
   2. If a player collides with a zombie, the player's score is increased by 25. Then, the Zombie disappears from the screen and is no longer updated or drawn. If all zombie have disappeared, the game ends and the player's current score is printed out to the console. 
   3. If a player collides with a cow, the player's score is decreased by 10. Then, the cow disappears from the screen and is no longer updated or drawn.
   4. If a player collides with a chicken, the player's score is decreased by 5. Then, the chicken disappears from the screen and is no longer updated or drawn.

## Scaling Images
Since the images are not guaranteed to be the same size, or even a useful size for this application, it's recommended that you scale them. You can do this when they are loaded. For example, if a ball image were larger than 100 x 100 pixels, you could scale it down to that size with the following statement:

```python
self.image = pygame.transform.scale(pygame.image.load('../images/ball.png'), (100,100))
```

You are free to choose image sizes for the various characters that you think makes the game more fun.
