import pygame

pygame.init()

window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

window.fill((0, 0, 0))

window.blit(robot, (0,0))
window.blit(robot, (window_width - robot_width,0))
window.blit(robot, (0,window_height - robot_height))
window.blit(robot, (window_width - robot_width,window_height - robot_height))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            