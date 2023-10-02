import pytest
import yaml
import requests

with open('config.yaml', encoding="utf-8") as file:
    my_dict = yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']


@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data={'username': 'username', 'password': 'password'})
    token = obj_data.json()['token']
    return token


@pytest.fixture()
def post():
    obj_data = requests.post(url=url1, headers={"X-Auth-Token": my_dict['token']}, data={
        'username': 'rav53-85@mail.ru',
        'password': 'X578Z4AE',
        'title': 'newTitle',
        'description': 'BBB',
        'content': 'not me'})
    return obj_data.json()['description']
