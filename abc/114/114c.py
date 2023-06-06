def func(tmp, use, cnt):
    if tmp > N:
        return cnt
    
    if use == 0b111:
        cnt.append(1)
        
    func(tmp * 10 + 7, use | 0b001, cnt)
    func(tmp * 10 + 5, use | 0b010, cnt)
    func(tmp * 10 + 3, use | 0b100, cnt)
    
N = int(input())
cnt = []
func(0, 0, cnt)
print(sum(cnt))