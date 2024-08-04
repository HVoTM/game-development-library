/*
=========================================================
Implement a class for Game, which will initialize the game, draw the board and pieces

by drawing each block as a rectangle and creates new random falling pieces
*/
#ifndef _GAME_
#define _GAME_
// --- Include ---
#include "Board.h"
#include "Pieces.h"
#include "IO.h"
#include <time.h>

#define WAIT_TIME 700 // Numebr of milliseconds that the piece remains before going 1 block down

// ---------------------------------------------------------
// GAME
// ---------------------------------------------------------

class Game
{
    public:
        // constructor
        Game (Board *pBoard, Pieces *pPieces, IO *pIO, int pScreenHeightl);

        void DrawScene          ();
        void CreateNewPiece     ();

        int mPosX, mPosY;  // Position of the Piece that is falling down
        int mPiece, mRotation;

    private:
        int mScreenHeight; // Screen height in pixels
        int mNextPosX, mNextPosY; //Position of the next piece
        int mNextPiece, mNextRotation; // kind of rotation of the next piece

        Board *mBoard;
        Pieces *mPieces;
        IO *mIO;

        int GetRand             (int pA, int pB);
        void InitGame           ();
        void DrawPiece          (int pX, int pY, int pPiece, int pRotation);
        void DrawBoard          ();
};

#endif // _GAME_