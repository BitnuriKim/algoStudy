# https://www.acmicpc.net/problem/11720

# ���� : N���� ���ڸ� ��� ���Ͽ� ���

def solve():
    N_of_num = int(input())
    num = str(input())  # str[index]
    sum_num = i = 0
    
    while i < N_of_num:
        sum_num = sum_num + int(num[i])
        i += 1
     
    print(sum_num)

if __name__ == "__main__":
    solve()