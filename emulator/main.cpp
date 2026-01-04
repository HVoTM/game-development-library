#include <chrono>
#include <iostream>
#include "Chip8.hpp"
#include "Platform.hpp"

/**
 * Main Loop that will call Chip8::Cycle() function continuously until exit
 * 3 command-line arguments:
 * - Scale: The CHIP-8 video buffer is only 64x32, so we’ll need an integer scale factor 
 * to be able to play on our big modern monitors.
 * - Delay: The CHIP-8 had no specified clock speed, so we’ll use a delay to determine the time 
 * in milliseconds between cycles. Different games run best at different speeds, so we can control it here.
 * - ROM: The ROM file to load.
 */
int main(int argc, char** argv)
{
    if (argc != 4)
	{
		std::cerr << "Usage: " << argv[0] << " <Scale> <Delay> <ROM>\n";
		std::exit(EXIT_FAILURE);
	}

	int videoScale = std::stoi(argv[1]);
	int cycleDelay = std::stoi(argv[2]);
	char const* romFilename = argv[3];

	Platform platform("CHIP-8 Emulator", VIDEO_WIDTH * videoScale, VIDEO_HEIGHT * videoScale, VIDEO_WIDTH, VIDEO_HEIGHT);

	Chip8 chip8;
	chip8.LoadROM(romFilename);

	int videoPitch = sizeof(chip8.video[0]) * VIDEO_WIDTH;

	auto lastCycleTime = std::chrono::high_resolution_clock::now();
	bool quit = false;

	while (!quit)
	{
		quit = platform.ProcessInput(chip8.keypad);

		auto currentTime = std::chrono::high_resolution_clock::now();
		float dt = std::chrono::duration<float, std::chrono::milliseconds::period>(currentTime - lastCycleTime).count();

		if (dt > cycleDelay)
		{
			lastCycleTime = currentTime;

			chip8.Cycle();

			platform.Update(chip8.video, videoPitch);
		}
	}

	return 0;

}