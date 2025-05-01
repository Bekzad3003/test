def parse(response: dict) -> list[str]:
    """
    Функция получает JSON-ответ и возвращает список логинов найденных людей.

    :param response: JSON-ответ от API.
    :return: Список логинов.
    """
    return [person["login"] for person in response.get("people", []) if "login" in person]

# Пример использования:
example_response = {
    "people": [
        {"login": "user1"},
        {"login": "user2"},
        {"login": "user3"}
    ]
}

logins = parse(example_response)
print(logins)  # ['user1', 'user2', 'user3']
