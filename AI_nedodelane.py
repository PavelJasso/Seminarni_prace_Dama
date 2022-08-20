from copy import deepcopy
import pygame

class AI(stone):

    def ai_move(self, board):
        self.board = board

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def minimax(depth, position, game, max_player):
        if depth == 0 or position.winner() != None:
            return position.evaluate(), position
        if max_player:
            maxEvaluation = float('-inf')
            best_path = None
            for path in get_all_paths(position, WHITE, game):
                evaluation = minimax(path, depth-1, False, game)[0]
                maxEvaluation = max(maxEvaluation, evaluation)
                if maxEvaluation == evaluation:
                    best_path = path
            return maxEvaluation, best_path       
        else:
            minEvaluation = float('inf')
            best_path = None
            for path in get_all_paths(position, BLACK, game):
                evaluation = minimax(path, depth-1, True, game)[0]
                minEvaluation = min(minEvaluation, evaluation)
                if minEvaluation == evaluation:
                    best_path = path
            return minEvaluation, best_path     