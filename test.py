import pytest
from gps_distance import gps_distance
from input_verification import input_verification
from match_points import match_points

def test_gps_distance():
    """
    Test the distance between New York and London using gps_distance.
    Known approximate distance: ~5570.22 km
    """
    new_york = (40.7128, -74.0060)
    london = (51.5074, -0.1278)
    
    assert gps_distance(new_york, london) == pytest.approx(5570.22, 0.1)

def test_input_verification():
    """
    Test the input_verification function with various formats.
    """

    # Case 1: Directional indicators
    raw_data = "40.7128° N 74.0060° W"
    result = input_verification(raw_data)
    assert len(result) == 1
    lat, lon = result[0]
    assert lat == pytest.approx(40.7128, 1e-12)
    assert lon == pytest.approx(-74.006, 1e-12)

    # Case 2: Simple decimals
    raw_data = "51.5074 -0.1278"
    result = input_verification(raw_data)
    assert len(result) == 1
    lat, lon = result[0]
    assert lat == pytest.approx(51.5074, 1e-12)
    assert lon == pytest.approx(-0.1278, 1e-12)

    # Case 3: Degrees without directional indicators (e.g., "40 42.8 74 00.6")
    raw_data = "40 42.8 74 00.6"
    result = input_verification(raw_data)
    assert len(result) == 1
    lat, lon = result[0]
    assert lat == pytest.approx(40.71333333333334, 1e-12)
    assert lon == pytest.approx(74.01, 1e-12)

    # Case 4: Invalid format
    raw_data = "Invalid Data"
    with pytest.raises(ValueError):
        input_verification(raw_data)

def test_match_points():
    """
    Test the match_points function with different scenarios.
    """
    array_a = [(40.7128, -74.0060), (51.5074, -0.1278)]
    array_b = [(41.8781, -87.6298), (51.1657, 10.4515)]
    assert match_points(array_a, array_b) == [0, 1]

    array_a = [(40.7128, -74.0060)]
    array_b = [(40.7128, -74.0060)]
    assert match_points(array_a, array_b) == [0]

    array_a = [(40.7128, -74.0060)]
    array_b = []
    with pytest.raises(ValueError):
        match_points(array_a, array_b)
