x,y,r,d, = -1,2,2,60
target = [[0, 1], [-1, 1], [1, 0], [-2, 2]]

from math import pi, atan2, sqrt

def solution(x,y,r,d,target):
    skillshot = atan2(y,x)*180/pi ## 스킬 찍은 지점의 각도를 구함 x축 기준으로 반시계 방향 각도

    answer = 0
    for tar in target:
        tx,ty = tar
        vdeg = atan2(ty,tx)*180/pi ## 각 타겟이 있는 지점의 각도를 구해서

        if skillshot-60 <= vdeg <= skillshot+60: ## 타겟이 각도(스킬 샷에서 -60 ~ 60 사이에 있는지 확인)
           if r >= sqrt(tx ** 2 + ty ** 2): ## 범위 내에 있으면 거리가 r 내에 있는지 확인
               answer += 1 ## 모든 조건을 만족하면 스킬 범위 내에 있는 것이므로 숫자 +1

    return(answer)
