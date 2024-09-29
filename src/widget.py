from src.masks import get_mask_account, get_mask_card_numbers

date = "2024-03-11T02:26:18.671407"


def mask_account_card(type_and_number_card: str) -> str:
    """Функция маскировки сета карты и номера карты"""

    split_account_or_card = type_and_number_card.split(" ")
    if "Счет" in split_account_or_card[-16:]:
        masked_number = get_mask_account(split_account_or_card[-1])
    else:
        masked_number = get_mask_card_numbers(split_account_or_card[-1])
    split_account_or_card[-1] = masked_number
    return " ".join(split_account_or_card)


def get_date(date: str) -> str:
    """Функция для формата ДД.ММ.ГГГГ"""

    user_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return user_date


print(f'Дата: {get_date("2024-03-11T02:26:18.671407")}')
