import pygame, sys, time, json

class Editor:
    def __init__(self):
        self.display = pygame.display.set_mode((500, 500))
        self.screen = pygame.Surface((250, 250))
        self.dt = 1
        self.last_time = time.time() - 1 / 60
        self.clock = pygame.time.Clock()
        self.running = True
    
    def close(self):
        self.running = False
        pygame.quit()
        sys.exit()
    
    def update(self):
        pass
    
    def run(self):
        while self.running:
            self.dt = time.time() - self.last_time
            self.dt *= 60
            self.last_time = time.time()
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close()
            self.update()
            pygame.transform.scale_by(self.screen, 2.0, self.display)
            pygame.display.set_caption(f'FPS: {self.clock.get_fps() :.1f}')
            pygame.display.flip()
            self.clock.tick()

if __name__ == '__main__':
    Editor().run()
