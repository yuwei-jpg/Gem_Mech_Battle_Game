Gem Mech Battle: A Side-Scrolling Saga
============================================
#### Yuwei Ji, Michael Abidemi Laleye, Olan James Kelleher, Cian Cripps

Introduction
--------------------------------------------
In the digital age, software has become an integral part of our daily lives. From smartphone apps to complex server systems, software is omnipresent. But how is this software built? If you're just stepping into your junior year of college, you might be curious about this. This chapter aims to demystify the process of software development through my project experience, offering you a peek behind the curtain.

Project Overview
--------------------------------------------
In the realm of 2D side-scrolling games, Gem Mech Battle emerges as a vivid escapade, blending precision and whimsy in a world where strategy meets agility. Our protagonist, equipped with a trusty cannon, ventures forth on a courageous expedition to procure a fortune in diamonds, each shimmering stone a jewel in the crown of their arduous quest. You have to defeat the robots with your weapons. This project was not just a programming exercise but a deep dive into the entire software development process.

Map (World & Level_Editor)
--------------------------------------------
### World
The game "Gem Mecha War" builds a vibrant and immersive world through a carefully designed map system. The map not only serves as the backdrop for the adventure, but also plays a vital role in the gameplay, affecting exploration, puzzles, and encounters with allies and opponents.
* **Loading and Displaying the Map**  

The map is composed of individual tiles, each of the tiles represented by an image. These tiles are loaded into an `img_list`, which stores the graphical representation of each tile type. The `NUM_TILES` indicates the total number of tile types and `TILE_SIZE` defines the dimensions of each tile. The game can accommodate a diverse range of environments, from rocky terrains and water bodies to decorative elements that enrich the game's atmosphere.
* **World Generation**

The `World` class is at the heart of map construction. It initializes with an `objects_group`, a structure designed to manage different categories of game objects, including exit points, water bodies, diamonds, potions, and enemies like the Ghost.

The `generate_world` method takes two parameters: `data`, which represents the layout of the map in a grid format, and `win`, the window where the game is rendered. It iterates over `data`, placing tiles according to their designated positions and types. This method meticulously categorizes tiles into `ground_list`, `rock_list`, and `decor_list`, depending on their nature and gameplay function, such as navigable terrain, obstacles, or aesthetic background elements.
* **Interactive Elements and Objectives**

Notably, the game map is populated with interactive elements that are essential to the gameplay:

1. [ ] _Exit Points: The special tiles allow the player to enter into the next level._
2. [ ] _Water Bodies: When the player drops into the water, he/she will die._
3. [ ] _Diamonds: The player collects diamonds and he/she will gain points._ 
4. [ ] _Potions: When the player gets hurt, he/she may get the potion to recover._

Each of these elements is derived from the `pygame.sprite.Sprite` class, enabling them to be easily managed, animated, and interacted with within the game's engine.
* **Dynamic Environment**

The game's map and its elements are designed to be dynamic. The `update` methods in each sprite class enable real-time adjustments to the game environment, such as the ability to scroll the map to follow the player's movements, ensuring a seamless and engaging gaming experience.

### Level_Editor
The level editor uses `pygame` to create and modify the game’s level directly. It uses a tile-based approach to build a diverse and engaging game environment.

* **Map Area**

The game world is visualized in a grid layout, with each cell representing a potential placement for a tile. The map supports horizontal scrolling, facilitated by `scroll_left` and `scroll_right` controls, allowing for the creation of extensive levels that exceed the screen width.

* **The Selection Panel**

This panel displays all available tiles as selectable buttons. Clicking a tile button sets it as the current tile, which can then be placed on the map. A red outline highlights the selected tile, providing clear visual feedback to the user.

* **Dynamic Backgrounds**

The level editor enhances the beauty of the game world by incorporating layered background images. These images are enlarged or reduced to fit the screen size and drawn behind the tile map, creating a vibrant and immersive background for the level.

* **Saving and Loading Levels**

