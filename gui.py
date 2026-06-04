"""
Interface graphique pour le jeu d'échecs Magnus Carlsen.
Permet de jouer en mode joueur contre joueur ou contre l'ordinateur (MagnusBot).
"""
import os
import pygame
from position import Position
from board import Board
from player import AIPlayer
from specific_pieces import King, Queen, Bishop, Knight, Rook, Pawn

# Configuration de la fenêtre
WIDTH, HEIGHT = 1000, 640
SQ_SIZE = 640 // 8

# Couleurs du thème
LIGHT_COLOR = (235, 236, 224)     # Crème
DARK_COLOR = (119, 149, 86)       # Vert
SEL_COLOR = (186, 202, 68)        # Jaune sélection
HIGHLIGHT_DOT = (150, 160, 150)    # Points d'aide

# Couleurs du tableau de bord
DASHBOARD_BG = (38, 37, 34)       # Anthracite foncé
PANEL_BG = (49, 46, 43)           # Anthracite clair
BTN_DEFAULT = (69, 65, 60)         # Bouton par défaut
BTN_HOVER = (89, 85, 80)           # Bouton survolé
BTN_ACTIVE = (129, 182, 76)        # Vert actif
TEXT_LIGHT = (255, 255, 255)
TEXT_DIM = (180, 180, 180)
TEXT_GOLD = (243, 194, 69)

# Dictionnaire global pour stocker les images des pièces
IMAGES = {}


def load_images():
    """Charge les images des pièces depuis le dossier images/."""
    pieces = ["K", "Q", "B", "N", "R", "P"]
    colors = ["w", "b"]
    for color in colors:
        for p in pieces:
            name = f"{color}{p}"
            path = f"images/{name}.png"
            if os.path.exists(path):
                IMAGES[name] = pygame.image.load(path)


def get_valid_moves(board, start_pos) -> list:
    """Retourne la liste des positions de destination valides pour une pièce."""
    valid_dests = []
    piece = board.getPiece(start_pos)
    if piece is None:
        return valid_dests

    for col in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        for row in range(1, 9):
            dest = Position(col, row)
            if start_pos.column != dest.column or start_pos.row != dest.row:
                if piece.isValidMove(dest, board):
                    valid_dests.append(dest)
    return valid_dests


def draw_button(screen, font, rect, text, is_active, is_hovered):
    """Dessine un bouton interactif simple."""
    if is_active:
        bg_color = BTN_ACTIVE
    elif is_hovered:
        bg_color = BTN_HOVER
    else:
        bg_color = BTN_DEFAULT

    pygame.draw.rect(screen, bg_color, rect, border_radius=6)
    text_surf = font.render(text, True, TEXT_LIGHT)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)


