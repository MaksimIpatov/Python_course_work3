import json

from src.config import OPERATIONS_PATH


def get_data():
    """Чтение данных из папки data  и возвращает"""
    with open(OPERATIONS_PATH, encoding="utf-8") as f:
        return json.load(f)


def filter_data(data):
    """операции с значением ключа"""
    filter_operations = [operation for operation in data if operation and operation.get("state") == "EXECUTED"]
    return filter_operations


def last_five_operations(data):
    """Сортировка и вывод"""
    sorted_operations = sorted(data, key=lambda x: x["date"], reverse=True)
    return sorted_operations[:5]

def format_date(date: str):
    """Возвращает строку даты в виде ДД.ММ.ГГГГ """
    date_format = date.split("T")[0].split("-")[::-1]
    return ".".join(date_format)


def format_card(card: str):
    """Сокрытие счетов XXXX"""
    if card is None:
        return ''
    card = card.split()
    card_number = card.pop()
    card_name = " ".join(card)
    if card_name.lower() == "счет":
        number_secret = "**" + card_number[-4:]
    else:
        number_secret = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_name} {number_secret}"

def format_operation(operation:dict):
    """
    # Пример вывода для одной операции:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.

    """
    first_line = format_date(operation['date']) + ' ' + operation['description']
    second_line = format_card(operation.get('from')) + ' => ' + format_card(operation['to'])
    third_line = operation['operationAmount'] + ' ' + operation['Column5']
    #print(operation)
    return '\n'.join([first_line, second_line, third_line])