The level editor includes functionality to save and load level data, ensuring that designers can load the designed levels and modify and save them. The `"Save"` and `"Load"` buttons trigger the serialization of the `world_data` array to the `Level_Data` folder and the deserialization of level data from the file, respectively. This feature supports the iterative design process by allowing level adjustments over multiple sessions.

* **Level Navigation**

Designers can navigate through different levels using the `"Left"` and `"Right"` arrow buttons, adjusting the `current_level` variable. This capability enables the management of multiple level designs within the same editor session, enhancing the tool's versatility.

* **Enhanced User Experience**

The level editor includes a clock to regulate the update frequency `('FPS')` ensures that the editor runs smoothly, providing a responsive and enjoyable user experience. Additionally, the editor gracefully handles user input, including keyboard shortcuts for scrolling and adjusting scroll speed, as well as handling window close events to terminate the session cleanly.

Text
--------------------------------------------
The `texts` python code example accompanies by the book and uses the pygame library for rendering text and displaying it within a graphic interface. In games, being able to present text to the user is critical. The fonts are also one of the primary factors of how beautiful a game is, so, how to show fonts to users is an important topic to discuss. The `texts` python code separates its creation for into several key parts, which are designed for handling different functionalities related to text:

* **The Text Class** 

The `Text` class creates a text image using a specific font in a set size that is suitable when you are dealing with static text.

* **The Message Class** 

The `Message` class on the other hand, is for when you want to display text at a specific position in your window. It also includes the option of adding a shadow to the text to make it easier to read. It also includes an `update` method which lets you refresh the text content and the way it looks dynamic.

* **The BlinkingText Class** 

The `BlinkingText` class is a subclass of a `Message`. It adds the ability to allow you to create blinking text effects. It does this by changing the visibility of the text at set intervals. You will often use this effect to catch the attention of a user for important messages.

* **The MessageBox Function** 

The `MessageBox` function when called will draw a message box including text to the screen. It includes automatic line wrapping of the text, so it all fits within the boundaries of the box. A title may be added to the message box, so that different messages can be clearly segmented from each other.


Button
--------------------------------------------
The `Button` class creates interactive buttons using the pygame library with optional text labels and hover effects for a graphical user interface.

To use a Button, you must first make an instance of the `Button `class. The parameters for `init `are as follows:

* **Image**

This is the only required attribute for creating a button. You pass the filename of the image you want to use, with a transparent background (which will make note of anything of that color).

* **Position**

A two item tuple containing the `'x'` and `'y'` positions on the screen where the dialog is to be blit.

* **Size**

This can either be None, in which case the image will be used as its own size. Alternatively, you can pass an int which will be used to scale the image by that factor.

* **On_Click**

You can link the button to either a virtual keyboard button (in which case the keyboard will be created, and the button added to it, in the same script), or a function.

* **Text**

This optional argument just adds text to the button—it is drawn centrally over the button.

* **Drawing the Button**

When the button is created, it is initialised, with its size equal to the size of the image (if no size is provided), or the image scaled by the size parameter. If a text is provided, positions for text placement (as an offset to the top left corner of the button) are also calculated. All button images should be contained in the directory `"/Assets/"` and be of the format button*.png.

The `draw` method for the `Button` class will handle rendering the buttons onto a surface that is passed to it. This method contains code to detect if the mouse is lying within the button, and if so, will draw the button in this position. It also checks to see if the button has had its pressed flag set to true. If so, then a third, sad image will be used. A rectangle is calculated which entirely encloses the button. If the text attribute has been set, then the text will also be rendered to this surface, at the calculated offset positions.

Particles
--------------------------------------------
The `particles` python code defines two classes, `Trail` and `Explosion`, for creating visual effects in a game developed using the pygame library. They leverage Pygame's sprite system to handle both dynamically manipulating and rendering the effects. This ultimately enhances the visual appeal of the game.

