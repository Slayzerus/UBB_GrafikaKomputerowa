import math
import pygame

window_size = (600, 600)
radius = 150
vertices_count = 5

pygame.init()

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pięciokąt foremny")
clock = pygame.time.Clock()

#color declarations
WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
VIOLET = (128, 0, 128)
LIGHT_BLUE = (0, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

center_x = window_size[0] // 2
center_y = window_size[1] // 2

original_vertices = [(center_x + int(radius * math.sin(2 * math.pi * i / vertices_count)),
                       center_y + int(radius * math.cos(2 * math.pi * i / vertices_count)))
                      for i in range(vertices_count)]

test = []
for i in range(vertices_count):
    x = center_x + int(radius * math.sin(2 * math.pi * i / vertices_count))
    y = center_y + int(radius * math.cos(2 * math.pi * i / vertices_count))
    test.append((x, y))
    print(x)
    print(y)




vertices = original_vertices.copy()
pressed_button = 1

def rotateVertices(verticesToRotate, angle):
    verticesToRotate = [(2 * x - center_x, 2 * y - center_y) for x, y in verticesToRotate]
    angleRad = math.radians(angle)
    verticesToRotate = [(int((x - center_x) * math.cos(angleRad) - (y - center_y) * math.sin(angleRad) + center_x),
                             int((x - center_x) * math.sin(angleRad) + (y - center_y) * math.cos(angleRad) + center_y))
                            for x, y in verticesToRotate]
    return verticesToRotate


angle = 0
display_polygon = True
button_number = None
font = pygame.font.Font(None, 36)
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                vertices = original_vertices.copy()
                display_polygon = True
                button_number = 1
            elif event.key == pygame.K_2:
                vertices = [(2 * x - center_x, 2 * y - center_y) for x, y in original_vertices]
                angle = math.radians(45)
                vertices = [(int((x - center_x) * math.cos(angle) - (y - center_y) * math.sin(angle) + center_x),
                             int((x - center_x) * math.sin(angle) + (y - center_y) * math.cos(angle) + center_y))
                            for x, y in vertices]
                display_polygon = True
                button_number = 2
            elif event.key == pygame.K_3:
                vertices = [(x, 2 * center_y - y) for x, y in original_vertices]
                vertices = [(x, int(2 * (y - center_y) + center_y)) for x, y in vertices]
                display_polygon = True
                button_number = 3
            elif event.key == pygame.K_4:
                shear_factor = 0.4
                vertices = [(x + shear_factor * y, y) for x, y in original_vertices]

                min_x = min(vertices, key=lambda point: point[0])[0]
                max_x = max(vertices, key=lambda point: point[0])[0]
                shift_x = (min_x + max_x) / 2 - center_x
                vertices = [(x - shift_x, y) for x, y in vertices]

                display_polygon = True
                button_number = 4
            elif event.key == pygame.K_5:
                scale_factor_x = 2
                scale_factor_y = 1
                translation_y = -158

                vertices = [(scale_factor_x * x, scale_factor_y * y) for x, y in original_vertices]

                vertices = [(x, y + translation_y) for x, y in vertices]

                min_x = min(vertices, key=lambda point: point[0])[0]
                max_x = max(vertices, key=lambda point: point[0])[0]
                shift_x = (min_x + max_x) / 2 - center_x
                vertices = [(x - shift_x, y) for x, y in vertices]

                display_polygon = True
                button_number = 5
            elif event.key == pygame.K_6:
                shear_factor_y = -0.4
                angle_rotation = 0

                vertices = [(x, x * shear_factor_y + y) for x, y in original_vertices]

                angle_rad = math.radians(angle_rotation)
                vertices = [(int((x - center_x) * math.cos(angle_rad) - (y - center_y) * math.sin(angle_rad) + center_x),
                             int((x - center_x) * math.sin(angle_rad) + (y - center_y) * math.cos(angle_rad) + center_y))
                            for x, y in vertices]

                min_y = min(vertices, key=lambda point: point[1])[1]
                max_y = max(vertices, key=lambda point: point[1])[1]
                shift_y = (min_y + max_y) / 2 - center_y
                vertices = [(x, y - shift_y) for x, y in vertices]

                display_polygon = True
                button_number = 6
            elif event.key == pygame.K_7:
                vertices = [(x, 2 * center_y - y) for x, y in original_vertices]
                vertices = [(x, int(2 * (y - center_y) + center_y)) for x, y in vertices]
                display_polygon = True
                button_number = 7
            elif event.key == pygame.K_8:
                scale_factor_x = 2
                scale_factor_y = 1
                angle_rotation = 30
                translation_y = -50
                translation_x = -250

                vertices = [(scale_factor_x * x, scale_factor_y * y) for x, y in original_vertices]

                angle_rad = math.radians(angle_rotation)
                vertices = [(int((x - center_x) * math.cos(angle_rad) - (y - center_y) * math.sin(angle_rad) + center_x),
                             int((x - center_x) * math.sin(angle_rad) + (y - center_y) * math.cos(angle_rad) + center_y))
                            for x, y in vertices]

                vertices = [(x, y + translation_y) for x, y in vertices]

                vertices = [(x + translation_x, y) for x, y in vertices]

                display_polygon = True
                button_number = 8
            elif event.key == pygame.K_9:
                angle_rotation = 180
                shear_factor = 0.3
                translation_x = 165

                angle_rad = math.radians(angle_rotation)
                vertices = [(int((x - center_x) * math.cos(angle_rad) - (y - center_y) * math.sin(angle_rad) + center_x),
                             int((x - center_x) * math.sin(angle_rad) + (y - center_y) * math.cos(angle_rad) + center_y))
                            for x, y in original_vertices]

                vertices = [(x, x * shear_factor + y) for x, y in vertices]

                vertices = [(x + translation_x, y) for x, y in vertices]

                display_polygon = True
                button_number = 9

    # Wypełnienie tła
    window.fill(YELLOW)

    # Rysowanie dziesięciokąta z ciemniejszym środkiem (jeśli zmienna display_polygon jest True)
    if display_polygon:
        pygame.draw.polygon(window, RED, vertices)
        pygame.draw.polygon(window, RED, vertices, 0)  # Wypełnienie środka
        pygame.draw.polygon(window, BLUE, vertices, 2)  # Rysowanie obramówki

        # Rysowanie numeru przycisku w lewym górnym rogu
        if button_number is not None:
            number_text = font.render(str(button_number), True, GRAY)
            number_rect = number_text.get_rect()
            number_rect.topleft = (10, 10)
            pygame.draw.rect(window, YELLOW, number_rect)
            window.blit(number_text, number_rect.topleft)

    # Aktualizacja ekranu
    pygame.display.flip()

# Zakończenie działania pygame
pygame.quit()