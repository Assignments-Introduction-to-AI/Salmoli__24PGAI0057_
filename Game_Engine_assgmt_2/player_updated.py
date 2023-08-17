# import game_rules, random
# ###########################################################################
# # Explanation of the types:
# # The board is represented by a row-major 2D list of characters, 0 indexed
# # A point is a tuple of (int, int) representing (row, column)
# # A move is a tuple of (point, point) representing (origin, destination)
# # A jump is a move of length 2
# ###########################################################################

# # I will treat these like constants even though they aren't
# # Also, these values obviously are not real infinity, but close enough for this purpose
# NEG_INF = -1000000000
# POS_INF = 1000000000

# class Player(object):
#     """ This is the player interface that is consumed by the GameManager. """
#     def __init__(self, symbol): self.symbol = symbol # 'x' or 'o'

#     def __str__(self): return str(type(self))

#     def selectInitialX(self, board): return (0, 0)
#     def selectInitialO(self, board): pass

#     def getMove(self, board): pass

#     def h1(self, board):
#         return -len(game_rules.getLegalMoves(board, 'o' if self.symbol == 'x' else 'x'))


# # This class has been replaced with the code for a deterministic player.
# class MinimaxPlayer(Player):
#     def __init__(self, symbol, depth): super(MinimaxPlayer, self).__init__(symbol)

#     # Leave these two functions alone.
#     def selectInitialX(self, board): return (0,0)
#     def selectInitialO(self, board):
#         validMoves = game_rules.getFirstMovesForO(board)
#         return list(validMoves)[0]

    
#     # getWinner returns X,0,None
#     def getMove(self, board):
#         move, val = self.minmax(board, self.symbol, self.depth) ''' call minimax() here'''
#         return move
    
#     '''minimax() takes the state of the board, current turn and returns the best move along with its value'''
    
#     # Edit this one here. :)
#     def minmax(self, board, turn, depth):
#         """ Args: self [player], board[list of [list of 'x','o','']] 
#             Returns: best_move [move], best_val [int]
            
#             Recursion ends when the depth is equal to 0 or there are no more possible moves
#             For each possible move, make recursive call on updated board, opposite turn symbol, and depth -1
#                 If turn == self.symbol, it is a maximizing turn -> set best_val = max(best_val, next_val)
#                 If turn != self.symbol, it is a minimizing turn -> set best_val = min(best_val, next_val) 
                
#             """

#         legalMoves = game_rules.getLegalMoves(board, turn)
        
#         if depth <= 0 or len(legalMoves) < 1:
#             return None, self.h1(board, turn)

#         best_move = None
#         if turn == self.symbol:
#             best_val = '''+infinity'''
#         else:
#             best_val = '''-infinity'''

#         for move in legalMoves:
#             next_board = game_rules.makeMove(board, move)
            
#             m, next_val = self.minmax(next_board, 'o' if turn == 'x' else 'x', depth-1)
            
#             if '''condition1''':
#                 '''update best_move and  best_val'''
#             elif '''condition2''':
#                 '''update best_move and  best_val'''

#         return best_move, best_val



# # This class has been replaced with the code for a deterministic player.
# class AlphaBetaPlayer(Player):
#     def __init__(self, symbol, depth): super(AlphaBetaPlayer, self).__init__(symbol)

#     # Leave these two functions alone.
#     def selectInitialX(self, board): return (0,0)
#     def selectInitialO(self, board):
#         validMoves = game_rules.getFirstMovesForO(board)
#         return list(validMoves)[0]

    
#     def getMove(self, board):
#         move, val = self.ab_max(board, self.symbol, NEG_INF, POS_INF, self.depth)'''call ab_max() here which eventually calls ab_min() in a loop '''
#         return move

#     # Edit this one here. :)
   
#     def ab_max(self, board, turn, alpha, beta, depth):
#         """ Args: self [player], board [list of [list of 'x','o','']], turn [string 'x' or 'o'], alpha [int], beta [int], depth[int]
#             Returns: best_move [move], opt [int]
            
#             Recursion ends when the depth is equal to 0 or there are no more possible moves"""
        
#         legal_moves = game_rules.getLegalMoves(board, turn)
        
#         if depth <= 0 or len(legal_moves) < 1:
#             return None, self.h1(board, turn)

#         opt = '''-infinity'''
        
#         for move in legal_moves:
#             next_board = game_rules.makeMove(board, move)
#             m, val = self.ab_min(next_board, 'o' if turn == 'x' else 'x', alpha, beta, depth-1) '''call ab_min() here'''
            
