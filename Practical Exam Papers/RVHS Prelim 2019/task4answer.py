import random

gems = ["d", "s", "t", "r", "e"]
# Diamond, Sapphire, Topaz, Ruby, Emerald
d_dict = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
d_str_dict = {"u": "up", "d": "down", "l": "left", "r": "right"}
# Up, Down, Left, Right
board = [['r', 'r', 'd', 'e', 'd'], ['s', 'd', 'r', 'd', 't'], [
    'd', 'd', 'r', 's', 'd'], ['e', 'r', 't', 'r', 'r'], ['t', 'e', 'e', 's', 'd']]


class Begemed:
    def __init__(self, n):
        self._board = [["_" for _ in range(n)] for _ in range(n)]

    def check_connection(self, row, col):
        d_count = {"u": 0, "d": 0, "l": 0, "r": 0}

        for d in d_dict:
            row_shift, col_shift = d_dict[d]
            new_row = row + (d_count[d] + 1) * row_shift
            new_col = col + (d_count[d] + 1) * col_shift
            while 0 <= new_row < len(self._board) and \
                    0 <= new_col < len(self._board) and \
                    self._board[new_row][new_col] == self._board[row][col] and \
                    self._board[new_row][new_col] != "_" and \
                    self._board[row][col] != "_":
                d_count[d] += 1
                new_row = row + (d_count[d] + 1) * row_shift
                new_col = col + (d_count[d] + 1) * col_shift

        return d_count["u"] + d_count["d"] + 1 >= 3 or \
            d_count["l"] + d_count["r"] + 1 >= 3, d_count

    def find_valid_moves(self, row, col):
        valid_moves = []
        for d in d_dict:
            new_row = row + d_dict[d][0]
            new_col = col + d_dict[d][1]
            if not (0 <= new_row < len(self._board) and
                    0 <= new_col < len(self._board)):
                continue

            # swap
            self._board[row][col], self._board[new_row][new_col] = \
                self._board[new_row][new_col], self._board[row][col]

            if self.check_connection(new_row, new_col)[0]:
                valid_moves.append(d)

            # swap back
            self._board[row][col], self._board[new_row][new_col] = \
                self._board[new_row][new_col], self._board[row][col]
        return valid_moves

    def check_lose(self):
        count = 0
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                if self.find_valid_moves(i, j):
                    count += 1
        return count == 0

    def new_game(self, board=[]):
        if board == []:
            # generate random board
            for i in range(len(self._board)):
                for j in range(len(self._board)):
                    while True:
                        self._board[i][j] = random.choice(gems)
                        if not self.check_connection(i, j)[0]:
                            break

            if self.check_lose():
                self.new_game()
        else:
            self._board = board
        print(self._board)

    def display(self, hint=False):
        n = len(self._board)
        result = ""

        # index line
        result += "   "
        for j in range(n):
            result += "  {} ".format(j)
        result += "  \n"

        # grid line
        result += "   "
        for j in range(n):
            result += "+---"
        result += "+\n"

        for i in range(n):
            # content line
            # leading index
            result += str(i) + "  "
            # iteration for blocks
            for j in range(n):
                if hint and len(self.find_valid_moves(i, j)) > 0:
                    result += "| {} ".format(str(self._board[i][j]).upper())
                    print((i, j), self.find_valid_moves(i, j))
                else:
                    result += "| {} ".format(self._board[i][j])
            result += "|\n"

            # grid line
            result += "   "
            for j in range(n):
                result += "+---"
            result += "+\n"

        print()
        print(result)

    def move_gem(self, row, col, d):
        swap_row = row + d_dict[d][0]
        swap_col = col + d_dict[d][1]

        # swap
        self._board[row][col], self._board[swap_row][swap_col] = \
            self._board[swap_row][swap_col], self._board[row][col]
        cells_to_check = [(row, col), (swap_row, swap_col)]

        def check_board():
            connected_cells = []
            for i in range(len(self._board)):
                for j in range(len(self._board)):
                    if self.check_connection(i, j)[0]:
                        connected_cells.append((i, j))
            return connected_cells

        def remove_connected(row, col):
            # find out which direction can remove gem
            d_count = self.check_connection(row, col)[1]
            remove_d = []
            if d_count["u"] + d_count["d"] + 1 >= 3 and d_count["u"] > 0:
                remove_d.append("u")
            if d_count["u"] + d_count["d"] + 1 >= 3 and d_count["d"] > 0:
                remove_d.append("d")
            if d_count["l"] + d_count["r"] + 1 >= 3 and d_count["l"] > 0:
                remove_d.append("l")
            if d_count["l"] + d_count["r"] + 1 >= 3 and d_count["r"] > 0:
                remove_d.append("r")

            # remove gems only in the rd directions
            for rd in remove_d:
                for i in range(d_count[rd]):
                    new_row = row + (i + 1) * d_dict[rd][0]
                    new_col = col + (i + 1) * d_dict[rd][1]
                    self._board[new_row][new_col] = "_"

            # remove centre gem
            if len(remove_d) != 0:
                self._board[row][col] = "_"

        # transpose matrix
        def transpose(m):
            result = []
            for j in range(len(m[0])):
                row = []
                for i in range(len(m)):
                    row.append(m[i][j])
                result.append(row)

            return result

        while len(cells_to_check) != 0:
            # remove connected gems
            for r, c in cells_to_check:
                remove_connected(r, c)
            self.display()

            # shift gems down columns

            # self.display()
            # self._board = transpose(self._board)
            # self.display()
            # self._board = transpose(self._board)
            # self.display()
            # print("transpose test")

            temp_matrix = transpose(self._board)
            temp_result = []
            for i in range(len(temp_matrix)):
                temp_row = []
                count = 0
                for j in range(len(temp_matrix) - 1, -1, -1):
                    if temp_matrix[i][j] != "_":
                        temp_row.append(temp_matrix[i][j])
                    else:
                        count += 1

                for j in range(count):
                    temp_row.append(random.choice(gems))

                temp_row.reverse()
                temp_result.append(temp_row)

            self._board = transpose(temp_result)
            self.display()

            cells_to_check = check_board()
            print(cells_to_check)