The `Trail` class creates a trail effect, simulating particles following behind a moving object. It initializes with a position, color, and window surface `('win')` on which to render. It uses a `pygame.Surface` with `SRCALPHA` to allow for alpha transparency, and thus, the trail to fade out. It adjusts its position based on a velocity vector, which includes a random horizontal component for a more natural effect. It gradually decreases in size, and fades out ( `'life'` attribute) until it disappears.

The `Explosion` class creates an explosion effect at a specified location. The effect simulates a burst of particles. As with Trail, it initializes with a position and window surface on which to render, but adds a velocity for the explosion that simulates an outward burst and follows the format of a velocity attribute for Trail. It manages its lifecycle through a `life` duration and `lifetime`, such that it fades out and eventually disappears. 
It progressively decreases the alpha value of its color, to provide a smooth fade away of the explosion The size of the explosion decreases over time, and it modifies the color and redraws to visually represent this change.

Both classes implement an `update` method that manages their behavior, such as it is, frame-by-frame. Namely, they manage their movement, resizing, fading and ultimate removal from the game. They both also have a `draw` method to render themselves to the provided window surface.

Projectiles
--------------------------------------------
The `projectiles` python code snippet uses the `pygame` library to demonstrate the `Bullet` and `Grenade` classes in a game. These classes handle the behavior and rendering of bullets and grenades in a game environment.

The `Bullet` class simulates a bullet that a player or enemy could fire. Bullets move horizontally across the screen, remove themselves when they collide with a world object, and do not pass through ground tiles.

The `Grenade` class simulates a grenade that could be thrown. It bounces and explodes. It changes a direction and velocity, influenced by gravity, and colliding against a world object. It uses the Explosion class to make a visual effect when it explodes. The explosion makes a countdown, harming every unit that is too close when the countdown reaches 0, which is demonstrated using the player as well.

Both classes define an `update` method to move, adjust their state and check for collisions (also to draw them). This way when update is called on each object, movements and actions are performed, and they’re drawn to the game window directly using the draw functionality the update methods contain.

Player
--------------------------------------------

The `player` python code defines a Player class that is responsible for all aspects of the player character within the game, developed with the pygame library. The player character is responsible for the creation of the player character, with all its various animations, the handling of its movement, and the management of all of its interactions within the game world.

* **Initialization and Attributes**

1. [ ] _Player Setup: The player is initialized with his position coordinates by the initialization function and then loads a variety of different animations from a directory of images which are then used as different states of the game such as idle, walking, attacking, dying, hit and defending._
2. [ ] _Scaling and Animation: All of these images that are loaded are then scaled to a target height, to maintain consistency, after their dimensions (in pixels). The character has flip to it, so it can also face right or left by appropriately flipping the images._
3. [ ] _Physics and Movement: With the character initialized, the physics of the character are then initialized. They require the setting of speeds, and then everything is simulated to create a reality of the game._

* **Movement**
1. [ ] _Horizontal Movement: The horizontal movement is controlled from two different flags defined earlier, `'moving_left'` and `'moving_right'` which when they are then signalled to be active using `self.left` or `self.right`, will then change the position of the character `('self.x')` by moving it by a `self.speed` multiplied by a `self.direction` to specify whether to move it right or left. The value to direction also determines which set of images as the walking ones, either `self.walk_left` or `self.walk_right` should be used instead to present the motion of the player character._
2. [ ] _Direction and Animation: With a value in the direction attributing `('self.direction')`, motion is then permitted to use the appropriate animation under the motion control. -1 is for left, 1 is for right and 0 for idle._

* **Jumping Mechanics**
1. [ ] _Initiating a Jump: With a position set, as activated by the `'self.jump'` flag the motion of the character was then controlled from the vertical velocity `('self.vel')` changing its position. The jumping has been created as a force with an abating one being applied as long as the player remains in the air to give the appearance of gravity._
2. [ ] _Gravity and Falling: The gravity has been being illustrated by continually changing the vertical velocity, this means the character falls back down after the jump and then appropriately reaches and lands on the ground or the platforms. The quicker the player is falling, the quicker this change will take place as influenced by `self.gravity`._

