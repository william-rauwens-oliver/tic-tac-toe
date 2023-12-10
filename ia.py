import random

def ia(board, signe, difficulty):
    flat_board = [element for row in board for element in row]

    if difficulty == "facile":
        return jouer_aleatoire(flat_board)
    elif difficulty == "moyen":
        return jouer_moyen(flat_board, signe)
    elif difficulty == "difficile":
        return jouer_difficile(flat_board, signe)
    else:
        raise ValueError("Niveau de difficulté non valide")

def jouer_aleatoire(board):
    # Joue un coup aléatoire
    empty_cells = [i for i, cell in enumerate(board) if cell == 0]
    return random.choice(empty_cells) if empty_cells else None

def jouer_moyen(board, signe):
    # Si l'IA peut gagner, l'IA joue pour gagner
    player = 1 if signe == 'X' else 2
    for i in range(9):
        if board[i] == 0:
            board[i] = player
            if est_victoire(board, player):
                return i
            board[i] = 0

    # Si l'adversaire peut gagner, l'IA joue pour bloquer
    opponent = 2 if player == 1 else 1
    for i in range(9):
        if board[i] == 0:
            board[i] = opponent
            if est_victoire(board, opponent):
                board[i] = player
                return i
            board[i] = 0

    return jouer_aleatoire(board)

def jouer_difficile(board, signe):
    # L'IA difficile joue pour gagner à chaque fois
    player = 1 if signe == 'X' else 2
    for i in range(9):
        if board[i] == 0:
            board[i] = player
            if est_victoire(board, player):
                return i
            board[i] = 0

    # Si l'adversaire peut gagner, l'IA joue pour bloquer
    opponent = 2 if player == 1 else 1
    for i in range(9):
        if board[i] == 0:
            board[i] = opponent
            if est_victoire(board, opponent):
                board[i] = player
                return i
            board[i] = 0

    # Si aucun joueur ne peut gagner immédiatement, l'IA joue de manière stratégique
    strategic_moves = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    for move in strategic_moves:
        if board[move] == 0:
            return move
        
    return jouer_aleatoire(board)

def est_victoire(board, player):
    for i in range(3):
        if all(board[i*3 + j] == player for j in range(3)) or \
           all(board[i + j*3] == player for j in range(3)):
            return True
    if all(board[i*3 + i] == player for i in range(3)) or \
       all(board[i*3 + 2 - i] == player for i in range(3)):
        return True
    return False