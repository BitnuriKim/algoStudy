#https://www.acmicpc.net/problem/5622

def solve(): #틀렸다고 나오는데.. 반례를 못 찾겠는데...
    dial={}
    start = ord('A')
    for i in range(8): #다이얼
        if i == 5 or i == 7:
            dial[i+2] = chr(start+3*i)+chr(start+3*i+1)+chr(start+3*i+2)+chr(start+3*i+3)
        else:
            dial[i+2] = chr(start+3*i)+chr(start+3*i+1)+chr(start+3*i+2)
    char = input()
    t = 0
    for x in char:
        for k in dial:
            if x in dial[k]:
                t+=k+1
    print(t)
    
def solve2(): #유니코드 이용하여 풀기
    char = input()
    time = len(char) # 시간은 각 문자에 해당하는 다이얼+1이기 때문에 한번에 먼저 계산.
    for x in char:
        if 65 <= ord(x) and ord(x) <68 : time+=2
        elif  68 <= ord(x) and ord(x)<71 : time+=3
        elif  71 <= ord(x) and ord(x)<74 : time+=4
        elif  74 <= ord(x) and ord(x)<77 : time+=5
        elif  77 <= ord(x) and ord(x)<80 : time+=6
        elif  80 <= ord(x) and ord(x)<84 : time+=7
        elif  84 <= ord(x) and ord(x)<87 : time+=8
        elif  87 <= ord(x) and ord(x)<91 : time+=9
        else: continue
    print(time)
if __name__=="__main__":
    solve2()