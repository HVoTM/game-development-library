/*
REMINDER TO SELF:
these headers are called include guards. 

Once the header is included, it checks if a unique value (in this case _PIECES_) is defined. Then if it's not defined, it defines it and continues to the rest of the page.

When the code is included again, the first ifndef fails, resulting in a blank file.

That prevents double declaration of any identifiers such as types, enums and static variables.
*/
#ifndef _PIECES_
#define _PIECES_

// ——————————————————————————–
// Pieces
// ——————————————————————————–

class Pieces
{
    public:
    // 3 dots under variable name to indicate refactoring code for readability
	int GetBlockType        (int pPiece, int pRotation, int pX, int pY);
	int GetXInitialPosition (int pPiece, int pRotation);
	int GetYInitialPosition (int pPiece, int pRotation);
};

#endif // _PIECES_