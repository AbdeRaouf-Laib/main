from sys import argv
if len(argv) == 2:
    print(f"hello {argv[1]}")
else:
    print(f"hello")
for i in argv:
    if i != 'argv.py':
        print(i)
for i in argv[1: ]:
    print(i)
for i in argv[1:3]:
    print(i)


