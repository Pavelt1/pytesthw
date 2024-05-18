# Тренажеры Основы языка программирования Python

# Задание «Проверка логина и пароля»
def check_auth(login: str, password: str) -> str:

    if login == "admin" and password == "password" :
        
        result = "Добро пожаловать"
    else:
        result = "Доступ ограничен"

    return result


# Задание «Знакомство»
def solve(boys: list, girls: list) -> str:
    if len(boys) == len(girls):
        result: str = ""
        for boy, girl in zip(sorted(boys), sorted(girls)):
            if len(result) > 0:
                result += ", "
            result += f"{boy} и {girl}"
    else:
        return "Кто-то может остаться без пары!"
    return result


# Задание «Кто дальше?»
def solve_2(hare_distances: list, turtle_distances: list):
    hare_all = 0
    for hare_distance in hare_distances:
        hare_all += hare_distance
    turtle_all = 0
    for turtle_distance in turtle_distances:
        turtle_all += turtle_distance
    if hare_all > turtle_all:
        result = "заяц"
    elif hare_all < turtle_all:
        result = "черепаха"
    else:
        result = "одинаково"
    return result
