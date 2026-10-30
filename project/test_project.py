from project import (
    intro_part_1,
    intro_part_2,
    fibonacci,
    biggest_value,
    pythagoras,
    randomness,
)
import pytest


def test_intro_part_1():
    # test first part of intro
    assert (
        intro_part_1()
        == "HOW TO PLAY: the small black object at the bottom is the spike, and you need to jump(w/space/up arrow) to avoid it."
    )


def test_intro_part_2():
    # test second part of intro
    assert (
        intro_part_2()
        == "The small smiley at the bottom is the player which you will be controlling. hope you enjoy my game.good luck!"
    )


def test_fibonacci():
    # F(10) = F(9) + F(8)
    assert fibonacci(10) == 55


def test_biggest_value():

    with pytest.raises(ValueError):
        # empty value
        biggest_value([])
    # 3 is the biggest
    assert biggest_value([1, 2, 3]) == 3


def test_pythagoras():
    # √ 3² + 4² = 5²
    assert pythagoras(3, 4) == 5.0


def test_randomness():
    # put pythagoras
    # and fibonacci
    # in calculation
    assert 0 <= randomness(2, 5, 2, 4) <= 2
