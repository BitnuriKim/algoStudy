# ���� : ù° �ٿ��� �� 1��, ��° �ٿ��� �� 2��, N��° �ٿ��� �� N��

def star():
    N = int(input())
    
    if 1<=N<=100:
        for i in range(N): # range(stop-1) : default setup = index(stop-1)
            print("*"*(i+1))
    else:
        return 0

if __name__ == "__main__":
    star()