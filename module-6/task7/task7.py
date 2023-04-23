source = "source.txt"
output = "output.txt"


def sanitize_file(source, output):
    result = ""

    with open(source, "r") as fh:
        text = fh.read()
        result = "".join(z for z in text if not z.isdigit())

    with open(output, "w") as fh:
        fh.write(result)


sanitize_file(source, output)
