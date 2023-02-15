# 시간복잡도 -> O(n)??

# 아이디어 -> 집합 교집합 차힙합 활용? -> 겹치는게 안됨
# 같은수와 다른수 카운트해서 함

def solution(lottos, win_nums):
    dif = 0 # 다른수
    same = 0 # 같은수
    
    for num in lottos:
        if num not in win_nums:
            if num == 0:
                dif +=1
        else:
            same+=1
    max_lotto = 7-(same + dif) # 7-4 = 3
    min_lotto = 7-same # 7-2 =5
    if min_lotto >=7:
        min_lotto = 6
    if max_lotto>=7:
        max_lotto=6
    
    return max_lotto, min_lotto
