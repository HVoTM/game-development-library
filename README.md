# game-development-library
 my own personal game dev experience, where I document everything game-related

>> Game = A frame that continuously updates + Logic how the game works
---
> **NOTE**: *TO BE UPDATING...* after building some games that are playable, I will be writing up a website to contain all the available games for playing
## Concepts
- Game Design
- Game Graphics, Graphics Programming
- Game AI 
    - <span style="color:blue; background-color:yellow">Read this</span>: https://karpathy.github.io/2016/05/31/rl/

# Ideas
- Chess
- Tic-tac-toe
- Snake
- Pong
- Gymnasium project for applying reinforcement learning to make an AI agent: https://gymnasium.farama.org/
- Ragdoll physics
- Lighting and textures on simple 3D objects conceptual understanding
- Suika Game
- Sandtris (Tetris but sand particles, falling sand and such)
- A* Pathfinding
- Rope Simulation
- Collision Detection (AABB)
- Sorting Algorithm Visualization
- OpenGL
- RayCasting (Playing with Ray Tracing and stuff)
- Traveling Salesman Problem
- Particle Generator
    - Another similar is pseudo random generated circles -> added collisions for bouncing, resolution
- Terrain Generator
- Player movement 
- [Screen wrapping](https://en.wikipedia.org/wiki/Wraparound_(video_games)): where the player moves off on one side and reappears on the other, opposite side

# Concepts and theories
- Quantum game theory: https://en.wikipedia.org/wiki/Quantum_game_theory
    + Quantum tic-tac-toe

# Game Algorithms
Gaming relies on a variety of algorithms to provide immersive, interactive experiences. Here are some of the most common types of algorithms used in gaming:

### 1. **Pathfinding Algorithms**
Pathfinding algorithms are crucial in games for navigating characters or objects in a virtual world.

- **A* (A-star)**: The most popular pathfinding algorithm used in games. It combines the benefits of Dijkstra’s Algorithm (which finds the shortest path) with heuristics to prioritize paths that seem to lead toward the goal, improving efficiency.
  
  - **Applications**: Movement of non-player characters (NPCs), obstacle avoidance, and map exploration.
  
- **Dijkstra’s Algorithm**: Finds the shortest path between nodes in a graph. Often used when no heuristic is required or in simpler environments.

- **Breadth-First Search (BFS)**: Ensures the shortest path is found in an unweighted grid or graph but is not as efficient as A* in large search spaces.

### 2. **AI and Decision-Making Algorithms**
Game AI algorithms determine how NPCs and opponents behave and make decisions.

- **Finite State Machines (FSM)**: Used to model different states of a character and the transitions between them. For example, an enemy character could have states like "Patrol", "Chase", and "Attack".
  
- **Minimax Algorithm**: Used in games like chess and checkers for decision-making in turn-based games. It minimizes the possible loss for a worst-case scenario by simulating various moves and outcomes.
  
- **Monte Carlo Tree Search (MCTS)**: A more advanced decision-making algorithm used in games like Go and complex strategy games. It combines randomness and exploration to decide the most promising moves.

- **Behavior Trees**: An alternative to FSMs, behavior trees allow more complex AI behavior by organizing tasks in a tree structure and evaluating conditions dynamically.

### 3. **Procedural Generation Algorithms**
These algorithms are used to automatically generate content such as maps, levels, and even story elements.

- **Perlin Noise**: A gradient noise function often used to generate natural-looking terrain, textures, and cloud effects.
  
- **Simplex Noise**: A faster alternative to Perlin Noise, often used for similar procedural content generation, such as landscapes in Minecraft.
  
- **L-Systems**: A mathematical model used to procedurally generate complex branching structures like plants, trees, or fractals in games.

### 4. **Collision Detection Algorithms**
Collision detection ensures that game objects interact correctly (e.g., not passing through walls or each other).

- **Bounding Box (AABB)**: A simple and fast method that uses axis-aligned bounding boxes around objects to check if they intersect.
  
- **Separating Axis Theorem (SAT)**: A more complex algorithm that checks whether two convex shapes are colliding by projecting them onto a line and determining if there’s any overlap.

- **Ray Casting**: Projects rays from a point (such as the camera or a character) to detect collisions or line of sight. It’s used in shooting games for hit detection.

### 5. **Physics Algorithms**
Physics simulations make objects behave in realistic ways (e.g., gravity, forces, collisions).

- **Verlet Integration**: A method for simulating the motion of particles by calculating their velocity and position over time. It’s commonly used in cloth simulation and soft-body dynamics.

- **Ragdoll Physics**: A physics-based animation technique used for simulating characters' bodies falling or being hit realistically.

- **Rigid Body Dynamics**: Used to simulate the movement of objects that do not deform (e.g., a ball or a box). These algorithms handle forces, collisions, and constraints.

### 6. **Rendering Algorithms**
Rendering algorithms are responsible for generating the images you see on screen.

- **Rasterization**: Converts 3D models into a 2D image by breaking them into pixels or fragments. This is the foundation of real-time rendering in most video games.

- **Ray Tracing**: Simulates the behavior of light to produce more realistic images. It traces the path of rays of light as they interact with surfaces, allowing for realistic reflections, shadows, and lighting effects. Though historically expensive, modern GPUs and algorithms like NVIDIA's RTX have made real-time ray tracing more feasible.

- **Z-Buffering**: Manages the depth of objects in a 3D scene to determine which objects are in front and which are hidden, ensuring correct rendering.

### 7. **Compression and Optimization Algorithms**
Games often need to compress data to optimize performance and reduce file size.

- **Texture Compression (DXT, ASTC, etc.)**: Compresses textures (2D images used in 3D rendering) without losing much quality, enabling faster loading times and reduced memory usage.
  
- **Level of Detail (LOD)**: Dynamically reduces the complexity of a 3D model when it's far from the camera, improving performance without significantly affecting visual quality.

### 8. **Audio Algorithms**
These algorithms handle sound effects, music, and voiceovers.

- **Fast Fourier Transform (FFT)**: Used to analyze the frequency components of sounds. It’s crucial in games for real-time sound processing, such as equalizing or creating dynamic music systems.

- **Spatial Audio Algorithms**: Used to simulate 3D audio environments, where sounds seem to come from a specific direction and distance.

### 9. **Network Algorithms**
Online and multiplayer games use network algorithms to handle communication between players and servers.

- **Lag Compensation Algorithms**: These algorithms ensure smooth gameplay even with network latency by predicting the future state of objects or by rolling back actions based on late player inputs.

- **Dead Reckoning**: Predicts the future position of moving objects based on their current velocity and direction, reducing the number of position updates needed in multiplayer games.

- **Interpolation/Extrapolation**: Smooths the movement of objects or characters between updates from a server in a multiplayer game.

# Game Graphics
- [] 3D, geometry, and tons more Knowledge needed as well
OpenGL
https://www.khronos.org/opengl/wiki/Getting_Started
LearnOpenGL
https://learnopengl.com/

# Inspirations
- [One year of my C++ SFML journey](https://www.youtube.com/watch?v=XxBZw2FEdK0&ab_channel=Snapi)
- [Making a Game with C++ and SDL2](https://www.youtube.com/watch?v=cZkfnLtKcAc&t=201s&ab_channel=Goodgis)
- [Building a Physics Engine with C++ and Simulating Machines](https://youtu.be/TtgS-b191V0?si=pIYk_Kr5NRlS1Dvs)
- [Half-year progress: C++ with SFML](https://www.youtube.com/watch?v=TYzOSeK_qxM&ab_channel=lutrarutra)
- [2 Months of Learning Howto Code for Games with SFML/C++](https://www.youtube.com/watch?v=kbVn7Jdhl3Y&ab_channel=Kebab)
- [Clear Code] (https://www.youtube.com/@ClearCode) and [Coding with Russ](https://www.youtube.com/c/CodingWithRuss) are two great inspirers for introduction to game development

# Libraries & Resources
When learning **game development** and **simulation** using C++, several libraries can help you understand core concepts like rendering, physics, input handling, and more. Here are some of the most commonly used libraries:

### 1. **SFML (Simple and Fast Multimedia Library)**
  - **Purpose**: 2D game development.
  - **Features**: Provides a simple API for handling graphics, window management, input, audio, and networking.
  - **Why It's Great for Learning**: It's beginner-friendly and abstracts complex lower-level operations. Its API is more modern and simpler compared to SDL.
  - **Use Cases**: Ideal for 2D games, multimedia applications, and prototyping.
  - **Website**: [SFML](https://www.sfml-dev.org)

### 2. **SDL (Simple DirectMedia Layer)**
  - **Purpose**: 2D game development and multimedia handling.
  - **Features**: Provides low-level access to audio, keyboard, mouse, and 2D hardware acceleration via OpenGL or DirectX.
  - **Why It's Great for Learning**: It's widely used in the game development industry and gives good exposure to game engines like Unreal Engine or game consoles.
  - **Use Cases**: Developing 2D games, emulators, and more complex simulations.
  - **Website**: [SDL](https://www.libsdl.org)

### 3. **OpenGL**
  - **Purpose**: 2D/3D graphics rendering API.
  - **Features**: Cross-platform graphics API used for rendering 2D/3D vector graphics. Often paired with **GLFW** or **GLUT** for window and input handling.
  - **Why It's Great for Learning**: Teaches you how graphics rendering works at a lower level, which is useful for understanding game engines.
  - **Use Cases**: Graphics rendering for games, simulations, CAD software.
  - **Website**: [OpenGL](https://www.opengl.org)

### 4. **GLEW (OpenGL Extension Wrangler Library)**
    - **Purpose**: OpenGL extension handling.
  - **Features**: Helps manage OpenGL extensions across various platforms.
  - **Why It's Great for Learning**: Simplifies using modern OpenGL features, especially when learning to develop 3D games or simulations.
  - **Use Cases**: Games and applications requiring modern OpenGL features.
  - **Website**: [GLEW](http://glew.sourceforge.net)

### 5. **GLFW (Graphics Library Framework)**
  - **Purpose**: Window creation and input handling for OpenGL.
  - **Features**: Handles creating windows, OpenGL contexts, and processing input from keyboards, mice, and gamepads.
  - **Why It's Great for Learning**: Useful when paired with OpenGL to handle windows, input, and context management.
  - **Use Cases**: 3D game engines, rendering engines, and visualization software.
  - **Website**: [GLFW](https://www.glfw.org)

### 6. **Box2D**
  - **Purpose**: 2D physics simulation.
  - **Features**: A popular physics engine that simulates rigid body physics.
  - **Why It's Great for Learning**: Provides a simple and widely used physics engine that integrates well with 2D games. It’s great for learning how real-world physics can be applied to game mechanics.
  - **Use Cases**: 2D platformers, puzzle games, and physics simulations.
  - **Website**: [Box2D](https://box2d.org)

### 7. **Bullet Physics**
  - **Purpose**: 3D physics simulation.
  - **Features**: Real-time collision detection and rigid body dynamics, including support for soft body and fluid simulations.
  - **Why It's Great for Learning**: It's used in many professional-grade applications and teaches you how to implement 3D physics in games.
  - **Use Cases**: 3D games, VR simulations, robotics, and physics simulations.
  - **Website**: [Bullet Physics](https://pybullet.org)

### 8. **Assimp (Open Asset Import Library)**
  - **Purpose**: Model loading.
  - **Features**: Supports loading various 3D model formats (OBJ, FBX, COLLADA, etc.) into your application.
  - **Why It's Great for Learning**: If you’re working with 3D assets, this library allows you to load models into your game or simulation, which is a critical aspect of 3D game development.
  - **Use Cases**: 3D games, simulations, or applications needing complex model import functionality.
  - **Website**: [Assimp](https://github.com/assimp/assimp)

### 9. **ImGui (Immediate Mode GUI)**
  - **Purpose**: GUI creation for game tools and in-game overlays.
  - **Features**: Allows quick creation of GUIs with buttons, sliders, checkboxes, etc. It’s very lightweight and easy to integrate with rendering pipelines like OpenGL.
  - **Why It's Great for Learning**: Great for building development tools (level editors, debuggers) and for creating in-game HUDs.
  - **Use Cases**: In-game development tools, overlays, HUDs, and GUI-based applications.
  - **Website**: [ImGui](https://github.com/ocornut/imgui)

### 10. **EnTT**
  - **Purpose**: Entity-Component-System (ECS) library for game development.
  - **Features**: Lightweight and fast ECS implementation for managing game entities and components.
  - **Why It's Great for Learning**: ECS architecture is common in modern game engines (like Unity and Unreal), and EnTT provides a clean, simple way to understand how an ECS system works.
  - **Use Cases**: Entity management in games, real-time simulations, game engines.
  - **Website**: [EnTT](https://github.com/skypjack/entt)

### 11. **Ogre3D**
  - **Purpose**: 3D rendering engine.
  - **Features**: Offers a high-level interface for creating real-time 3D applications. Handles complex rendering tasks without needing low-level management.
  - **Why It's Great for Learning**: For more advanced learners, Ogre3D provides a higher-level abstraction for creating 3D scenes and rendering without dealing with raw OpenGL or Direct3D code.
  - **Use Cases**: 3D game engines, simulation tools, real-time rendering applications.
  - **Website**: [Ogre3D](https://www.ogre3d.org)

### 12. **Catch2**
  - **Purpose**: Unit testing framework.
  - **Features**: Simple, header-only unit testing framework for C++.
  - **Why It's Great for Learning**: Writing testable code is a key skill for game developers, and Catch2 allows you to easily write unit tests to validate game logic.
  - **Use Cases**: Testing game mechanics, physics interactions, and other critical logic.
  - **Website**: [Catch2](https://github.com/catchorg/Catch2)

### 13. **RakNet**
  - **Purpose**: Networking library for games.
  - **Features**: Provides a high-level API for handling multiplayer games over the network, with features like reliable UDP, object replication, and voice chat.
  - **Why It's Great for Learning**: Multiplayer programming is complex, and RakNet abstracts many common networking challenges for you, helping you focus on game logic.
  - **Use Cases**: Multiplayer games, networked simulations.
  - **Website**: [RakNet](https://github.com/OculusVR/RakNet)

---

### Choosing Libraries Based on Use Case:

- **2D Games**: 
  - SFML, SDL, Box2D, ImGui.
  
- **3D Games**: 
  - OpenGL, GLFW, Bullet Physics, Assimp, Ogre3D.

- **Physics Simulations**: 
  - Box2D (for 2D), Bullet (for 3D).

- **Real-time Simulations**:
  - OpenGL, Bullet Physics, EnTT, ImGui.

> NOTE: watch this Low Level Game Dev [video](https://www.youtube.com/watch?v=7qm4OR3EmnQ&ab_channel=LowLevelGameDev) to have a high-level abstract on how to start with game Dev
---
**Summary**: Start with learning C++ (The Cherno); SFML, OpenGL, ImGui for library to get fastened onto game dev; CMake for packaging and management later on if you are really passionate about making a commercial game!