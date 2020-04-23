

def minimax(state, depth=0, maximize=0):

    if possible_moves(state) == -1:
        return sum(state)

    if maximize:
        val = float("-inf")
        for move in possible_moves(state):
            return max( val, minimax(move, depth+1, 0) )

    else:
        val = float("-inf")
        for move in possible_moves(state):
            return min ( val, minimax(move,depth+1. 1) )
