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


def check_games():
    game_i = 1
    for game in games:
        game = game[game.find(":") + 1 :]
        if is_game_possible(game):
            possible_games.append(game_i)
        game_i = game_i + 1


check_games()
print(sum(possible_games))
