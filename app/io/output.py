import pathlib
from typing import Union


def console_output(message: str):
    """
    Write content to the console
    :param message: content
    """
    print(message)


def file_output(path: Union[str, pathlib.Path], content: str):
    """
    Write content to the file
    :param path: path to file
    :param content: content to save
    """
    with open(path, 'w') as f:
        f.write(content)
