from unittest.mock import Mock, mock_open, patch

from app.io import output


def test_console_output(mocker):
    expected_val = "expected"

    mock = Mock(return_value=expected_val)
    mocker.patch("builtins.print", mock)

    output.console_output(expected_val)

    mock.assert_called_with(expected_val)


@patch("builtins.open", new_callable=mock_open)
def test_file_output(patched):
    file_output_expected = "data"
    output.file_output("whatever", file_output_expected)
    assert patched.mock_calls[-1].assert_called_with(file_output_expected)
