import requests
from requests.exceptions import RequestException


def get_temperature(lat, lng):
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)

    try:
        reponse = requests.get(url)
        data = reponse.json()

        temperature = data.get('currently').get('temperature')
        celcius = int((temperature - 32) * 5.0 / 9.0)

    except RequestException as erro:
        print("An HTTP exception was throw {}".format(erro))
        celcius = 'error'

    except AttributeError as erro:
        print("An exception was throw {}".format(erro))
        celcius = 'error'

    except TypeError as erro:
        print("An Type exception was throw {}".format(erro))
        celcius = 'error'

    except ValueError as erro:
        print("An Value exception was throw {}".format(erro))
        celcius = 'error'

    except TimeoutError as erro:
        print("An Timeout exception was throw {}".format(erro))
        celcius = 'error'

    return celcius
