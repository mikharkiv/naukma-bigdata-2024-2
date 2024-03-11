import pathlib

import pandas as pd


def console_input(prompt: str = "Your input: ") -> str:
    return input(prompt)


def file_input(path: str | pathlib.Path) -> str:
    with open(path, "r") as file:
        return file.read()


def file_input_pandas(path: str | pathlib.Path) -> pd.DataFrame:
    return pd.read_json(path)
