from main import get_temperature
from unittest.mock import patch
import pytest
import requests


LATITUDE = -14.235004
LONGITUDE = -51.92528
TEMPETATURES = [(62, 16), (92, 33), (70, 21), (0, -17),
                ('e', 'error'), (80, 26), (None, 'error'), (-4, -20)]


@patch('main.requests.get')
@pytest.mark.parametrize("farenheit, celcius", TEMPETATURES)
def test_get_temperature_by_lat_lng(mock_requests_get, farenheit, celcius):

    mock_requests_get.return_value.json.return_value = {
        "currently": {
            "temperature": farenheit
        }
    }

    response = get_temperature(LATITUDE, LONGITUDE)

    assert celcius == response, "Actual result was {}".format(response)
