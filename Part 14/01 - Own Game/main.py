import pygame
from random import randint

# Game constants
WINDOW_WIDTH = 640         # Width of the game window
WINDOW_HEIGHT = 480        # Height of the game window
ROBOT_SPEED = 5            # Speed of the robot
FALL_SPEED = 2             # Speed at which objects fall
NEW_OBJECT_FREQUENCY = 2   # Lower number means more frequent
WHITE = (255, 255, 255)    # Background color
BLACK = (0, 0, 0)          # Background color
RED = (255, 0, 0)          # Font color

class CoinCollector:
    def __init__(self):
        # Initialization of the game
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Coin Collector")
        self.font = pygame.font.SysFont("Arial", 22)

        self.load_assets()
        self.reset_game()
        self.main_loop()
    
    def load_assets(self):
        # Loading all necessary images for the game
        self.robot = pygame.image.load("robot.png")
        self.coin = pygame.image.load("coin.png")
        self.monster = pygame.image.load("monster.png")
    
    def reset_game(self):
        # Initialize / Reset the game state
        self.x = WINDOW_WIDTH // 2 - self.robot.get_width() / 2  # Robot's starting position X
        self.y = WINDOW_HEIGHT - self.robot.get_height()         # Robot's starting position Y
        self.score = 0
        self.falling_objects = []
        self.to_right = False
        self.to_left = False
        self.game_over = False
    
    def create_falling_object(self):
        # Create a new falling object (coin or monster) at a random position
        if randint(1, 100) <= NEW_OBJECT_FREQUENCY:
            if randint(0, 1) == 0:
                object = self.coin
                object_type = "coin"
            else:
                object = self.monster
                object_type = "monster"

            object_x = randint(0, WINDOW_WIDTH - object.get_width())
            object_y = 0 - object.get_height()
            self.falling_objects.append((object, object_type, object_x, object_y))
    
    def handle_collisions(self):
        # Handle collisions between the robot and falling objects
        robot_rectangle = self.robot.get_rect(topleft=(self.x, self.y))
        for i, (object, object_type, object_x, object_y) in enumerate(self.falling_objects):
            object_y += FALL_SPEED
            self.falling_objects[i] = (object, object_type, object_x, object_y)

            object_rectangle = object.get_rect(topleft=(object_x, object_y))
            if robot_rectangle.colliderect(object_rectangle):
                if object_type == "coin":
                    self.score += 1
                    del self.falling_objects[i]
                elif object_type == "monster":
                    self.game_over = True
                    return
            
            if object_y >= WINDOW_HEIGHT:
                del self.falling_objects[i]
    
    def draw(self):
        # Draw all game elements on the window
        self.window.fill(WHITE)
        for object, object_type, obj_x, obj_y in self.falling_objects:
            self.window.blit(object, (obj_x, obj_y))
        self.window.blit(self.robot, (self.x, self.y))
        
        # Display the current
        score_text = self.font.render(f"Score: {self.score}", True, RED)
        self.window.blit(score_text, (550, 10))

        if self.game_over:
            game_over_text = self.font.render("Game Over", True, RED)
            final_score_text = self.font.render(f"Final Score: {self.score}", True, BLACK)
            self.window.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - 24))
            self.window.blit(final_score_text, (WINDOW_WIDTH // 2 - final_score_text.get_width() // 2, WINDOW_HEIGHT // 2 + 24))
        pygame.display.flip()
    
    def main_loop(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.to_left = True
                    if event.key == pygame.K_RIGHT:
                        self.to_right = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.to_left = False
                    if event.key == pygame.K_RIGHT:
                        self.to_right = False

            if not self.game_over:
                if self.to_right and self.x <= WINDOW_WIDTH - self.robot.get_width():
                    self.x += ROBOT_SPEED
                if self.to_left and self.x > 0:
                    self.x -= ROBOT_SPEED

                self.create_falling_object()
                self.handle_collisions()
            
            self.draw()
            clock.tick(60)

if __name__ == "__main__":
    CoinCollector()