def draw_board(screen, board, selected_pos, current_turn):
    """Dessine les cases, la pièce sélectionnée et les points d'aide."""
    # 1. Cases du plateau
    for r in range(8):
        for c in range(8):
            color = LIGHT_COLOR if (r + c) % 2 == 0 else DARK_COLOR
            pygame.draw.rect(screen, color, (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    # 2. Surlignage et coups autorisés
    if selected_pos is not None:
        c_idx = ord(selected_pos.column) - ord('a')
        r_idx = 8 - selected_pos.row
        pygame.draw.rect(screen, SEL_COLOR, (c_idx * SQ_SIZE, r_idx * SQ_SIZE, SQ_SIZE, SQ_SIZE), 4)

        valid_dests = get_valid_moves(board, selected_pos)
        for dest in valid_dests:
            c_d = ord(dest.column) - ord('a')
            r_d = 8 - dest.row
            center = (c_d * SQ_SIZE + SQ_SIZE // 2, r_d * SQ_SIZE + SQ_SIZE // 2)

            dest_piece = board.getPiece(dest)
            if dest_piece is not None:
                pygame.draw.circle(screen, HIGHLIGHT_DOT, center, SQ_SIZE // 2 - 8, 5)
            else:
                pygame.draw.circle(screen, HIGHLIGHT_DOT, center, 10)

    # 3. Affichage des pièces
    for pos_str, piece in board.grid.items():
        if piece is not None:
            col_char = pos_str[0]
            row_num = int(pos_str[1])
            c_idx = ord(col_char) - ord('a')
            r_idx = 8 - row_num

            name = f"{'w' if piece.color == 0 else 'b'}{str(piece)}"
            if name in IMAGES:
                screen.blit(IMAGES[name], (c_idx * SQ_SIZE, r_idx * SQ_SIZE))
            else:
                bg = (255, 255, 255) if piece.color == 0 else (40, 40, 40)
                txt = (0, 0, 0) if piece.color == 0 else (255, 255, 255)
                center = (c_idx * SQ_SIZE + SQ_SIZE // 2, r_idx * SQ_SIZE + SQ_SIZE // 2)
                pygame.draw.circle(screen, bg, center, SQ_SIZE // 2 - 8)
                font = pygame.font.SysFont("arial", 28, bold=True)
                surf = font.render(str(piece), True, txt)
                screen.blit(surf, surf.get_rect(center=center))


def save_game(board, current_turn, game_mode, filename="sauvegarde.json"):
    """Sauvegarde la partie au format JSON compatible."""
    import json
    w_is_ai = False
    b_is_ai = (game_mode == "vs_ai")
    state = {
        "players": [
            {"name": "Joueur Blanc", "color": 0, "is_ai": w_is_ai},
            {"name": "MagnusBot" if b_is_ai else "Joueur Noir", "color": 1, "is_ai": b_is_ai}
        ],
        "currentPlayerIndex": current_turn,
        "board": {
            pos_str: {"type": str(piece), "color": piece.color}
            for pos_str, piece in board.grid.items() if piece is not None
        }
    }
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erreur de sauvegarde : {e}")
        return False


def load_game(board, filename="sauvegarde.json"):
    """Charge la partie depuis un fichier JSON."""
    import json
    if not os.path.exists(filename):
        return None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            state = json.load(f)

        board.grid.clear()
        for col_char in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            for row in range(1, 9):
                board.grid[f"{col_char}{row}"] = None

        from specific_pieces import King, Queen, Bishop, Knight, Rook, Pawn
        piece_mapping = {
            "K": King,
            "Q": Queen,
            "B": Bishop,
            "N": Knight,
            "R": Rook,
            "P": Pawn
        }

        for pos_str, p_data in state["board"].items():
            col = pos_str[0]
            row = int(pos_str[1])
            pos = Position(col, row)
            piece_class = piece_mapping[p_data["type"]]
            board.grid[pos_str] = piece_class(pos, p_data["color"])

        current_turn = state["currentPlayerIndex"]
        b_is_ai = state["players"][1]["is_ai"]
        game_mode = "vs_ai" if b_is_ai else "vs_human"

        return current_turn, game_mode
    except Exception as e:
        print(f"Erreur de chargement : {e}")
        return None


def main():
    """Initialise et lance l'affichage graphique simplifié."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Échecs - Magnus Carlsen")
    clock = pygame.time.Clock()

    load_images()
    board = Board()
    ai_player = AIPlayer("MagnusBot", 1)

    selected_pos = None
    current_turn = 0  # 0: Blancs, 1: Noirs
    game_mode = "vs_human"  # "vs_human" ou "vs_ai"
    ai_delay_timer = None
    status_msg = ""

    # Polices de texte
    btn_font = pygame.font.SysFont("arial", 14, bold=True)
    title_font = pygame.font.SysFont("arial", 22, bold=True)

    # Coordonnées des boutons
    R_VS_HUMAN = pygame.Rect(660, 150, 315, 40)
    R_VS_AI = pygame.Rect(660, 200, 315, 40)
    R_SAVE = pygame.Rect(660, 260, 315, 40)
    R_LOAD = pygame.Rect(660, 310, 315, 40)
    R_RESTART = pygame.Rect(660, 380, 315, 40)
    R_QUIT = pygame.Rect(660, 430, 315, 40)

    running = True

    while running:
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Clic sur le plateau
                    if mx < 640:
                        if game_mode == "vs_ai" and current_turn == 1:
                            continue

                        col_idx = mx // SQ_SIZE
                        row_idx = 8 - (my // SQ_SIZE)

                        if 0 <= col_idx < 8 and 1 <= row_idx <= 8:
                            clicked_pos = Position(chr(col_idx + ord('a')), row_idx)
                            piece = board.getPiece(clicked_pos)

                            if selected_pos is None:
                                if piece is not None and piece.color == current_turn:
                                    selected_pos = clicked_pos
                                    status_msg = ""
                            else:
                                if piece is not None and piece.color == current_turn:
                                    selected_pos = clicked_pos
                                    status_msg = ""
                                else:
                                    active_piece = board.getPiece(selected_pos)
                                    if active_piece is not None and active_piece.isValidMove(clicked_pos, board):
                                        board.movePiece(selected_pos, clicked_pos)
                                        current_turn = 1 - current_turn
                                        status_msg = ""
                                        if game_mode == "vs_ai" and current_turn == 1:
                                            ai_delay_timer = pygame.time.get_ticks() + 800
                                    selected_pos = None

                    # Clic sur le panneau de configuration à droite
                    else:
                        if R_VS_HUMAN.collidepoint(mx, my):
                            game_mode = "vs_human"
                            status_msg = "Mode VS Humain activé."
                        elif R_VS_AI.collidepoint(mx, my):
                            game_mode = "vs_ai"
                            status_msg = "Mode VS Ordinateur activé."
                            if current_turn == 1:
                                ai_delay_timer = pygame.time.get_ticks() + 800
                        elif R_SAVE.collidepoint(mx, my):
                            if save_game(board, current_turn, game_mode):
                                status_msg = "Partie sauvegardée !"
                            else:
                                status_msg = "Erreur de sauvegarde."
                        elif R_LOAD.collidepoint(mx, my):
                            res = load_game(board)
                            if res is not None:
                                current_turn, game_mode = res
                                selected_pos = None
                                ai_delay_timer = None
                                status_msg = "Partie rechargée !"
                            else:
                                status_msg = "Aucune sauvegarde trouvée."
                        elif R_RESTART.collidepoint(mx, my):
                            board = Board()
                            selected_pos = None
                            current_turn = 0
                            ai_delay_timer = None
                            status_msg = "Partie réinitialisée."
                        elif R_QUIT.collidepoint(mx, my):
                            running = False

        # Gestion de l'action de l'IA
        if game_mode == "vs_ai" and current_turn == 1:
            if ai_delay_timer is not None and pygame.time.get_ticks() >= ai_delay_timer:
                ai_delay_timer = None
                move_str = ai_player.askMove(board)

                if len(move_str) == 7 and move_str[3] == ' ':
                    s_col, s_row = move_str[1], int(move_str[2])
                    e_col, e_row = move_str[5], int(move_str[6])

                    s_pos = Position(s_col, s_row)
                    e_pos = Position(e_col, e_row)

                    active_piece = board.getPiece(s_pos)
                    if active_piece is not None and active_piece.isValidMove(e_pos, board):
                        board.movePiece(s_pos, e_pos)
                    current_turn = 0

        # Rendu graphique
        screen.fill(DASHBOARD_BG)
        draw_board(screen, board, selected_pos, current_turn)

        # Panneau latéral droit
        pygame.draw.rect(screen, PANEL_BG, (650, 10, 340, 620), border_radius=8)

        # Titre
        title_surf = title_font.render("JOUER AUX ÉCHECS", True, TEXT_GOLD)
        title_rect = title_surf.get_rect(center=(820, 60))
        screen.blit(title_surf, title_rect)

        # Indicateur de tour
        turn_str = "Tour : Blancs" if current_turn == 0 else "Tour : Noirs"
        turn_surf = btn_font.render(turn_str, True, TEXT_LIGHT)
        turn_rect = turn_surf.get_rect(center=(820, 110))
        screen.blit(turn_surf, turn_rect)

        # Dessin des boutons de choix de mode
        draw_button(screen, btn_font, R_VS_HUMAN, "VS HUMAIN", game_mode == "vs_human", R_VS_HUMAN.collidepoint(mx, my))
        draw_button(screen, btn_font, R_VS_AI, "VS ORDI (IA)", game_mode == "vs_ai", R_VS_AI.collidepoint(mx, my))

        # Dessin des boutons de sauvegarde / chargement
        draw_button(screen, btn_font, R_SAVE, "SAUVEGARDER LA PARTIE", False, R_SAVE.collidepoint(mx, my))
        draw_button(screen, btn_font, R_LOAD, "CHARGER LA PARTIE", False, R_LOAD.collidepoint(mx, my))

        # Dessin des boutons d'actions générales
        draw_button(screen, btn_font, R_RESTART, "RECOMMENCER LA PARTIE", False, R_RESTART.collidepoint(mx, my))
        draw_button(screen, btn_font, R_QUIT, "QUITTER", False, R_QUIT.collidepoint(mx, my))

        # Message de statut
        if status_msg:
            status_surf = btn_font.render(status_msg, True, TEXT_GOLD)
            status_rect = status_surf.get_rect(center=(820, 520))
            screen.blit(status_surf, status_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
