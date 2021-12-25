import os
import random
import sys
import time

import pygame

snake_speed = 20

WIDTH = 600
HEIGHT = 340
BLOCK_SIZE = 20

pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((600, 400))

fps = pygame.time.Clock()

bg = pygame.image.load(os.path.join("images", "background-snake.png"))

pygame.mouse.set_visible(False)

snake_position = [(WIDTH / 2) + 2, (HEIGHT / 2) - 10 + 2]
snake_body = [[WIDTH / 2 - 20, HEIGHT / 2],
              [WIDTH / 2 - 40, HEIGHT / 2],
              [WIDTH / 2 - 60, HEIGHT / 2],
              [WIDTH / 2 - 80, HEIGHT / 2]
              ]

fruit_position = [random.randrange(1, (WIDTH // 20)) * 20 + 2,
                  random.randrange(1, (HEIGHT // 20)) * 20 + 62]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0


def show_score():
    score_font = pygame.font.SysFont('helvetica neue', 35)
    score_surface = score_font.render('Score: ' + str(score), True, (39, 199, 71))

    screen.blit(score_surface, (30, 10))


def game_over():
    text_font = pygame.font.SysFont('helvetica neue', 50)

    game_over_surface = text_font.render('You scored ' + str(score) + ' points!', True, 'black')
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH/2, HEIGHT/4)

    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    quit()


def make_game():
    game_ended = False
    global change_to, direction, fruit_position, fruit_spawn, score
    while True:
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
            if event.type == pygame.QUIT:
                sys.exit()

        if change_to == 'UP' and direction != 'DOWN' and snake_position[0] % 20 == 2:
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP' and snake_position[0] % 20 == 2:
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT' and snake_position[1] % 20 == 2:
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT' and snake_position[1] % 20 == 2:
            direction = 'RIGHT'

        if direction == 'UP' and not game_ended:
            snake_position[1] -= 10
        if direction == 'DOWN' and not game_ended:
            snake_position[1] += 10
        if direction == 'LEFT' and not game_ended:
            snake_position[0] -= 10
        if direction == 'RIGHT' and not game_ended:
            snake_position[0] += 10
        # make snake stop moving when it dies
        if direction == 'NONE':
            snake_position[0] += 0
            snake_position[1] += 0
            game_ended = True

        # add another snake body at front of snake to move forward
        snake_body.insert(0, list(snake_position))

        # if snake eats the fruit
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 1
            fruit_spawn = False
        else:
            # if snake is still alive, remove last piece of snake body to imitate movement
            if not game_ended:
                snake_body.pop()

        # create new fruit in random position if it just got eaten
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (WIDTH // 20)) * 20 + 2,
                              random.randrange(1, (HEIGHT // 20)) * 20 + 62]
            # create new position for fruit if the generated position exists in the snake body
            while fruit_position in snake_body:
                fruit_position = [random.randrange(1, (WIDTH // 20)) * 20 + 2,
                                  random.randrange(1, (HEIGHT // 20)) * 20 + 62]

        fruit_spawn = True

        for pos in snake_body:
            pygame.draw.rect(screen, 'green', pygame.Rect(
                pos[0], pos[1], 16, 16))

        pygame.draw.rect(screen, 'red', pygame.Rect(
            fruit_position[0], fruit_position[1], 16, 16))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > WIDTH - 20:
            change_to = 'NONE'
            direction = 'NONE'
            game_over()
        if snake_position[1] < 60 or snake_position[1] > HEIGHT + 40:
            change_to = 'NONE'
            direction = 'NONE'
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                change_to = 'NONE'
                direction = 'NONE'
                game_over()

        # displaying score continuously
        show_score()

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)


if __name__ == "__main__":
    make_game()
