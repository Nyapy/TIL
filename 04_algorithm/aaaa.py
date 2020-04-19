# N = 3
# T = list(range(N+1))
# print(T)
# for i in range(1,1<<N):
#     for j in range(N):
#         if i & (1<<j):
#             print(T[j], end=" ")
#     print()
#
#
# a = [1,2]

# answers = [1,2,3,4,5]
#
# def solution(answers):
#     answer = []
#     one = [1, 2, 3, 4, 5]
#     two = [2, 1, 2, 3, 2, 4, 2, 5]
#     three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     cnt = [0, 0, 0]
#     for i in range(len(answers)):
#         o = i % 5
#         t = i % 8
#         th = i % 10
#         if answers[i] == one[o]:
#             cnt[0] += 1
#         if answers[i] == two[t]:
#             cnt[1] += 1
#         if answers[i] == three[th]:
#             cnt[2] += 1
#     ans = 0
#     for i in cnt:
#         if i > ans:
#             ans = i
#     for i in range(len(cnt)):
#         if ans == cnt[i]:
#             answer.append(i+1)
#
#     return answer
#
# print(solution(answers))

a,b,c, = [1,2,3]

print(a)