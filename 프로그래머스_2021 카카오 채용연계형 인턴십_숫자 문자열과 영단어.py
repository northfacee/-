# 시간복잡도 O(n**2??)



number = {'zero':0,'one':1, 'two':2, 'three':3, 'four':4,'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
def solution(s):
    answer =[]
    eng = []
    for num in s: # 50, n
        if num.isdigit():
            answer.append(int(num))
        else:
            eng.append(num)
            for key,value in number.items(): # 10, n
                if key == ''.join(eng):
                    eng.clear()
                    answer.append(value)
    return int(''.join(map(str, answer)))
