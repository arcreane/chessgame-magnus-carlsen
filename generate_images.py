import os
import pygame


def generate_default_images():
  
    os.makedirs("images", exist_ok=True)
    pygame.init()

    size = 80
    
    font = pygame.font.SysFont("arial", 42, bold=True)

    
    pieces = ["K", "Q", "B", "N", "R", "P"]
    colors = [
        ("w", (245, 245, 245), (40, 40, 40)),  
        ("b", (50, 50, 50), (245, 245, 245))   
    ]

    for prefix, bg_color, text_color in colors:
        for piece in pieces:
            
            surface = pygame.Surface((size, size), pygame.SRCALPHA)

            
            pygame.draw.circle(surface, bg_color, (size // 2, size // 2), size // 2 - 6)
            
            pygame.draw.circle(surface, text_color, (size // 2, size // 2), size // 2 - 6, 3)

            
            text_surf = font.render(piece, True, text_color)
            text_rect = text_surf.get_rect(center=(size // 2, size // 2))
            surface.blit(text_surf, text_rect)

           
            pygame.image.save(surface, f"images/{prefix}{piece}.png")

    pygame.quit()


if __name__ == "__main__":
    generate_default_images()
    print("Les 12 images de pièces ont été générées avec succès dans 'images/'.")
