from base64 import b64encode


def main(filename: str):
    result = {}
    with open(filename, "rb") as file:
        byte = file.read(1)
        while byte != b'':
            if result.get(byte) is not None:
                result[byte] += 1
            else:
                result[byte] = 0
            byte = file.read(1)
    for key in result.keys():
        print(f"{b64encode(key)}: {result[key]}")


if __name__ == "__main__":
    main('first_task.docx')
