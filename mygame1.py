
import pygame
import random

# Initialize Pygame
pygame.init()

# Add sound
startSound = pygame.mixer.Sound('bullet.mp3')
hitSound = pygame.mixer.Sound('hit.mp3')

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BACK_GROUND = (240, 233, 242)


# Define Classes

class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        
        super().__init__()
       
        self.image = pygame.Surface([width, height]) 
        self.image.fill(color)

        self.rect = self.image.get_rect()
        
        
    def reset_pos(self):
        
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)

    def update(self):
        
        self.rect.y += 1
        if self.rect.y > 410:
            self.reset_pos()


class Player(Block):
    
    def update(self):
        # Get the current mouse position.  This returns the position as a 
        # list of numbers.  
        pos = pygame.mouse.get_pos()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]


# Main
startSound.play()

# Set screen width and height 
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    # This is a block
    color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    block = Block(color, 20, 15)
    
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    
    block_list.add(block)
    all_sprites_list.add(block)
    
# Create a black player
player = Player(BLACK, 20, 15)
all_sprites_list.add(player)   

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize score to zero
score = 0

#---------------------------------------------------------
# Main Loop
#---------------------------------------------------------

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # Clear the screen
    screen.fill(BACK_GROUND)
    
    # Call update() method on every sprite in the list
    all_sprites_list.update()
    
    # See if the player block has hit anything 
    block_hit_list = pygame.sprite.spritecollide(player, block_list, False)            
    
    # Check list of collisions 
    for block in block_hit_list:
        score +=1 
        print(score)
        hitSound.play()
        
        # Rest to the top of the screen to fall again
        block.reset_pos()
        
    # Draw all the spites
    all_sprites_list.draw(screen)
    
    # Limit to 20 frames per second
    clock.tick(20)
    
    # Go ahead and update the screen with what has bene drawn
    pygame.display.flip()

# Quit the game
pygame.quit()    
    
                
        
        
        
     


    



