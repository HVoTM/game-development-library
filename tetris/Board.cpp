#include <Board.h>
#include <Pieces.h>

/*
========================================================================
A nested loop to Init the board blocks with free positions
========================================================================
*/
void Board::InitBoard(){
    for (int i=0; i < BOARD_WIDTH; i++)
    {
        for (int j=0;  j < BOARD_HEIGHT; j++)
        {
            mBoard[i][j] = POS_FREE;
        }
    }
}

/*
========================================================================
Store a Piece in the board by filling the appropriate blocks as POS_FILLED

Parameters:

>> pX: Horizontal position in blocks
>> pY: Vertical position in blocks
>> pPiece: Piece to draw
>> pRotation: 1 of the 4 possible rotations
========================================================================
*/

void Board::StorePiece(int pX, int pY, int pPiece, int pRotation){
    //store each block of the piece, which we have defined as a 5x5 matrix into the board
    for (int i1=pX, i2=0; i1 < pX + PIECE_BLOCKS; i1++, i2++)
    {
        for (int j1 = pY, j2=0; j1 < pY + PIECE_BLOCKS; j1++, j2++)
        {
            // Store only the blocks of the piece that are not holes
            if (mPieces -> GetBlockType(pPiece, pRotation, j2, i2) != 0)
            {
                mBoard[i1][j1]= POS_FILLED;
            }
        }
    }
}

/*
========================================================================
isGameOver checks if the game is over because a pieace have achieved the upper position

return True or False
========================================================================
*/
bool Board::GameOver()
{
    for (int i=0; i<BOARD_WIDTH; i++)
    {
        if (mBoard[i][0] == POS_FILLED) return true;
        
    }
    return false;
}   

/*
========================================================================
DeleteLine erases a line and moves all the blocks of upper position one row down.
Starting from the line that needs erasing, and then, iterating through the board in a nested loop and moves
all the blocks of the upper lines one row down

Parameters:
>> pY: Vertical position in blocks of the line to be deleted
========================================================================
*/
void Board::DeleteLine(int pY)
{
    // Move all the upper lines one row down
    for (int j=pY; j >0; j--)
    {
        for (int i=0; i < BOARD_WIDTH; i++)
        {
            mBoard[i][j] = mBoard[i][j-1];
        }
    }
}

/*
========================================================================
DeletePossibleLines() to remove all the lines that should be erased from the board.
Basically use this function for every loop to check every row, if all blocks are filled at that row, use DeleteLine 
========================================================================
*/

void Board::DeletePossibleLines()
{
    for (int j=0; j < BOARD_HEIGHT; j++)
    {
        int i = 0;
        while (i < BOARD_WIDTH)
        {
            if (mBoard[i][j] != POS_FILLED) break;
            i++;
        }

        if (i==BOARD_WIDTH) DeleteLine(j);
    }
}

/*
========================================================================
isFreeBlock is a trivial method that checks out if a board block is Filled or not

Returns 1 (true) if the block of the board is empty, 0 if it is filled

Parameters:
>> pX: Horizontal position in blocks
>> pY: vertical position in blocks
========================================================================
*/
bool Board::isFreeBlock(int pX, int pY)
{
    if(mBoard [pX][pY] == POS_FREE) return true; else return false;
}

// UP UNTIL NOW, IT IS JUST BOARD AND BLOCK LOGIC FUNCTION TO PERFORM
// WE WILL BE IMPLEMENTING FUNCTIONS TO SPECIFY THE POSITION IN PIXELS TO DRAW

/*
========================================================================
Returns the horizontal position (in pixels) of the block given like parameter

Parameters:
>> pPos: Horizontal position of the block in the board
========================================================================
*/
int Board::getXPosinPixels(int pPos)
{
    return ((BOARD_POSITION - (BLOCK_SIZE * (BOARD_WIDTH /2))) + (pPos * BLOCK_SIZE));
}

/*
========================================================================
Returns the vertical position (in pixels) of the block given like parameter

Parameters:
>> pPos: Vertical position of the block in the board
========================================================================
*/

int Board::getYPosinPixels(int pPos)
{
    return ((mScreenHeight - (BLOCK_SIZE * BOARD_HEIGHT)) + (pPos * BLOCK_SIZE));
}

/*
========================================================================
Checks if the piece can be stored at this position without any collision
Returns true if the movement is possible, false if not 

Parameters:
>> pX: Horizontal position in Blocks
>> pY: Vertical position in blocks
>> pPiece: Piece to draw
>> pRotation: 1 of the 4 possible rotations
========================================================================
*/

bool Board::isPossibleMovement(int pX, int pY, int pPiece, int pRotation)
{
    //Checks collision with pieces already stored in the board or the board limits
    // This is to check the 5x5 blocks of a piece with the appropriate area in the board
    for (int i1 = pX, i2 = 0; i1 < pX + PIECE_BLOCKS; i1++, i2++)
    {
        for (int j1 = pY, j2 = 0; j1 < pY + PIECE_BLOCKS; j1++, j2++)
        {
            // Check if the piece is outside the limits of the board
            if ( i1 < 0 || i1 > BOARD_WIDTH - 1 || j1 > BOARD_HEIGHT - 1)
            {
                if (mPieces->GetBlockType (pPiece, pRotation, j2, i2) != 0) return 0;
            }

            // Check if the piece have collisioned with a block already stored in the map
            if (j1 >= 0)
            {
                if ((mPieces->GetBlockType (pPiece, pRotation, j2, i2) != 0) && (!isFreeBlock(i1, j1)) ) return false;
            }
        }
    }
    // No collision
    return true;
}