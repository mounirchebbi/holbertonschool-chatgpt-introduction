#!/usr/bin/python3
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        if mines >= width * height:
            raise ValueError("Number of mines cannot exceed board size")
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False

    def print_board(self, reveal=False):
        clear_screen()
        # Print column numbers
        print('   ' + ' '.join(str(i).rjust(2) for i in range(self.width)))
        print('  ' + '-' * (self.width * 3 + 1))
        for y in range(self.height):
            print(f'{str(y).rjust(2)}|', end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end='  ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end='  ')
                else:
                    print('.', end='  ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < self.width
                        and 0 <= ny < self.height
                        and not self.revealed[ny][nx]
                    ):
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate\
                               (0-{}): ".format(self.width-1)))
                y = int(input("Enter y coordinate\
                               (0-{}): ".format(self.height-1)))

                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds! Try again.")
                    continue

                if self.revealed[y][x]:
                    print("This cell is already revealed! Try again.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # Check for win condition
                unrevealed = sum(not cell
                                 for row in self.revealed for cell in row)
                if unrevealed == len(self.mines):
                    self.print_board(reveal=True)
                    print("Congratulations! You've won!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except KeyboardInterrupt:
                print("\nGame terminated by user.")
                break


if __name__ == "__main__":
    try:
        game = Minesweeper()
        game.play()
    except KeyboardInterrupt:
        print("\nGame terminated by user.")
