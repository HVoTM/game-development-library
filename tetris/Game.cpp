// Define class Game with the corresponding defined attributes
#ifndef LINUX
#include <windows.h>
#endif
#include "Game.h"

/*
=================================================================
Constructor for class Game
=================================================================
*/
Game::Game(Board *pBoard, Pieces *pPieces, IO *pIO, int pScreenHeight)
{
    mScreenHeight = pScreenHeight;
    mBoard = pBoard;
    mPieces = pPieces;
    mIO = pIO;

    // Game initialization
    InitGame();
}

/*
=================================================================
GetRand() returns a random number between two boundaries

Parameters:
>> pA: first number
>> pB: second number
=================================================================
*/
int Game::GetRand(int pA, int pB)
{
    return rand() % (pB - pA + 1) + pA;
}

/*
=================================================================
InitGame () to initialize the parameters of the game
=================================================================
*/
void Game::InitGame()
{
    // Init random numbers
    srand ((unsigned int) time(NULL));

    // First piece
    mPiece = GetRand(0, 6); // choose betwene the 7 types
    mRotation = GetRand (0, 3);  // choose between 4 rotations
    mNextPosX = BOARD_WIDTH + 5;
    mNextPosY = 5;

    // Next piece
    mNextPiece = GetRand(0, 6);
    mNextRotation = GetRand(0, 3);
    mNextPosX = BOARD_WIDTH + 5;
    mNextPosY = 5;
}

/*
=================================================================
Create a random piece
=================================================================
*/
void Game::CreateNewPiece()
{
    // new piece
    mPiece = mNextPiece;
    mRotation = mNextRotation;
    mPosX = (BOARD_WIDTH / 2) + mPieces->GetXInitialPosition(mPiece, mRotation);
    mPosY = mPieces -> GetYInitialPosition (mPiece, mRotation);

    // Random next piece
    mNextPiece = GetRand (0, 6);
    mNextRotation = GetRand(0, 3);
}


/*
=================================================================
DrawPiece() : iterates through the piece matrix and draws each block of the piece

Parameters:
>> pX: Horizontal position in blocks
>> pY: Vertical position in blocks
>> pPiece: piece to draw
>> pRotation: 1 of the 4 possible rotations
=================================================================
*/

void Game::DrawPiece(int pX, int pY, int pPiece, int pRotation)
{
    color mColor; // color of the block

    // Obtain the position in pixel in the screne of the block we want to draw
    int mPixelsX = mBoard -> getXPosinPixels(pX);
    int mPixelsY = mBoard -> getYPosinPixels(pY);

    // Travel the matrix of the blocks of the piece and draw the blocks that are filled
    for (int i=0; i < PIECE_BLOCKS; i++)
    {
        for (int j=0; j < PIECE_BLOCKS; j++)
        {
            // Get the type of the block and draw it with the correct color
            switch (mPieces->GetBlockType (pPiece, pRotation, j, i))
            {
            case 1 /*constant-expression*/:
                mColor = GREEN; break;
            
            case 2:
                mColor = BLUE;  break;
            }

            if (mPieces->GetBlockType(pPiece, pRotation, j, i) != 0)
            mIO->DrawRectangle (mPixelsX + i * BLOCK_SIZE,
            mPixelsY + j * BLOCK_SIZE,
            (mPixelsX + i * BLOCK_SIZE) + BLOCK_SIZE - 1,
            (mPixelsY + j * BLOCK_SIZE) + BLOCK_SIZE - 1,
            mColor);
        }
    }
}

/*
=========================================================
DrawBoard() to draws the blue columns as the boundary of the boards. Then draws the board blocks that are flagged
as POS_FILLED in a nested loop
=========================================================
*/

void Game::DrawBoard()
{
    // Calculate the limits of the board in pixels
    int mX1 = BOARD_POSITION - (BLOCK_SIZE * (BOARD_WIDTH /2 )) -1;
    int mX2 = BOARD_POSITION + (BLOCK_SIZE * (BOARD_WIDTH /2 ));
    int mY = mScreenHeight - (BLOCK_SIZE * BOARD_HEIGHT);

    // Check that the vertical margin is not too small
    // assert (mY -> MIN_VERTICAL_MARGIN)

    // Rectangles that delimits the board
    mIO -> DrawRectangle(mX1 - BOARD_LINE_WIDTH, mY, mX1, mScreenHeight - 1, BLUE);
    mIO -> DrawRectangle(mX2, mY, mX2 + BOARD_LINE_WIDTH, mScreenHeight -1 , BLUE);

    // Check that the horizontal margin is not too small
    // assert (mX1 -> MIN_HORIZONTAL_MARGIN);

    // Drawing the blocks that are already stored in the board
    mX1 += 1;
    for (int i=0; i < BOARD_WIDTH; i++)
    {
        for (int j=0; j < BOARD_HEIGHT; j++)
        {
            // Check if the block is filled, if so, draw it
            if (!mBoard->isFreeBlock(i, j))
            mIO->DrawRectangle ( mX1 + i * BLOCK_SIZE,
            mY + j * BLOCK_SIZE,
            (mX1 + i * BLOCK_SIZE) + BLOCK_SIZE - 1,
            (mY + j * BLOCK_SIZE) + BLOCK_SIZE - 1,
            RED);
        }
    }
}

/*
======================================================
Draw Scene by calling all the previous methods 
======================================================
*/

void Game::DrawScene()
{
    DrawBoard ();
    DrawPiece (mPosX, mPosY, mPiece, mRotation);
    DrawPiece (mNextPosX, mNextPosY, mNextPiece, mNextRotation);
}