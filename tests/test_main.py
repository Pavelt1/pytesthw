import pytest
import requests
from main import check_auth, solve, solve_2

# Тест Задание «Проверка логина и пароля»
@pytest.mark.parametrize(
        "login,password,expented",(
            ["admin","password","Добро пожаловать"],
            ["administrator","pass","Доступ ограничен"],
            [1333,1111,"Доступ ограничен"],
            [True,"password","Доступ ограничен"]
        ))
def test_check_auth(login, password,expented):
    result = check_auth(login, password)
    assert result == expented

# Тест Задание «Знакомство»
@pytest.mark.parametrize(
    "boys,girls,expented",(
        [['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
         ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
         "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha"],
        
        [['Peter', 'Alex', 'John', 'Arthur'],
         ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
         "Кто-то может остаться без пары!"],
        
        [['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
         ['Kate', 'Liza', 'Kira', 'Emma'],
         "Кто-то может остаться без пары!"],
    ))
def test_solve(boys,girls,expented):
    result = solve(boys,girls)
    assert result == expented

# Тест Задание «Кто дальше?»
@pytest.mark.parametrize(
        "hare_dist,turtle_dist,expented",(
            [[8, 5, 3, 2, 0, 1, 1],
             [3, 3, 3, 3, 3, 3, 3],
             "черепаха"],

            [[8, 5, 3, 2, 2, 1, 1],
             [3, 3, 3, 3, 3, 3, 3],
             "заяц"],

            [[8, 5, 3, 2, 1, 1, 1],
             [3, 3, 3, 3, 3, 3, 3],
             "одинаково"]
        ))
def test_solve_2(hare_dist,turtle_dist,expented):
    result = solve_2(hare_dist,turtle_dist)
    assert result == expented


class TestYandex:
    def setUp(self):
        self.header = { 
        "Authorization" : 'OAuth ............'
        }

    def tearDown(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {
            "path" : "Тест Папка"
        }
        response = requests.delete(url, params=params, headers=self.header)
        assert response.status_code == 200    

    def test_create(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {
                "path" : "Тест Папка"
            }
        response = requests.put(url,params=params, headers=self.header)
        assert response.status_code == 201

    def test_invalid_path(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {
                "Error" : "Тест Папка"
            }
        response = requests.put(url,params=params, headers=self.header)
        assert response.status_code == 400 

    def test_invalid_url(self):
        url = "https://cloud-api.yandex.net/v1/disk/resoError"
        params = {
                "path" : "Тест Папка"
            }
        response = requests.put(url,params=params, headers=self.header)
        assert response.status_code == 404 
