import pygame
import numpy as np

pygame.init()

win_x = 500
win_y = 500

win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Paint')

class DrawingTool:
    def __init__(self):
        self.color = (255, 255, 255)
        self.radius = 10
        self.is_drawing = False
        self.points = []

    def start_draw(self, pos):
        self.is_drawing = True
        self.points.append(pos)

    def continue_draw(self, pos):
        if self.is_drawing:
            self.points.append(pos)

    def end_draw(self):
        self.is_drawing = False

    def draw(self, window):
        for i in range(len(self.points) - 1):
            pygame.draw.line(window, self.color, self.points[i], self.points[i + 1], self.radius * 2)

def main_loop():
    drawing_tool = DrawingTool()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing_tool.start_draw(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEMOTION:
                drawing_tool.continue_draw(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing_tool.end_draw()

        win.fill((0, 0, 0))
        drawing_tool.draw(win)
        pygame.display.update()

    convert_to_image(drawing_tool.points)
    pygame.quit()

def convert_to_image(points):
    img = np.zeros((28, 28), dtype=np.uint8)
    for point in points:
        x, y = point
        img[y // 18, x // 18] = 255

    img_vector = img.flatten()

    print("Image vector shape:", img_vector.shape)
    print("Image vector:", img_vector.tolist())

main_loop()
