import pytest
from gps_distance import gps_distance
from input_verification import input_verification
from match_points import match_points

def test_gps_distance():
    # Known distance between New York and London
    new_york = (40.7128, -74.0060)
    london = (51.5074, -0.1278)
    assert pytest.approx(gps_distance(new_york, london), 0.1) == 5570.22

def test_input_verification():
    # Case 1: Directional indicators
    raw_data = "40.7128° N 74.0060° W"
    assert input_verification(raw_data) == [(40.7128, -74.006)]

    # Case 2: Simple decimals
    raw_data = "51.5074 -0.1278"
    assert input_verification(raw_data) == [(51.5074, -0.1278)]

    # Case 3: Degrees without directional indicators
    raw_data = "40 42.8 74 00.6"
    assert input_verification(raw_data) == [(40.71333333333334, 74.01)]

    # Case 4: Invalid format
    raw_data = "Invalid Data"
    with pytest.raises(ValueError):
        input_verification(raw_data)

def test_match_points():
    # Testing closest match
    array_a = [(40.7128, -74.0060), (51.5074, -0.1278)]
    array_b = [(41.8781, -87.6298), (51.1657, 10.4515)]
    assert match_points(array_a, array_b) == [0, 1]

    # Edge case: Identical coordinates
    array_a = [(40.7128, -74.0060)]
    array_b = [(40.7128, -74.0060)]
    assert match_points(array_a, array_b) == [0]

    # Edge case: No coordinates in array_b
    array_a = [(40.7128, -74.0060)]
    array_b = []
    with pytest.raises(ValueError):  # 修改为捕获 ValueError
        match_points(array_a, array_b)

