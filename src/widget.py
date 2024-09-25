from .masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(number: str) -> str:
    """маскировка счет-карта"""

    if len(number.split()[-1]) == 16:
        new_number = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[:20]}{new_number}"
    return result


def get_date(user_date: str) -> str:
    """Функция получения даты и времени в формате ДД.ММ.ГГГГ"""

    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
