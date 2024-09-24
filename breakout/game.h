#ifndef GAME_H
#define GAME_H

#include <glad/glad.h>
#include <GLFW/glfw3.h>

/*
---------------------------------------------------------
GameState
This allows us to keep track of what state the game is currently in. 
This way, we can decide to adjust rendering and/or processing based on the
current state of the game (we probably render and process different items when
we're in the game's menu for example).
---------------------------------------------------------
*/
// Represents the current state of the game
enum GameState {
    GAME_ACTIVE,
    GAME_MENU,
    GAME_WIN
};

// Game holds all game-related state and functionality.
// Combines all game-related data into a single class for
// easy access to each of the components and manageability.
class Game
{
public:
    // game state
    GameState               State;	
    bool                    Keys[1024];
    unsigned int            Width, Height;

    // constructor/destructor
    Game(unsigned int width, unsigned int height);
    ~Game();
    // initialize game state (load all shaders/textures/levels)
    void Init();
    // game loop
    void ProcessInput(float dt);
    void Update(float dt);
    void Render();
};

#endif