print("Welcome to my X's and O's tutorial program!")
print("Eventually I hope to add a multiplayer mode.")

cell_position = [1,2,3,4,5,6,7,8,9]
three_in_a_row = 0
total_moves = 0


def grid(self):
    vertical_grid = "|"
    horizontal_grid = "---------"
    print(cell_position[0], vertical_grid, cell_position[1], vertical_grid, cell_position[2])
    print(horizontal_grid)
    print(cell_position[3], vertical_grid, cell_position[4], vertical_grid, cell_position[5])
    print(horizontal_grid)
    print(cell_position[6], vertical_grid, cell_position[7], vertical_grid, cell_position[8])

grid(1)

while total_moves < 9:
    while three_in_a_row == 0:

            if total_moves == 0 or total_moves == 2 or total_moves == 4 or total_moves == 6 or total_moves == 8:
                player_x_move = int(input("Player X, select a cell:  "))

                if player_x_move == 1:
                    cell_position[0] = "X"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 2:
                    cell_position[1] = "X"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 3:
                    cell_position[2] = "X"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 4:
                    cell_position[3] = "X"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 5:
                    cell_position[4] = "X"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 6:
                    cell_position[5] = "X"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 7:
                    cell_position[6] = "X"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 8:
                    cell_position[7] = "X"
                    grid(1)
                    total_moves += 1
                else:
                    cell_position[8] = "X"
                    grid(1)
                    total_moves += 1

            else:
                player_x_move = int(input("Player O, select a cell:  "))

                if player_x_move == 1:
                    cell_position[0] = "O"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 2:
                    cell_position[1] = "O"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 3:
                    cell_position[2] = "O"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 4:
                    cell_position[3] = "O"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 5:
                    cell_position[4] = "O"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 6:
                    cell_position[5] = "O"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 7:
                    cell_position[6] = "O"
                    grid(1)
                    total_moves += 1
                elif player_x_move == 8:
                    cell_position[7] = "O"
                    grid(1)
                    total_moves += 1
                else:
                    cell_position[8] = "O"
                    grid(1)
                    total_moves += 1

            if cell_position[0] == "X" and cell_position[1] == "X" and cell_position[2] == "X":
                three_in_a_row = 1
                print("Player X WINS!")
                break
