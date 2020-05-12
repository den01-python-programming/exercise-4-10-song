import pytest
from src.song import Song

def test_exercise(capsys):
    garden = Song("In The Garden", 10910)
    print("The song " + garden.name + " has a length of " + str(garden.length) + " seconds.")

    out, err = capsys.readouterr()
    assert out == "The song In The Garden has a length of 10910 seconds.\n"
