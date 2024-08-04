#ifndef _BOARD_ // reminder: ifndef checks whether a macro is not defined
#define _BOARD_

// library import
#include "Pieces.h"

#define BOARD_LINE_WIDTH 6          // width of the lines that delimit, surrounding perimeter
#define BLOCK_SIZE 16               // width and height of each block of a piece
#define BOARD_POSITION 320          // center pos of the board from the left of the screen
#define BOARD_WIDTH 10              // board width in blocks
#define BOARD_HEIGHT 20             // board height in blocks 
#define MIN_VERTICAL_MARGIN 20      // minimum vertical margin for the board limit
#define MIN_HORIZONTAL_MARGIN 20    // minimum horizontal margin for the board limit
#define PIECE_BLOCKS 5

// -------------------------------------------------------------------
// BOARD DEFINITION
// -------------------------------------------------------------------

class Board
{
public:

    Board(Pieces *pPieces, int pScreenHeight);

    int getXPosinPixels             (int pPos);
    int getYPosinPixels             (int pPos);
    bool isFreeBlock                (int pX, int pY);
    bool isPossibleMovement         (int pX, int pY, int pPiece, int pRotation);
    void StorePiece                 (int pX, int pY, int pPiece, int pRotation);
    void DeletePossibleLines        ();
    bool GameOver                   ();

private:
    /*
    Remind: enum is a special type that represents a group of constants (unchangeable values)
    By default, the first item has value 0, the second has 1, and so on
    So POS_FREE = 0, POS_FILLED = 1

    You can indicate the value when first defining an enum object
    */
    enum { POS_FREE, POS_FILLED };			// POS_FREE = free position of the board; POS_FILLED = filled position of the board
	int mBoard [BOARD_WIDTH][BOARD_HEIGHT];	// Board that contains the pieces
	Pieces *mPieces;
	int mScreenHeight;

	void InitBoard();
	void DeleteLine (int pY); 
};

#endif