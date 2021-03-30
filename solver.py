# Date: 3/28/21
# Desc: This program solves sliding puzzles by making every possible move then reporting back the solution to the puzzle


import sys
import copy # Allows me to make deep copies.

class Node:
    
    def __init__( self, grid, freeSpaceLoc, stepsLst ):
        self.grid = grid
        self.freeSpaceLoc = freeSpaceLoc
        self.stepsLst = stepsLst


    def printGrid(self ):
        
        for row in self.grid:
            for el in row:
                print( f" { el } ", end="" )
            print( )
        print()




def check( node ):
    num = [ num for num in range( 1, 10) ]
    index = 0
    for row in node.grid:
        for el in row:
            if num[ index ] == el:
                index += 1
            else:
                return False
    return True



def solve( grid, freespace ):
    lst = []

    seenConfigs = []


    freeSpaceValue = grid[ freespace[ 0 ] ][ freespace[ 1 ] ]
    lst.append( Node( grid, freespace, [] ) )


    while len( lst ) > 0:
        config = lst[0]
        lst.remove( config )

        if check( config ):
            print( "====" * 15, "\nPUZZLE SOLVED!" )
            
            config.printGrid()
            
            for step in config.stepsLst:
                print( step )
            break

        row = config.freeSpaceLoc[ 0 ]
        col = config.freeSpaceLoc[ 1 ]

        if row - 1 >= 0:
            topNode = Node( copy.deepcopy( config.grid ), ( row - 1, col), copy.deepcopy( config.stepsLst ) )
            topNode.stepsLst.append( f"Switched ({ row }, { col }) with ({row - 1}, {col})" )

            topNode.grid[row][col] = topNode.grid[row - 1][col]
            topNode.grid[row - 1][col] = freeSpaceValue


            if topNode.grid not in seenConfigs:
                lst.append( topNode )
                seenConfigs.append( topNode.grid )
            

        if row + 1 < 3:
            bottomNode = Node( copy.deepcopy( config.grid ), ( row + 1, col), copy.deepcopy( config.stepsLst ) )
            bottomNode.stepsLst.append( f"Switched ({ row }, { col }) with ({row + 1}, {col})" )

            bottomNode.grid[row][col] = bottomNode.grid[row + 1][col]
            bottomNode.grid[row + 1][col] = freeSpaceValue

            if bottomNode.grid not in seenConfigs:
                lst.append( bottomNode )
                seenConfigs.append( bottomNode.grid )


        
        if col - 1 >= 0:
            leftNode = Node( copy.deepcopy( config.grid ), ( row, col - 1), copy.deepcopy( config.stepsLst ) )
            leftNode.stepsLst.append( f"Switched ({ row }, { col }) with ({row}, {col - 1})" )

            leftNode.grid[row][col] = leftNode.grid[ row ][ col - 1]
            leftNode.grid[row][col - 1] = freeSpaceValue

            if leftNode.grid not in seenConfigs:
                lst.append( leftNode )
                seenConfigs.append( leftNode.grid )


        if col + 1 < 3:
            rightNode = Node( copy.deepcopy( config.grid ), ( row, col + 1), copy.deepcopy( config.stepsLst ) )
            rightNode.stepsLst.append( f"Switched ({ row }, { col }) with ({row}, {col + 1})" )

            rightNode.grid[row][col] = rightNode.grid[ row ][ col + 1]
            rightNode.grid[row][col + 1] = freeSpaceValue

            if rightNode.grid not in seenConfigs:
                lst.append( rightNode )
                seenConfigs.append( rightNode.grid )

def main():

    detective = [
                    [4, 2, 6],
                    [1, 3, 9],
                    [7, 8, 5]
                ]

    solve( detective, (1, 1) )



if __name__ == "__main__":
    main()
