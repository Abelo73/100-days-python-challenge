from tkinter import *
import random
import pygame

# Initialize pygame mixer
pygame.mixer.init()

GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"  # Green color for snake's body
HEAD_COLOR = "orange"  # Orange color for snake's head
FOOD_COLOR = "yellow"
BACKGROUND_COLOR = "#000000"

# Sound effects
EAT_SOUND = "snake_eat.mp3"
GAME_OVER_SOUND = "game_over.mp3"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")


def next_turn(snake, food):
    global paused
    if not paused:
        x, y = snake.coordinates[0]

        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        snake.coordinates.insert(0, (x, y))

        # Create a rounded rectangle for the snake's head
        if len(snake.coordinates) == 1:
            head_circle = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=HEAD_COLOR)
            head_rect_left = canvas.create_rectangle(x, y, x + SPACE_SIZE // 2, y + SPACE_SIZE, fill=HEAD_COLOR)
            head_rect_right = canvas.create_rectangle(x + SPACE_SIZE // 2, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                                      fill=HEAD_COLOR)
        else:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            global score
            score += 5
            label.config(text="Score: {}".format(score))
            canvas.delete("food")
            food = Food()
            # Play eat sound effect
            pygame.mixer.music.load(EAT_SOUND)
            pygame.mixer.music.play()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if check_collisions(snake):
            game_over()
        else:
            window.after(SPEED, next_turn, snake, food)
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


# def check_collisions(snake):
#     x, y = snake.coordinates[0]
#
#     if x < 0 or x >= GAME_WIDTH:
#         return True
#     elif y < 0 or y >= GAME_HEIGHT:
#         return True
#     for body_part in snake.coordinates[1:]:
#         if x == body_part[0] and y == body_part[1]:
#             return True
#     return False

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        # Snake hit the game boundaries
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            # Snake collided with itself
            return True
    return False


# def game_over():
#     canvas.delete(ALL)
#     canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 50),
#                        text='GAME OVER | Abel Adisu', fill='red', tag='game over')
#     # Play game over sound effect
#     pygame.mixer.music.load(GAME_OVER_SOUND)
#     pygame.mixer.music.play()
# def game_over():
#     global paused
#     paused = True  # Pause the game
#     canvas.delete(ALL)
#     # Display "Game Over" text
#     game_over_text = canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
#                                         font=('consolas', 50), text='GAME OVER', fill='red')
#     # Play game over sound effect
#     pygame.mixer.music.load(GAME_OVER_SOUND)
#     pygame.mixer.music.play()
#     # After a delay, restart the game
#     window.after(3000, restart_game)

def game_over():
    global paused
    paused = True  # Pause the game
    canvas.delete(ALL)
    # Display "Game Over" text
    game_over_text = canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                                        font=('consolas', 50), text='GAME OVER', fill='red')
    # Play game over sound effect
    pygame.mixer.music.load(GAME_OVER_SOUND)
    pygame.mixer.music.play()
    # After a delay, show crash animation
    window.after(2000, show_crash_animation)


def show_crash_animation():
    # Display crash animation (optional)
    # After 2 seconds, restart the game
    window.after(2000, restart_game)


def restart_game():
    global paused, score, direction, snake, food  # Declare snake and food as global variables
    paused = False
    score = 0
    direction = 'down'
    label.config(text="Score: {}".format(score))
    snake.coordinates = []
    snake.squares = []
    food.coordinates = []
    canvas.delete(ALL)
    snake = Snake()
    food = Food()
    next_turn(snake, food)


def toggle_pause(event):
    global paused
    paused = not paused


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'
paused = False

label = Label(window, text="Score:{}".format(score), font=('consolas', 14))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
# window.geometry(f"{window_width} * {window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<space>', toggle_pause)

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
