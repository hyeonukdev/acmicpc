A = int(input())
B = int(input())

if 0 < A and 0 < B:
    print("1")
elif 0 < A and B < 0:
    print("4")
elif A < 0 and 0 < B:
    print("2")
else:
    print("3")