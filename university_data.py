import requests


def get_university_data(country):
    response = requests.get(
        f"http://universities.hipolabs.com/search?country={country}")
    data = response.json()
    return (data)
