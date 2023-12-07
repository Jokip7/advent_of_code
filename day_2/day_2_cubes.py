file = open("cube_games.txt", "r")
games = file.readlines()

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

possible_games: list[int] = []


def is_game_possible(game: str) -> bool:
    for move in game.split(";"):
        for color in move.split(","):
            if "red" in color:
                if int("".join(filter(str.isdigit, color))) > MAX_RED:
                    return False
            elif "green" in color:
                if int("".join(filter(str.isdigit, color))) > MAX_GREEN:
                    return False
            elif "blue" in color:
                if int("".join(filter(str.isdigit, color))) > MAX_BLUE:
                    return False
    return True


def get_pow_highest_colors(game: str) -> int:
    highest_red = 0
    highest_green = 0
    highest_blue = 0
    for move in game.split(";"):
        for color in move.split(","):
            if "red" in color:
                red = int("".join(filter(str.isdigit, color)))
                if red > highest_red:
                    highest_red = red
            elif "green" in color:
                green = int("".join(filter(str.isdigit, color)))
                if green > highest_green:
                    highest_green = green
            elif "blue" in color:
                blue = int("".join(filter(str.isdigit, color)))
                if blue > highest_blue:
                    highest_blue = blue

    return highest_red * highest_green * highest_blue


def check_games():
    game_i = 1
    for game in games:
        game = game[game.find(":") + 1 :]
        if is_game_possible(game):
            possible_games.append(game_i)
        game_i = game_i + 1


def sum_games() -> int:
    highest_colors: list[int] = []
    for game in games:
        game = game[game.find(":") + 1 :]
        highest_colors.append(get_pow_highest_colors(game))
    return sum(highest_colors)


check_games()
print(sum(possible_games))
print(sum_games())
