def part1():
    total=0
    with open('day3input.txt', 'r') as file:
        for line in file:
            line=line.strip()
            bestdigit=int(line[-1])
            bestvalue=0
            for i in range(len(line)-2,-1,-1):
                curdigit=int(line[i])
                curval=10*curdigit+bestdigit
                if curval>bestvalue:
                    bestvalue=curval
                    print(f"current best value: {bestvalue}")
                if curdigit>bestdigit:
                    bestdigit=curdigit
                    print(f"besdigit in first if: {bestdigit}")
            total+=bestvalue
                    
    print(total)
    
# part1()


# Not the prettiest code but eh it works. debugger came handy lol
def part2():
    total=0
    with open('day3input.txt', 'r') as file:
        for line in file:
            line=line.strip()
            bestdigit=0
            i=0
            lastind=-1
            while i<=12:
                total+=10**(12-i)*bestdigit
                bestdigit=0
                for j in range(lastind+1,len(line)):
                    if len(line[j:])>(11-i):
                        curdigit=int(line[j])
                        if curdigit>bestdigit:
                            bestdigit=curdigit
                            lastind=j
                i+=1
    print(total)
part2()