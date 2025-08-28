from contextlib import contextmanager
0@contextmanager
def open_files(*files):
    """Context manager to open multiple files and ensure all are closed."""
    opened = []
    try:
        for file_args in files:
            if isinstance(file_args, tuple):
                f = open(*file_args)
            else:
                f = open(file_args)
            opened.append(f)
        yield opened
    finally:
        for f in opened:
            try:
                f.close()
            except Exception:
                pass

# code1
with open_files(("example.txt", "w")) as (f,):
    f.write("Hello, World!")

# code2
with open_files(("data1.txt", "w"), ("data2.txt", "w")) as (f1, f2):
    f1.write("First file content\n")
    f2.write("Second file content\n")
print("files written successfully")

# code3
try:
    with open_files(("input.txt", "r"), ("output.txt", "w")) as (infile, output):
        for line in infile:
            output.write(line.upper())
    print("processing done")
except FileNotFoundError as e:
    print(f"Error: {e}")

# code4
try:
    with open_files(("numbers.txt", "r")) as (f,):
        nums = f.readlines()
    squares = []
    for n in nums:
        n = n.strip()
        if n.isdigit():
            squares.append(int(n) * int(n))
    with open_files(("squares.txt", "w")) as (f2,):
        for sq in squares:
            f2.write(str(sq) + "\n")
    print("squares written")
except FileNotFoundError as e:
    import traceback
    print("Error:", e)
    traceback.print_exc()