def part1():
    with open("day2input.txt", "r") as file:
        for line in file:
            total=0
            IDrange = line.split(',')
            for r in IDrange:
                parts=r.split('-')
                Rstart=int(parts[0])
                Rend=int(parts[1])
                for i in range(Rstart,Rend+1):
                    if len(str(i))%2!=0:
                        # print(f"skipped num: {i}")
                        continue
                    else:
                        halflen=len(str(i))//2
                        if str(i)[:halflen]==str(i)[halflen:]:
                            newsum=int(str(i)[:halflen]+str(i)[halflen:])
                            total+=newsum
                        
                        
            print(total)
                    
part1()
                    
def isInvalid(n:int)->bool:
    s = str(n)
    length = len(s)
    if length == 1:
        return False
    for L in range(1,length//2+1):
        if length % L != 0:
            continue
        block = s[:L]
        repeats = length // L
        if block * repeats == s:
            return True
    return False
                 

def part2():
    total = 0 
    with open("day2input.txt", "r") as file:
        for line in file:
            IDranges = line.split(',')
            for r in IDranges:
                parts = r.split('-')
                Rstart = int(parts[0])
                Rend = int(parts[1])
                for i in range(Rstart, Rend + 1):
                    if isInvalid(i):
                        total += i
    print(total)

part2()