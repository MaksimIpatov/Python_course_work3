from src.utils import get_data, filter_data, format_date, last_five_operations, format_card


def test_get_data():
    data = get_data()
    assert type(data) is list
    assert len(data) > 0
def test_filter_data(operations):
    data = filter_data(operations)
    assert data == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": "31957.58",
            "Column5": "руб.",
            "Column6": "RUB",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": "9824.07",
            "Column5": "USD",
            "Column6": "USD",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }

    ]
    assert [operation["id"] for operation in data] == [441945886, 939719570]

def test_format_date():
    assert format_date("2018-06-30T02:08:58.425572") == "30.06.2018"
    assert format_date("2019-08-26T10:50:58.294041") == "26.08.2019"
def test_format_card():
    assert format_card(None) == ""
    assert format_card("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"
    assert format_card("Счет 72731966109147704472") == "Счет **4472"

def test_format_operation():
    test_data = [{'date': '2018-08-26T10:50:58.294041'},
                 {'date': '2023-08-26T10:50:58.294041'},
                 {'date': '2019-08-26T10:50:58.294041'},
                 {'date': '2015-08-26T10:50:58.294041'},
                 {'date': '2019-08-26T10:50:58.294041'},
                 {'date': '2019-08-26T10:50:58.294041'},
                 {'date': '2018-08-26T10:50:58.294041'},
                 {'date': '2019-08-26T10:50:58.294041'},
                 {'date': '2011-08-26T10:50:58.294041'},
                 {'date': '2010-08-26T10:50:58.294041'},
                 {'date': '2008-08-26T10:50:58.294041'},]
    result = last_five_operations(test_data)
    expected_result =  [
                 {'date': '2023-08-26T10:50:58.294041'},
                 {'date': '2019-08-26T10:50:58.294041'},
                 {'date': '2019-08-26T10:50:58.294041'},
                 {'date': '2019-08-26T10:50:58.294041'},
                 {'date': '2019-08-26T10:50:58.294041'}
]
    assert result == expected_result

