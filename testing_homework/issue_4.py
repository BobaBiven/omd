import pytest
from one_hot_encoder import fit_transform


def test_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
        ]
    actual = fit_transform(cities)
    assert actual == expected


def test_weather():
    weather = [
        'cold', 'cold', 'warm',
        'cold', 'hot', 'hot',
        ]
    expected = [
        ('cold', [0, 0, 1]),
        ('cold', [0, 0, 1]),
        ('warm', [0, 1, 0]),
        ('cold', [0, 0, 1]),
        ('hot', [1, 0, 0]),
        ('hot', [1, 0, 0])
    ]
    actual = fit_transform(weather)
    assert actual == expected


def test_empty():
    arr = []
    expected = []
    actual = fit_transform(arr)
    assert actual == expected


def test_exception():
    with pytest.raises(TypeError):
        fit_transform(1)
