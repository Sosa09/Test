import pygame, sys
from settings import *
from level import Level
from battle import Battle
class Game:

    def __init__(self):
        #de Basics
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('POKEMON SYNTRA')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.battle = Battle()
        self.groups = pygame.sprite.Group()
        self.groups.add(self.level.pokemons)
        
   
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()           
            # for button in self.buttons: # added by joris maar nog niet opp
            #     if button.handle_event(event):
            #         button_text = button.text.lower()
            #         if button_text == "pause":
            #             running = False
            #implementing colission detection.add()
            #the colission detection works by looping through all the pokemons available on the maps coliding with the actual Player
            for x in self.level.pokemons: 
                if pygame.sprite.collide_rect(self.level.player, x):
                    running = False
                    self.collidedItem = x
                    self.battle._start_battle(self)
            self.screen.fill('chartreuse4')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            

if __name__=='__main__':
    game = Game()
    game.run()