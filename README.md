# game-development-library
 my own personal game dev experience, where I document everything game-related

## Concepts
- Game Design
- Game Graphics, Graphics Programming
- Game AI

# Ideas
- Chess
- Tic-tac-toe
- Snake
- Pong
- Gymansium project for applying reinforcement learning to make an AI agent: https://gymnasium.farama.org/
- Ragdoll physics
- Lighting and textures on simple 3D objects conceptual understanding
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

### Conclusion:
Game development integrates a variety of algorithms, each optimized for a specific aspect of the gaming experience. From AI to pathfinding, physics to rendering, and procedural generation to network optimization, these algorithms work together to create engaging, immersive, and high-performance games.
# Game Graphics
- [] 3D, geometry, and tons more Knowledge needed as well
OpenGL
https://www.khronos.org/opengl/wiki/Getting_Started
LearnOpenGL
https://learnopengl.com/
