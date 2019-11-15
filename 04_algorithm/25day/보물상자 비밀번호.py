import sys
sys.stdin = open('보물상자 비밀번호.txt')
T= int(input())

for tc in range(1,1+T):
    N,K = map(int, input().split())
    psw = list(input())
    candi = set()
    side = N//4
    for i in range(side):

        for j in range(0, len(psw), side):
            tem = ''
            for k in range(side):
                tem += psw[j+k]
            candi.add(tem)
        psw.insert(0,psw.pop())

    dap = []
    for i in candi:
        dap.append(i)

    dap.sort(reverse=1)
    ans = 0
    n = 0

    for a in range(len(dap[K-1])-1, -1, -1):
        if  ord('0')<= ord(dap[K-1][a]) <= ord('9'):
            ans += int(dap[K-1][a])*(16**n)
        else:
            ans += (ord(dap[K-1][a])-ord('A')+10)*(16**n)
        n += 1

    print('#{} {}' .format(tc, ans))
