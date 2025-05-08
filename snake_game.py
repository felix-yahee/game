import random
import os
import time
import msvcrt

WIDTH = 30
HEIGHT = 20

def print_board(snake, food, score):
    os.system('cls')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [x, y] == food:
                print('O', end='')
            elif [x, y] in snake:
                print('*', end='')
            elif x == 0 or x == WIDTH-1 or y == 0 or y == HEIGHT-1:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(f"Score: {score}")

def get_key(last_direction):
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key in [b'w', b'W', b'H']:
            return 'UP'
        elif key in [b's', b'S', b'P']:
            return 'DOWN'
        elif key in [b'a', b'A', b'K']:
            return 'LEFT'
        elif key in [b'd', b'D', b'M']:
            return 'RIGHT'
    return last_direction

def main():
    snake = [[WIDTH//2, HEIGHT//2]]
    direction = 'RIGHT'
    food = [random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2)]
    score = 0

    while True:
        direction = get_key(direction)
        head = snake[0][:]
        if direction == 'UP':
            head[1] -= 1
        elif direction == 'DOWN':
            head[1] += 1
        elif direction == 'LEFT':
            head[0] -= 1
        elif direction == 'RIGHT':
            head[0] += 1

        if (head[0] == 0 or head[0] == WIDTH-1 or
            head[1] == 0 or head[1] == HEIGHT-1 or
            head in snake):
            print_board(snake, food, score)
            print("Game Over!")
            break

        snake.insert(0, head)
        if head == food:
            score += 1
            while True:
                food = [random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2)]
                if food not in snake:
                    break
        else:
            snake.pop()

        print_board(snake, food, score)
        time.sleep(0.1)

if __name__ == '__main__':
    main() 