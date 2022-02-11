import random


def encode(input_bytes: bytearray, columns: str) -> bytearray:
    columns_count = len(columns)
    result = bytearray()
    while len(input_bytes) % columns_count != 0:
        input_bytes.extend(b'z')
    bytes_count = len(input_bytes)
    for column_iterator in range(1, columns_count + 1):
        index_of_next_column = columns.index(str(column_iterator)) + 1
        for bytes_iterator in range(index_of_next_column, bytes_count + 1, columns_count):
            resulting_byte = input_bytes[bytes_iterator - 1]
            result.append(resulting_byte)
    return result


"""
5147263
abcdefg
hijklmn
opqrstu
wxyzzzz

bipx-elsz-gnuz-cjqy-ahow-fmtz-dkrz
bipx-elsz-gnuz-cjqy-ahow-fmtz-dkrz')

"""


def decode(input_bytes: bytearray, columns: str) -> bytes:
    columns_count = len(columns)
    rows_count = len(input_bytes) // columns_count
    rows_usage = [0 for _ in range(columns_count)]
    result = bytearray()
    for i in range(len(input_bytes)):
        current_column = int(columns[i % columns_count])
        bytes_before = (current_column - 1) * rows_count
        desired_byte = bytes_before + rows_usage[current_column - 1]
        result.append(input_bytes[desired_byte])
        rows_usage[current_column - 1] += 1
    return result


def make_padding(input_bytes: bytearray, columns: str):
    columns_count = len(columns)
    while len(input_bytes) % columns_count != 0:
        input_bytes.extend(b'z')


def validate_input(columns: str) -> bool:
    if not columns.isnumeric():
        return False
    return True


def main(input_filename: str,
         output_filename: str,
         columns: str,
         mode: str = "encode"):
    with open(input_filename, "rb") as file:
        input_bytes = bytearray(file.read())
    if mode == "encode":
        make_padding(input_bytes, columns)
        output_bytes = encode(input_bytes, columns)
    elif mode == "decode":
        output_bytes = decode(input_bytes, columns)
    else:
        output_bytes = b''
    with open(output_filename, "wb") as file:
        file.write(output_bytes)


def assertion(string: str, columns: str):
    input_bytes = bytearray(string, "utf-8")
    make_padding(input_bytes, columns)
    encoded_bytes = encode(input_bytes, columns)
    decoded_bytes = decode(encoded_bytes, columns)
    actual = decoded_bytes.decode("utf-8")
    assert actual[:len(string)] == string, f"actual and expected differ: expected {string}, but decoded {actual}"


def debug(tests_count: int = 1000):
    string = "1234567890-=!@#$%^&*()_+qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?~`\\"
    for i in range(tests_count):
        columns_count = random.randint(1, 9)
        string_length = random.randint(1, 100)
        string = "".join([random.choice(string) for _ in range(string_length)])
        columns_array = []
        for j in range(1, columns_count + 1):
            columns_array.append(str(j))
        random.shuffle(columns_array)
        columns = "".join(columns_array)
        assertion(string, columns)


if __name__ == "__main__":
    main("encoded.txt", "decode.txt", '5147263', "decode")
    # try:
    #     debug()
    # except AssertionError as e:
    #     print(e)
