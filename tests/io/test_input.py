import json
from unittest.mock import Mock, mock_open, patch

import pandas as pd

from app.io import input


def test_console_input(mocker):
    expected_val = "expected"

    mock = Mock(return_value=expected_val)
    mocker.patch("builtins.input", mock)

    assert input.console_input() == expected_val


file_input_expected = "data"


@patch("builtins.open", new_callable=mock_open, read_data=file_input_expected)
def test_file_input(mocker):
    filename = "file"

    assert input.file_input(filename) == file_input_expected


def test_pandas_input(mocker):
    mocker.patch(
        "pandas.io.json._json.JsonReader._get_data_from_filepath",
        return_value=json.dumps([{"a": "b"}, {"a": "c"}]),
    )

    actual = input.file_input_pandas("whatever.json")
    expected = pd.DataFrame.from_dict({"a": ["b", "c"]})

    assert actual.equals(expected)
