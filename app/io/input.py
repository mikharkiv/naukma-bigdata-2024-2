import pathlib
from typing import Union

import pandas as pd


def console_input(prompt: str = "Your input: ") -> str:
    """
    Read user's input from console
    :param prompt: prompt
    :return: user's input
    """
    return input(prompt)


def file_input(path: Union[str, pathlib.Path]) -> str:
    """
    Read user's input from file
    :param path: path to file
    :return: file content
    """
    with open(path, "r") as file:
        return file.read()


def file_input_pandas(path: Union[str, pathlib.Path]) -> pd.DataFrame:
    """
    Read Pandas DataFrame from JSON file
    :param path: path to JSON file
    :return: DataFrame made from JSON
    """
    return pd.read_json(path)
