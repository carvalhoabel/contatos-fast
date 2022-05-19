"""This module is responsible to functions to check all data.
"""
from types import NoneType
from typing import Generator


def str_len(word: str, max: int, null=False) -> bool:
    """This function checks the lenght of a str and the instance.
    It checks:
    - instance of word;
    - if it is allowed None type of empty;
    - else if the lenght is small or equal to max;

    Args:
        word (str): word str to check.
        max (int): max size.
        null (bool, optional): if is allowed None. Defaults to False.

    Returns:
        bool: True if valid else False.
    """
    if not word:
        if isinstance(word, NoneType) or null:
            return True
        else:
            return False
    return False if word.__len__() > max else True


def mobile_checker(mobile: str, max=22) -> bool:
    """This function checks mobile number.

    Args:
        mobile (str): mobile number.
        max (int, optional): allowed size. Defaults to 22.

    Returns:
        bool: True if valid else False.
    """
    if not isinstance(mobile, str):
        return False
    elif max < 1:
        return False
    elif mobile.__len__() > max:
        return False
    else:
        mobile = mobile.strip()
    if not mobile[-1].isnumeric():
        return False
    elif not mobile[0].isnumeric() and mobile[0] != '+' and mobile[0] != '(':
        return False
    elif mobile.count('(') > 1 or mobile.count(')') > 1:
        return False
    elif mobile.count('(') != mobile.count(')'):
        return False
    # inner funtion generator to valid chars

    def valids() -> Generator:
        for val in ('+', '(', ')', '-', ' ',):
            yield val
    # end of inner function
    for char in mobile:
        if char.isnumeric():
            continue
        valid = valids
        for dt in valid():
            if char == dt:
                break
        else:
            return False
    else:
        return True


def get_type_name(obj: object) -> str:
    """Get object type name.

    Args:
        obj (object): object to extract class name.

    Returns:
        str: object class name.
    """
    return obj.__class__.__name__.__str__()


def valid_chars(word: str, valids: Generator) -> bool:
    """Verify if characters are valid.

    Args:
        word (str): word to check.
        valids (Generator): functions generator.

    Returns:
        bool: _description_
    """
    word = word.strip()
    types = ('method_descriptor', 'function')
    valids = tuple(i for i in valids)
    for wd in word:
        items = ()
        for item in valids:
            if get_type_name(item) == types[0] or get_type_name(item) == types[1]:
                items += (item(wd),)
        if True not in items:
            return False
    else:
        return True


def lowchrs(wd: str) -> bool:
    """Returns only lowcase chars of alphabet.

    Args:
        wd (str): str to check.

    Returns:
        bool: True if success else False.
    """
    low = tuple(chr(i) for i in range(97, 123))
    return wd in low


def check_email(email: str, null=True, max=120) -> bool:
    """Check email.

    Args:
        email (str): Email.
        null (bool, optional): if it can be None. Defaults to True.
        max (int, optional): max lenght. Defaults to 120.

    Returns:
        bool: True if valid else False.
    """
    if not str_len(word=email, max=max, null=null):
        return False
    email = email.lower()
    email = email.strip()
    if not email[0].isalpha() or not email[-1].isalpha():
        return False
    # inner function email valid required

    def email_ch(wd: str) -> bool:
        return wd in ('@', '.', '_')
    valids = (lowchrs, email_ch)
    valids = (i for i in valids)
    return valid_chars(word=email, valids=valids, null=null)
