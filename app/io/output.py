import pathlib


def console_output(message: str):
    print(message)


def file_output(path: str | pathlib.Path, content: str):
    with open(path, 'w') as f:
        f.write(content)
