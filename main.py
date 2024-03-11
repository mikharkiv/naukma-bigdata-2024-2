from app.io import input, output


def main():
    user_input = input.console_input("Enter your message:")
    output.console_output(user_input)

    file_input = input.file_input("data/test.json")
    output.file_output("data/output.json", file_input)

    df = input.file_input_pandas("data/test.json")
    print(df)


if __name__ == '__main__':
    main()
