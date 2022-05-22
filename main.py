from abc import ABC, abstractclassmethod
from typing import Dict
from pygame.event import Event
import pygame
from types import FunctionType

class Window: 
    root: pygame = pygame
    run: bool = True
    event: pygame.event = pygame.event
    screen: pygame.display = pygame.display
    display: object
    clock: pygame.time.Clock = pygame.time.Clock
    draw: pygame.draw = pygame.draw
    
    def get_clock(self): return self.clock
    
    def get_event(self): return self.event
    
    def get_display(self): return self.display

    def get_run(self): return self.run
    def set_run(self, o:bool = True): self.run = o
    
    def get_root(self): return self.root
    
    def get_screen(self): return self.screen
    
    def header_func(self): pass
    def set_header_func(self, o:FunctionType): self.header_func = o

    def control_func(self, event:Event = None):pass
    def set_control_func(self, o:FunctionType): self.set_control_func = o

    def main_func(self):pass
    def set_main_func(self, o:FunctionType): self.main_func = o

    def __init__(self, w: int, h: int) -> None:
        self.root.init()
        self.screen.init()

        self.display = self.screen.set_mode((w, h), 0, 32)

    def loop(self):
        while self.run:
            for events in self.event.get():
                if events.type == self.root.QUIT:
                    self.run = False
                self.control_func(events)
            self.main_func()

class Player(ABC):pass

class BPlayer(Player):
    def auto(self):pass

class RPlayer(Player):
    key_func: Dict = {}
    constants: int = None
    def __init__(self, start_x, start_y, w, h) -> None:

        self.key_func[pygame.K_UP] = self.move_up
        self.key_func[pygame.K_DOWN] = self.move_down
        self.key_func[pygame.K_LEFT] = self.move_left
        self.key_func[pygame.K_RIGHT] = self.move_right
    
        self.weight = w
        self.height = h
        
        self.x = start_x
        self.y = start_y

        self.rect = pygame.rect.Rect((self.x, self.y),(self.weight, self.height))

    def move_up(self):pass
    print("up +4")
    def set_move_up(self, o:FunctionType): self.move_up = o

    def move_down(self):pass
    def set_move_down(self, o:FunctionType): self.move_down = o

    def move_right(self):pass
    def set_move_right(self, o:FunctionType): self.move_right = o
    
    def move_left(self):pass
    def set_move_left(self, o:FunctionType): self.move_left = o

    def get_player_coordinat(self): return [self.x, self.y]

    def add_x(self, o: int): self.rect.x += o
    def add_y(self, o:int): self.rect.y += o

    def control_func(self, events:Event):
        print("aktarım yapıldı")
        self.key_func[self.constants]()
        if events.type == pygame.KEYDOWN:
            print(events.key)
            self.constants = events.key

class Pong:
    
    player_1: Player = RPlayer(960, 540, 100, 100)
    player_2: Player = RPlayer


    def player_1_move_up(self):
        self.player_1.add_y(4)

    def map_draw(self):pass
    def player_1_move_down(self):
        self.player_1.add_y(-4)

    def __init__(self, w:Window = None) -> None:
        self.window = w
        
        self.player_1.set_move_up(self.player_1_move_up)
        self.player_1.set_move_down(self.player_1_move_down)

    def header_func(self): 
        sc = self.window.get_screen()
        sc.fill()

    def control_func(self, events: Event): 
        self.player_1.control_func(events)
        self.player_2.control_func(events)

    def main_func(self): 
        self.window.screen.flip()
        self.window.draw.rect(self.window.display, (255,255,255), self.player_1.rect)
        

class Game:
    window: Window
    pong: Pong

    def __init__(self) -> None:
        self.window = Window(1920, 1080)

        self.pong = Pong(self.window) 

        self.window.set_header_func(self.pong.header_func)
        self.window.set_control_func(self.pong.control_func)
        self.window.set_main_func(self.pong.main_func)

    def start(self): self.window.loop()

if __name__ == "__main__":
    game: Game = Game()
    game.start()

