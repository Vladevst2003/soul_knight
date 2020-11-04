import pygame

window = 500, 500
screen = pygame.display.set_mode(window)
running = True
clock = pygame.time.Clock()
field = [1000, 1000]
coords = [500, 500]
max_out = [100, 100]
move = [0, 0]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                move[1] = 0
            if event.key == pygame.K_w:
                move[1] = 0
            if event.key == pygame.K_d:
                move[0] = 0
            if event.key == pygame.K_a:
                move[0] = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                move[1] = 1
            if event.key == pygame.K_w:
                move[1] = -1
            if event.key == pygame.K_d:
                move[0] = 1
            if event.key == pygame.K_a:
                move[0] = -1

    coords = [min(max(coords[0] + move[0], 0), field[0] - 1), min(max(coords[1] + move[1], 0), field[1] - 1)]
    screen.fill([0, 0, 0])
    view = [min(max(coords[0] - window[0] // 2, - max_out[0]), field[0] + max_out[0] - window[0]), min(max(coords[1] - window[1] // 2, - max_out[1]), field[1] + max_out[1] - window[1])]
    print(coords)
    pygame.draw.rect(screen, (255, 255, 255), (0 - 1 - view[0], 0 - 1 - view[1] + 50, field[0], field[1]))
    pygame.draw.rect(screen, (0, 0, 0), (coords[0] - 1 - view[0], coords[1] - 1 - view[1], 2, 2))



    pygame.display.flip()
    clock.tick(100)
pygame.quit()
