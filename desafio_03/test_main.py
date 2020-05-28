from main import get_temperature
from unittest.mock import patch
import pytest

parametrized_values = [
    (-14.235004, -51.92528, 62, 16),
    (18.854793, -22.62783, 92, 33),
    (-32.75395, 09.37813, 70, 21),
]


@pytest.mark.parametrize("lat,lng,temperature,expected", parametrized_values)
def test_get_temperature_by_lat_lng(lat, lng, temperature, expected):

    mock_get_patcher = patch('main.requests.get')

    temperature = {
        "currently": {
            "temperature": temperature
        }
    }

    mock_get = mock_get_patcher.start()

    mock_get.return_value.json.return_value = temperature

    response = get_temperature(lat, lng)

    mock_get_patcher.stop()

    assert response == expected
