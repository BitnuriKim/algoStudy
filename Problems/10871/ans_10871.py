# https://www.acmicpc.net/problem/10871

# �Է� : ���� N���� �̷���� ���� A�� ���� X
# ��� : X���� ���� ���� �Է� ���� ������� ���

def compare():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    # input().split()) -> output = string type
    # map(int,input().split()) -> output = map object at address
    
    for i in range(N):
        if A[i] < X :
            print(A[i], end=" ")

if __name__ == "__main__":
    compare()    