* **Attacking and Defense**
1. [ ] _Attacking: During the duration of the `self.attack` flag the character will be in the status of an attack. This is typically activated by player movement, i.e. pressing g key and the characters sprites will then cycle through the `self.attack_list` animations. The player will be in the state of 'defend' until this last attack image is removed or the state is interfered with._
2. [ ] _Defense: The defensive state is similarly controlled and is activated by the setting of a flag itself `'self.defend'`. The player character is in the defensive stance. This will often include the player having a reduced movement during its duration while its sprites are cycled through its `self.defend_list` animations, were after they will then simply remain in that state until a defence action is passed._

* **Collision Detection and Response**
1. [ ] _Collision with the Environment: The `check_collision` method is crucial for handling interactions with the game world. It checks for collisions with ground and obstacle tiles and adjusts the player's position to prevent overlapping or passing through solid objects. This ensures logical movement and interaction within the game environment._
2. [ ] _Response to Collisions: When a collision is detected, the player's movement is adjusted to align with the surface of the ground or to stop movement in the direction of an obstacle. This creates a seamless experience, preventing the player from moving through walls or falling through floors._

Enemy
--------------------------------------------
The `Robot` class, as part of a game developed using pygame, defines an enemy character with behaviors such as patrolling, taking damage, dying, and shooting bullets at the player.
* **Initialization**
1. [ ] _Attributes: The robot starts at a set `'x'`, `'y'` coordinate and has a set size. The series of images for walking (left and right), taking hits and dying animations are loaded in and are scaled to the appropriate size._
2. [ ] _Movement Direction: The robot's initial horizontal direction `(self.dx)` is randomly chosen, so he starts by either moving left or right so that his behavior is still unpredictable when the game starts._

* **Update Method**
1. [ ] _Movement: The robot moves horizontally, and he flips his direction whenever he has moved a certain distance so that it seems like he is patrolling. The variable `screen_scroll `adjusts his position relative to the player's movement so that he continues to stay in place within the game world._
2. [ ] _Health and Death: The robot's health is monitored and when his health reaches zero he transitions into a dying state `(self.on_death_bed)` and when his death animation is over he leaves the game._
3. [ ] _Attacking: On a regular basis, the robot checks his distance to the player, and if he is close enough, he shoots a bullet. This adds a combat dynamic where the robot becomes a threat to the player._
4. [ ] _Sound Effects: A sound effect of the robot shooting is played so that the game's auditory feedback is more complete._

* **Animation Handling**
1. [ ] _Animation Cycling: Through a counter-mechanism the class cycles through the animation frames for walking, hitting and dying and updates `self.image` to reflect his current state._
2. [ ] _Directional Animation: The robot's walking animation is different depending on his direction. The correct facing image is selected everytime he is updated, and the animation can be cycled through._

* **Drawing The Robot**

The `draw` method renders the robot's current image to the game window at its current position, ensuring the visual representation matches its state.

* **Key Takeaways**
1. [ ] _State Management: The robot is controlled using a variety of different states such as alive, hit and dying. The correct animation is also used to represent the correct state._
2. [ ] _Interaction with the Player: The robot shoots bullets and reacts to the player's position. The robot actively participates in the game's combat mechanics._
3. [ ] _Animation: Using counter to time images, and select correct animation from the list in regard to the robot walking or standing, taking hits and dying_

Music
--------------------------------------------

The game is meticulously crafted in the sound department, too, with the type of soundtrack that captures a sense of adventure. The music is full of hummable, melodic tunes that blend whimsy with intrigue that sets the stage for the sprite’s journey. They manage to be evocative and heartening on their own, and they complement the action perfectly. 

* **Background Music**

The title loads a background music file `(‘Sounds/menu2.mp3’)` here, and starts playing it in an infinite loop `(loops=-1)` with a volume of 50 percent `(0.5)`. That would ensure you hear the menu music as soon as the game loaded, and continuously thereafter.
* **Sound Effects**

