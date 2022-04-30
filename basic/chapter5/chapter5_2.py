

def count_lines(fl):
    return len(fl.readlines())


def count_chars(fl):
    return len(fl.read())


def test(fl):
    print(fl, "lines: ", count_lines(fl), sep=" ", end="\n")
    fl.seek(0)
    print(fl, "chars: ", count_chars(fl), sep=" ", end="\n")


if __name__ == "__main__":
    import sys
    # print(sys.argv)
    # print(type(sys.argv))
    if len(sys.argv) == 2:
        test(open(sys.argv[1], "r", encoding="utf-8"))
    elif len(sys.argv) == 1:
        test(open(sys.argv[0], "r", encoding="utf-8"))
    else:
        test(open("chapter5_2.py", "r", encoding="utf-8"))
