import sys
from enum import Enum
from tools import runtime
import pathlib


class HandShape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


letter_to_handshape = {
    'A': HandShape.ROCK,
    'B': HandShape.PAPER,
    'C': HandShape.SCISSORS,
    'X': HandShape.ROCK,
    'Y': HandShape.PAPER,
    'Z': HandShape.SCISSORS
}

# Maps a hand shape to the shape it wins against
wins_against = {
    HandShape.ROCK: HandShape.SCISSORS,
    HandShape.SCISSORS: HandShape.PAPER,
    HandShape.PAPER: HandShape.ROCK
}

looses_against = {v: k for k, v in wins_against.items()}

points_for_shape = {
    HandShape.ROCK: 1,
    HandShape.PAPER: 2,
    HandShape.SCISSORS: 3
}


def parse_game(line, my_letter_to_shape):
    shapes_letters = line.rstrip('\n').split(" ")
    opponent_symbol = letter_to_handshape[shapes_letters[0]]
    my_symbol = my_letter_to_shape(shapes_letters[1], opponent_symbol)
    return (opponent_symbol, my_symbol)


def score_game(hand_shapes):
    opponent_shape, my_shape = hand_shapes
    symbol_points = points_for_shape[my_shape]
    if my_shape == opponent_shape:  # draw
        game_points = 3
    elif wins_against[opponent_shape] == my_shape:
        game_points = 0
    else:  # I win :-)
        assert wins_against[my_shape] == opponent_shape
        game_points = 6
    return symbol_points + game_points


def simple_letter_to_shape(letter, opponent_symbol):
    return letter_to_handshape[letter]


def shape_for_desired_outcome(letter, opponent_shape):
    if letter == 'X':  # I need to loose
        my_shape = wins_against[opponent_shape]
    elif letter == 'Y':  # draw
        my_shape = opponent_shape
    else:  # I need to win
        my_shape = looses_against[opponent_shape]
    return my_shape


@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[:]
    lines = open(pathlib.Path(__file__).parent / "input").readlines()
    part1 = sum(
        score_game(parse_game(line, simple_letter_to_shape)) for line in lines)
    print(part1)
    part2 = sum(
        score_game(parse_game(line, shape_for_desired_outcome))
        for line in lines)
    print(part2)


if __name__ == "__main__":
    main()