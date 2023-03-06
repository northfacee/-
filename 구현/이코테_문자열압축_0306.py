def solution(s):
    answer = len(s)
    
    for i in range(1,(len(s)//2)+1):
        prev = s[:i]# 왜 +1 이냐 0~4 -> 0 1 2 3 4 홀수일때 아래 포문을 돌리면 하나가 남음
        words = ''
        count = 1
        
        for spl in range(i, len(s), i):
            current = s[spl:spl+i] # i 만큼 끊어줌
            if current == prev: # 이전것과 현재가 같으면(중복되면) 숫자 +1 하고 넘어감
                count +=1
            else: # 이전것과 현재가 다르다
                if count >1: # 근데 그 앞에 중복된것이 있음
                    words += str(count)
                words += prev
                prev = current # 앞의 값을 없애고 그 다음 값을 기준으로 함
                count = 1
            
        if count >1:
            words += str(count)
        words += prev
        answer = min(answer, len(words))
            
    return answer
