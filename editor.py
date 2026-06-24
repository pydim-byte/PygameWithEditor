import pygame, sys
from editor_modules.globals import Mode
from editor_modules.namings import ModeName
from editor_modules.menus.setup_menu import SetupMenu
from editor_modules.menus.editor_menu import EditorMenu

 
class Editor:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps : int = 60
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.display_size = pygame.display.get_surface().get_size()
        self.W : int = self.display_size[0]
        self.H : int = self.display_size[1]
        self.menu = SetupMenu()

    def handle_inputs(self, inputs : dict) -> None:
        self.menu.hanlde_inputs(inputs)

    def update(self) -> None:
        if Mode.NEXT == ModeName.EDITOR:
            Mode.NEXT = None
            Mode.CURRENT == ModeName.EDITOR
            self.menu = EditorMenu()
            pygame.key.set_repeat(100)
        self.menu.update()

    def draw(self, screen : pygame.surface.Surface) -> None:
        screen.fill("grey")
        if Mode.CURRENT == ModeName.SETUP:
            pygame.draw.rect(screen, (50, 50, 255), pygame.Rect(0, self.H - 40, self.W, 40))
            pygame.draw.rect(screen, "black", pygame.Rect(0, self.H - 40, self.W, 40), width=1)
        self.menu.draw(screen)
        pygame.display.flip()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.handle_inputs(event)

            self.update()
            self.draw(self.screen)
            self.clock.tick(self.fps)


editor = Editor()
editor.run()