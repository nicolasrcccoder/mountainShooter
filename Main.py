import pygame

print("Setup Start")
pygame.init()

window = pygame.display.set_mode(size=(600, 480))
print("Setup end")

print("loop start")
while True:
    # check for all events (checa por todos os eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window (fechar janela)
            quit()  # end pygame
