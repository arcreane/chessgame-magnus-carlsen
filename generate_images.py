import os
import pygame


def generate_default_images():
    """
    Génère 12 images de pièces d'échecs sous forme de fichiers PNG.
    Utile si les images externes sont manquantes.
    """
    os.makedirs("images", exist_ok=True)
    pygame.init()

    size = 80
    # Utilisation d'une police système standard
    font = pygame.font.SysFont("arial", 42, bold=True)

    # Définition des pièces et des couleurs (préfixe, couleur de fond, couleur de texte)
    pieces = ["K", "Q", "B", "N", "R", "P"]
    colors = [
        ("w", (245, 245, 245), (40, 40, 40)),  # Pièces blanches
        ("b", (50, 50, 50), (245, 245, 245))    # Pièces noires
    ]

    for prefix, bg_color, text_color in colors:
        for piece in pieces:
            # Créer une surface transparente
            surface = pygame.Surface((size, size), pygame.SRCALPHA)

            # Dessiner un disque pour représenter le jeton de la pièce
            pygame.draw.circle(surface, bg_color, (size // 2, size // 2), size // 2 - 6)
            # Dessiner le contour du disque
            pygame.draw.circle(surface, text_color, (size // 2, size // 2), size // 2 - 6, 3)

            # Rendre et centrer l'initiale de la pièce
            text_surf = font.render(piece, True, text_color)
            text_rect = text_surf.get_rect(center=(size // 2, size // 2))
            surface.blit(text_surf, text_rect)

            # Sauvegarder au format PNG dans le dossier images/
            pygame.image.save(surface, f"images/{prefix}{piece}.png")

    pygame.quit()


if __name__ == "__main__":
    generate_default_images()
    print("Les 12 images de pièces ont été générées avec succès dans 'images/'.")
