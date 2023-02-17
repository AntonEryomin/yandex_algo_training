phone_to_add = input()
phone_a = input()
phone_b = input()
phone_c = input()


def normalized_phone(phone: str) -> str:
    """
    Метод, производящий нормализацию входящей записи номера телефона к стандартному: +7(код города)*******
    """
    number = []
    code = []
    rp = len(phone) - 1

    while rp >= 0:

        if phone[rp] not in ("(", ")", "-", "+"):
            current_num = phone[rp]
        else:
            current_num = -1
        if len(number) < 7 and current_num != -1:
            number.insert(0, str(current_num))
        elif len(code) < 3 and current_num != -1:
            code.insert(0, str(current_num))
        rp -= 1

    if len(code) == 0:
        code = ['4', '9', '5']
    return f"+7({''.join(code)}){''.join(number)}"


def phone_compare(phone_a: str, phone_b: str) -> str:
    if normalized_phone(phone_a) == normalized_phone(phone_b):
        return "YES"
    else:
        return "NO"


print(phone_compare(phone_to_add, phone_a))
print(phone_compare(phone_to_add, phone_b))
print(phone_compare(phone_to_add, phone_c))
