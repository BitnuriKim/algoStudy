# https://www.acmicpc.net/problem/10809
# ���� : ���ĺ� ���ڷθ� �̷���� �ܾ� S�� �־�����, �� �������� ó�� �����ϴ� ��ġ ���. ���ĺ��� ���� ���, -1 ���

import sys

def solve():
    input = sys.stdin.readline
    words = str(input())
    array = []

    # ��� (1) - index�� ���ϱ�
    for i in range(97,123):       # ascii �ڵ� : 97~123 (a~z)
        if chr(i) in words:
            index_num = words.index(chr(i))
            array.append(index_num)
        else:
            array.append(-1)

    # ��� (2) - find �Լ� ��� (�̿ϼ�)
#    alphabet = list(map(chr,range(97,123))) # ascii �ڵ� ���� - chr ���

#    index_num = words[i].find(str(alphabet))
#    print(index_num)

#    print(array) # �̷� ���, list ��µǾ� Ʋ�ȴٰ� ��.
    for i in array: # end=" "�� �̿��Ͽ� list�� ������� �ʱ� ���� �κ�
        print(i, end=" ")

if __name__ == "__main__":
    solve()