# ���� : ���� A,B�� �Է� �޾� A/B�� ���

def solve():
    # A,B = map(int,input().split(" "))
    A,B = map(float,input().split(" "))
    if A > 0 and B < 10:
        print(A/B)
    else:
        print("wrong input")

if __name__ == "__main__":
    solve()