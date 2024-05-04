from typing import Union

from tune_password.tune_logic import add_comments, sanitize_password, tune_special_symbols


def remove_excess_password_io(password: str) -> str:
    """
    firstly removes _ and - for the password
    secondly change lower => upper; upper => lower; removes digits
    """
    items: list = ['_', '-']

    symbols: str = input(
        f"""
         choose and write symbobls from {items}
         without spaces and commas that we need to delete
         if u dont need to press enter
         """)
    if symbols is not None:
        password: str = tune_special_symbols(password, symbols)

    items: list = ['up', 'low', 'dig']
    print(f"""
          choose and write words from {items} that we need to delete
          if u dont need to press enter
          for example: low deleting whole lower letters from the password
          """)

    symbols: Union[str, None] = input()
    if symbols is not None:
        password: str = sanitize_password(password, symbols.lower())

    return password


def comments_to_password_io(password: str) -> str:
    """
    adding comment to the password
    it can help you have a few accs in 1 store
    can add some info about password; (-time: creation data), (-len: length)
    """

    comment: Union[str, None] = input(
        """
        You can add some comments to password, it can help you if:
        You have a few accs in 1 app and want to see more information
        Write your commentary, also you can use this commands:
        (-time: creation data), (-len: length)
        press enter if you dont want to have it
        """)
    if comment is not None:
        password = add_comments(password, comment)

    return password


if __name__ == '__main__':
    print('You cant run this file as main!')
