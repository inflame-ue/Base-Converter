from stack import Stack


def base_converter(decimal: int, base: int) -> str:
    """
    This function converts a decimal to any base from 2 to 16 by using the divide by base algorithm.
    :param decimal: number to convert
    :param base: base to which you want to convert the number
    :return: number in given base represented by a string
    """
    digits = "0123456789ABCDEF"
    stack = Stack()
    base_str = ""

    while decimal > 0:
        digit = decimal % base
        decimal = decimal // base
        stack.push(digit)

    while not stack.is_empty():
        base_str = base_str + digits[stack.pop()]

    return base_str
