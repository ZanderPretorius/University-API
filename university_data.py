import requests
from collections import OrderedDict


def get_university_data(country):
    response = requests.get(
        f"http://universities.hipolabs.com/search?country={country}")
    data = response.json()
    # print(data)

    result = list(
        {
            dictionary['name']: dictionary
            for dictionary in data
        }.values()
    )

    return (result)