def test_bejeweled():
    game = Begemed(3)
    game.new_game()
    game.display()


# test_bejeweled()


def validate_int(user_input, optional_arg):
    min_val, max_val = optional_arg
    # presence check
    if len(user_input) == 0:
        print("Presence Check Failed. Please do not leave the field blank.")
        return False
    # type check
    if not user_input.isdigit():
        print("Type Check Failed. Please enter a valid integer.")
        return False
    # range check
    if not (min_val <= int(user_input) <= max_val):
        print("Range Check Failed. Please key in values in range {} to {}.".format(
            min_val, max_val))
        return False

    return True


def validate_direction(user_input, optional_arg=None):
    if user_input not in "uUdDlLrR":
        print("Please only input U/D/L/R for direction.")
    else:
        return True


def valid_user_input(validate_func, question, optional_arg=[]):
    done = False
    user_input = ""
    while not done:
        user_input = input(question).strip()
        done = validate_func(user_input, optional_arg)
    return user_input


def display_main_menu():
    print("Choose an option below:")
    print("1) Validate Move")
    print("2) Toggle Hint Mode")
    print("3) Move the Gem!")
    print("4) New Game")
    print("5) Exit")


def menu():
    done = False
    hint = False

    size = int(valid_user_input(
        validate_int, "Please select size of game from 3 to 10: ", (3, 10)))
    game = Begemed(size)

    game.new_game(board)

    while not done:
        game.display(hint=hint)

        display_main_menu()
        menu_input = int(valid_user_input(
            validate_int, "Please select an option from 1 to 5: ", (1, 5)))
        print()

        if menu_input in (1, 3):
            row = int(valid_user_input(
                validate_int, "Enter row: ", (0, size-1)))
            col = int(valid_user_input(
                validate_int, "Enter col: ", (0, size-1)))
            d = valid_user_input(validate_direction,
                                 "Enter direction (U)p/(D)own/(L)eft/(R)ight: ").lower()
            print()

            if d in game.find_valid_moves(row, col):
                if menu_input == 1:
                    print("Valid move, gem at ({}, {}) can be moved [{}].".format(
                        row, col, d_str_dict[d]))
                else:
                    game.move_gem(row, col, d)
                    print("Gem at ({}, {}) moved [{}].".format(
                        row, col, d_str_dict[d]))
            else:
                print("Invalid Move, please try again.")

            print()
        elif menu_input == 2:
            hint = not hint
            print("Hint mode {}.\n".format("on" if hint else "off"))
        elif menu_input == 4:
            print("Starting a new game! Hint mode off.\n")
            hint = False
            size = int(valid_user_input(
                validate_int, "Please select size of game from 3 to 10: ", (3, 10)))
            game = Begemed(size)
            game.new_game()
        else:
            print("Exit Game. Thanks for playing!")
            done = True


menu()
