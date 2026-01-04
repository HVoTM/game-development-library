#pragma once

#include <cstdint>
#include <SDL.h>
#include <glad/glad.h>

class Platform
{
public:
    Platform(char const* title, int windowWidth, int windowHeight, int textureWidth, int textureHeight);
    ~Platform(); // destructor
    void Update(void const* buffer, int pitch);
	bool ProcessInput(uint8_t* keys);

private:
    SDL_Window* window{};
    // SDL Renderer to give 2D GPU acceleration
    SDL_Renderer* renderer{};
    // Render 2D Image
    SDL_Texture* texture{};

    SDL_GLContext gl_context{};
	GLuint framebuffer_texture;

};
