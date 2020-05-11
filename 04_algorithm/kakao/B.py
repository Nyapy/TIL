expression = "100-200*300-500+20"

def perm(n,k):
    global answer, nums, exp
    if k == 3:
        local_num = nums
        local_exp = exp
        for i in order:
            tem_nums = []
            tem_exp = []

            num = local_num[0]
            for j in range(len(local_exp)):
                if local_exp[j] == i:
                    next = local_num[j+1]
                    if local_exp[j] == "-":
                        num = num - next
                    elif local_exp[j] == "+":
                        num = num + next
                    elif local_exp[j] == "*":
                        num = num * next

                else:
                    tem_nums.append(num)
                    tem_exp.append(local_exp[j])
                    num = local_num[j+1]

            tem_nums.append(num)
            local_num = tem_nums
            local_exp = tem_exp
        a = tem_nums[0]
        if answer < abs(a):
            answer = abs(a)
        return

    else:
        for i in range(k,n):
            order[i],order[k] = order[k],order[i]
            perm(n,k+1)
            order[i],order[k] = order[k],order[i]

nums = []
exp = []
tem = ""

order = ["-","+","*"]
for i in expression:
    if 48 <= ord(i) <=57:
        tem += i

    else:
        nums += [int(tem)]
        tem = ""
        exp += i
nums += [int(tem)]

answer = 0


perm(3,0)

print(answer)