Each sound and song is carefully placed, nested and named in the file tree in relation to the narrator’s exact movements so the runtime can find it as needed. As for those sound effects? All are attached to a specific action or event, and equally blend to create an immersive, dynamic game environment. 
1. [ ] _Diamond Collection `('diamond_fx')`: Played when the player collects a diamond, indicating success and rewarding the player._
2. [ ] _Shooting `('bullet_fx')`: Accompanies the action of firing a bullet, adding realism to combat scenarios._
3. [ ] _Jumping `('jump_fx')`: Triggered when the player jumps, enhancing the physicality of the character's movements._
4. [ ] _Health Pickup `('health_fx')`: Signals the player regaining health, important for indicating recovery during gameplay._
5. [ ] _Menu Interaction `('menu_click_fx')`: Plays upon menu selection, improving user interface responsiveness and feedback._
6. [ ] _Level Advancement `('next_level_fx')`: Marks the transition to a new level, signifying progress within the game._
7. [ ] _Grenade Throw `('grenade_throw_fx')`: Accompanies the act of throwing a grenade, adding weight to this strategic action._
* **Importance of Sound in Game Design**

1. [ ] _Enhanced Immersion: They can draw you deep into a world, dramatically change your experience, engage your emotions and, oftentimes, alert you to what’s happening and what’s about to do down (usually, when you’re least ready for it)._
2. [ ] _Feedback Mechanism: By providing sound feedback and a mood setting, they underline the video game player’s experience — think how much poorer Halo or Mario would be without Marty O’Donnell and Koji Kondo’s soundtracks, or how less terrifying Dark Souls would have been with a minimalist masterstroke like the release of the “4th of July” DLC. That’s right, it would not have been half as scary._

Game
--------------------------------------------
This comprehensive `main` Python code snippet outlines the structure of a 2D game built using the pygame library. It integrates various game components, including player characters, enemies, backgrounds, and interactive objects, along with implementing a main game loop to control gameplay flow, user input, and rendering.
 
* **Initialization and Global Variables**

The initialization of a 2D game window using the `pygame` library, selecting the exact dimensions and setting up no frame display. It also includes definition of constants such as `WIDTH`, `HEIGHT`, `TILE_SIZE`, and it initializes the pygame mixer for sound effects.

* **Sound Effects**

Loading and setting up of background music and various sound effects (`'bullet_fx'`, `'jump_fx'` etc) are employed to enhance the gaming experience and add that extra touch of gameplay immersion that can only be available through auditory feedback in a game, such as when a character is shooting, jumping or collecting items.

* **Sprite Group**

The use of sprite groups to handle different game entities such as bullets, grenades, enemies and collectibles, and is incredibly important as they allows us to manage, update and draw entities, loop through our groups of entities and detect collision between entities.

* **Game Level and Player Setup**

Utilization of the `load_level` and `reset_level` functions to load and set up our game levels by initializing everything such as the world and the objects within the world that the player can interact with. An instance of `Player` is created, and our reset functions ensure that the player can die or progress to the next level in which it will need to be reinitialized once again.
* **Game Loop**

Here we have the main of our game where we manage the game states such as `(main menu, game won, level selection...)`, that will become relevant later down the line of our game development. 
It handles the events, updates the game states, processes the user inputs, and renders the game elements. The user inputs `(keyboard events)` control the player movement in x and y, jumping, shooting, and pretty much anything else you could think of that the player may need to operate. 
There is an implementation of logic that changes the game states that usually are an attribute that will allow us to only render particular game elements such as (main menu, level selection, gameplay...), a mini example would be that anything the user needs to input would be processed in the event section and anything that is a result of the user input would render in the update section. 
We encapsulate collision that the player could come across, any type of collision from enemy bullet to player collision and player health. We encapsulate any interaction of the player with our world such as item pickups, interactions with enemies for a fight or any type of communication the two could have.
* **Rendering and Game Dynamics**