#             '''update best move, best value, and alpha according to the rules'''
            
#         return best_move, opt

#     def ab_min(self, board, turn, alpha, beta, depth):
        
#         legal_moves = game_rules.getLegalMoves(board, turn)
        
#         if depth <= 0 or len(legal_moves) < 1:
#             return None, self.h1(board, turn)
        
#         opt = '''+infinity'''
        
#         for move in legal_moves:
#             next_board = game_rules.makeMove(board, move)
#             m, val = self.ab_max(next_board, 'o' if turn == 'x' else 'x', alpha, beta, depth-1)'''call ab_max() here'''
            
#             '''update best move, best value, and beta according to the rules'''

#         return best_move, opt



# class RandomPlayer(Player):
#     def __init__(self, symbol):
#         super(RandomPlayer, self).__init__(symbol)

#     def selectInitialX(self, board):
#         validMoves = game_rules.getFirstMovesForX(board)
#         return random.choice(list(validMoves))

#     def selectInitialO(self, board):
#         validMoves = game_rules.getFirstMovesForO(board)
#         return random.choice(list(validMoves))

#     def getMove(self, board):
#         legalMoves = game_rules.getLegalMoves(board, self.symbol)
#         if len(legalMoves) > 0: return random.choice(legalMoves)
#         else: return None


# class DeterministicPlayer(Player):
#     def __init__(self, symbol): super(DeterministicPlayer, self).__init__(symbol)

#     def selectInitialX(self, board): return (0,0)
#     def selectInitialO(self, board):
#         validMoves = game_rules.getFirstMovesForO(board)
#         return list(validMoves)[0]

#     def getMove(self, board):
#         legalMoves = game_rules.getLegalMoves(board, self.symbol)
#         if len(legalMoves) > 0: return legalMoves[0]
#         else: return None


# class HumanPlayer(Player):
#     def __init__(self, symbol): super(HumanPlayer, self).__init__(symbol)
#     def selectInitialX(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
#     def selectInitialO(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
#     def getMove(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')


# def makePlayer(playerType, symbol, depth=1):
#     player = playerType[0].lower()
#     if player   == 'h': return HumanPlayer(symbol)
#     elif player == 'r': return RandomPlayer(symbol)
#     elif player == 'm': return MinimaxPlayer(symbol, depth)
#     elif player == 'a': return AlphaBetaPlayer(symbol, depth)
#     elif player == 'd': return DeterministicPlayer(symbol)
#     else: raise NotImplementedException('Unrecognized player type {}'.format(playerType))

# def callMoveFunction(player, board):
#     if game_rules.isInitialMove(board): return player.selectInitialX(board) if player.symbol == 'x' else player.selectInitialO(board)
#     else: return player.getMove(board)

class Player(object):
    """ This is the player interface that is consumed by the GameManager. """
    def __init__(self, symbol): self.symbol = symbol # 'x' or 'o'

    def __str__(self): return str(type(self))

    def selectInitialX(self, board): return (0, 0)
    def selectInitialO(self, board): pass

    def getMove(self, board): pass

    def h1(self, board):
        return -len(game_rules.getLegalMoves(board, 'o' if self.symbol == 'x' else 'x'))


# This class is the code for a deterministic player.
class MinimaxPlayer(Player):
    def __init__(self, symbol, depth):
        super(MinimaxPlayer, self).__init__(symbol)
        self.depth=depth

    # Leave these two functions alone.
    def selectInitialX(self, board): #return (0,0)
    # Changes made so that game starts from middle
        validMoves = game_rules.getFirstMovesForX(board)
        return list(validMoves)[0]
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]
    def getMove(self,board):
        return self.Max_Value(board,self.depth,self.symbol)[1]


    def Max_Value(self, board, depth, symbol):
        legalMoves = game_rules.getLegalMoves(board, symbol)
        if depth == 0 or len(legalMoves) == 0:
            return (self.h1(board), None)
        best = (NEG_INF, None)
        for i in range(len(legalMoves)):
            nextBoard = game_rules.makeMove(board, legalMoves[i])
            if symbol == 'x':
                val = self.Min_Value(nextBoard, depth - 1, 'o')[0]
            else:
                val = self.Min_Value(nextBoard, depth - 1, 'x')[0]
            if best[0] < val:
                best = (val, legalMoves[i])
        return best

    def Min_Value(self, board, depth, symbol):
        legalMoves = game_rules.getLegalMoves(board, symbol)
        if depth == 0 or len(legalMoves) == 0:
            return (self.h1(board), None)
        best = (POS_INF, None)
        for i in range(len(legalMoves)):
            nextBoard = game_rules.makeMove(board, legalMoves[i])
            if symbol == 'x':
                val = self.Max_Value(nextBoard, depth - 1, 'o')[0]
            else:
                val = self.Max_Value(nextBoard, depth - 1, 'x')[0]
            if best[0] > val:
                best = (val, legalMoves[i])
        return best
    

