# https://www.acmicpc.net/problem/1110

# �Է� : 0~99 ������ ���� (0 < N < 99)
# ��� : N�� ����ũ ���� ���

def sum_up():
    N = new_num = int(input())
    cnt = 0
    
    while True:
        sum_num = new_num//10 + new_num%10 # 10�� �ڸ� + 1�� �ڸ�
        new_num = int(new_num%10)*10 + int(sum_num%10)
        # new_num = int(str(new_num%10) + str(sum_num%10))
        cnt = cnt + 1
        if (new_num == N):
            break
    print(cnt)

if __name__ == "__main__":
    sum_up()