Rendering of all the backgrounds, player, enemies and previously mentioned game object in respect to the game state and player interactions. Update and draw sprite groups is another frequently disposed, an opportunity to keep updating, drawing the entities, managing the animations and their collision between the different game elements. 
Of course, playing sound effects will be a big part of the dynamic rendering, playing any sound effects here such as (shooting, item pickup, ect...), It's a real-time feedback that becomes relevant to the player.

* **Utility Functions**

There are a couple of functions that would be called upon such as `reset_level` and `reset_player`. 
This particular usage allows for the initialization of a new game level or reinitialize the player state in seconds without re-writing it. Another example of utility functions would be that of a custom message box that will render specific text and display this message box with text, can apply this with a lot of things like in-game instructions, story elements, dialogues.

Conclusion ( Lessons Learned )
--------------------------------------------

Developed with `pygame`, `The Gem Mech Battle` is a deep side-scrolling adventure where the player goes through a variety of stages, each with their own set of obstacles and settings. The player character, who can move left or right, leap, shoot bullets, and fire grenades, is the main focus of the game. These abilities are made possible by thoughtfully designed animations and responsive controls.

The player must navigate a variety of landscapes made of tiles that make up the game universe. The gameplay is made more complex with special items like adversaries, health potions, and diamonds. To advance, one must gather diamonds, heal with health pills, and conquer barriers in the form of opponents, such as the robot that patrols and attacks. Specifically, the robot enemy adds dynamic battle circumstances by being able to shoot back at
the player and sustain damage, increasing the difficulty of the game.
Incorporating certain missions or goals into levels might provide gamers more rewards and difficulties than just gathering diamonds. This, in my opinion, can also be made better.
Players may have a more engaging experience if the game's story is expanded. Enhancing the game world can involve introducing people, lore, and goals through cutscenes, in-game text, or environmental storytelling.


Sound effects are also an important part of improving the gaming experience. The game environment comes alive with the sound effects for activities like jumping, shooting and gathering goods and gives instantaneous aural feedback. The background music can make or break the mood for player. 
To even further improve ambience, add more sound effects for different actions and expand the soundtrack from more cave music and different themes. You can make the graphics of the game look so much better with little improvements, for example, adding more dynamic lighting, adding more animated detail, or changing up the particle effects.

One of the key highlights of the game is its level structure. Players can travel through a series of increasingly challenging levels, and each one may have a unique layout and a unique set of problems. I wanted gamers to go into the next level (or even restarting the level if the player dies) to find advancing in the game to be interesting and to find it compelling to build their skills. Adding moving obstacles would allow me to make the player work carefully to survive.

Level editing in the pygame framework is limited only to a level editor. It is not a general tile editor; it is a game-specific tile editor. It lacks the power, flexibility, and sophistication found in general tile editing software, but it does allow basic levels to be designed by placing tiles. So, using the tile editor is financially more sensible and effective for designing more complex game levels.

Additionally, I believe that the AI of the adversary needs to be enhanced. Combat could be made more difficult and interesting by giving the enemy AI more varied attack patterns, behaviors, or the capacity to react to the player's moves.

In addition, enhancing the user experience can involve simplifying the user interface and incorporating functionalities like a pause menu, settings, or control customization options.
The game can be made more inclusive by adding accessibility features like text size adjustment, colorblind modes, and configurable difficulty.


Furthermore, assets have to be adjusted to ensure that the game functions properly on a range of hardware, and coding can improve the user experience in general.
Also, it's critical to keep the game polished, which calls for ongoing testing and issue repairs.

All things considered, `Gem Mech Battle` is a compelling side-scrolling adventure that blends strategic fighting, intricate level design, character control, and a full sound and user interface. Its focus on player interaction along with the difficulty of gathering things and taking out foes makes it an engaging game for anyone seeking repeat value and depth in a pygame-based project.
Nonetheless, there are still a lot of things about this project that might be done better—like the UI interface, opponent assaults, and game level design.