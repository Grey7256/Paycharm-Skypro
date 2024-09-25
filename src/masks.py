def get_mask_card_numbers(card: str) -> str:
    """функция маскировки  карты"""
    operation_list = list()
    operation_list.append(card[0:4])
    operation_list.append(card[4:6] + "**")
    operation_list.append("****")
    operation_list.append(card[12:])
    return " ".join(operation_list)


def get_mask_account(ac_number: str) -> str:
    """функция маскировки счета"""
    new_list = list()
    new_list.append("**" + ac_number[-4:])
    return " ".join(new_list)


account_number = 73654108430135874305
card_number = 5999414228426353
print(f"Visa Gold: {(get_mask_card_numbers(str(card_number)))}")
print(f"Счет: {(get_mask_account(str(account_number)))}")