# This class is the code for a deterministic player.
class AlphaBetaPlayer(Player):
    def __init__(self, symbol, depth):
        super(AlphaBetaPlayer, self).__init__(symbol)
        self.depth = depth

    # Leave these two functions alone.
    def selectInitialX(self, board): #return (0,0)
    # Changes made so that game starts from middle
        validMoves = game_rules.getFirstMovesForX(board)
        return list(validMoves)[0]
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def getMove(self, board):
        return self.AlphaBetaSearch(board)[1]
    def AlphaBetaSearch(self, board):
        return self.Max_Value(board, -1000000000, 1000000000, self.depth, self.symbol)

    def Max_Value(self, board, a, b, depth, symbol):
        # set initial max value to minus infinity
        #val = -1000000000
        # get legalmoves
        legalMoves = game_rules.getLegalMoves(board,symbol)
        best = (-1000000000, None)
        # return utility when no more legalmoves
        if (len(legalMoves) == 0 or depth == 0):
            return (self.h1(board), None)
        
        for i in range(len(legalMoves)):
            nextBoard = game_rules.makeMove(board, legalMoves[i])
            #nextBoard = game_rules.makeMove(board, legalMoves[i])
            # when meet depth limit, then use heuristic function to replace the val Min_Value
            if symbol == 'x':
                val = self.Min_Value(nextBoard, a, b, depth - 1, 'o')[0]
            else:
                val = self.Min_Value(nextBoard, a, b, depth - 1, 'x')[0]
            if best[0] < val:
               best = (val,legalMoves[i])
            if (best[0] >= b):
                return best
            if (a < best[0]):
                a = best[0]
        return best

    def Min_Value(self, board, a, b, depth, symbol):
        # set initial max value to minus infinity
        #val = 1000000000
        # get legalmoves
        legalMoves = game_rules.getLegalMoves(board, symbol)
        best = (1000000000, None)
        # return utility when no more legalmoves
        if (len(legalMoves) == 0 or depth == 0):
            return (self.h1(board), None)
        for i in range(len(legalMoves)):
            nextBoard = game_rules.makeMove(board, legalMoves[i])
            #nextBoard = game_rules.makeMove(board, legalMoves[i])
            # when meet depth limit, then use heuristic function to replace the val Min_Value
            if symbol == 'x':
                val = self.Max_Value(nextBoard, a, b, depth - 1, 'o')[0]
            else:
                val = self.Max_Value(nextBoard, a, b, depth - 1, 'x')[0]
            if best[0] > val:
                best = (val, legalMoves[i])
            if (best[0] <= a):
                return best
            if (b > best[0]):
                b = best[0]
        return best


class RandomPlayer(Player):
    def __init__(self, symbol):
        super(RandomPlayer, self).__init__(symbol)

    def selectInitialX(self, board):
        validMoves = game_rules.getFirstMovesForX(board)
        return random.choice(list(validMoves))

    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return random.choice(list(validMoves))

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return random.choice(legalMoves)
        else: return None


class DeterministicPlayer(Player):
    def __init__(self, symbol): super(DeterministicPlayer, self).__init__(symbol)

    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return legalMoves[0]
        else: return None


class HumanPlayer(Player):
    def __init__(self, symbol): super(HumanPlayer, self).__init__(symbol)
    def selectInitialX(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
    def selectInitialO(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
    def getMove(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')


def makePlayer(playerType, symbol, depth=1):
    player = playerType[0].lower()
    if player   == 'h': return HumanPlayer(symbol)
    elif player == 'r': return RandomPlayer(symbol)
    elif player == 'm': return MinimaxPlayer(symbol, depth)
    elif player == 'a': return AlphaBetaPlayer(symbol, depth)
    elif player == 'd': return DeterministicPlayer(symbol)
    else: raise NotImplementedException('Unrecognized player type {}'.format(playerType))

def callMoveFunction(player, board):
    if game_rules.isInitialMove(board): return player.selectInitialX(board) if player.symbol == 'x' else player.selectInitialO(board)
    else: return player.getMove(board)



