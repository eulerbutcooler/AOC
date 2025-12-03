
# simply counts the number of times the dial hits 0
def part1():
    dial=50
    zerocount=0
    with open('day1input.txt', 'r') as file:
        for line in file:
            direction=line[0]
            steps=int(line[1:])
            if direction=='L':
                dial=(dial-steps)%100
            else:
                dial=(dial+steps)%100
            if dial==0:
                zerocount+=1
    print(f"Zerocount in part1: {zerocount}")
    
part1()

# math method
# instead of thinking of dial as a circle thinking of it as an infinite number line
# for L: (start-end)//100 -> we count how many times do we hit a multiple of 100
# for L: start = (dial-1)//100 and end = (dial-steps-1)//100
# -1 in both start and end is to ensure inclusivity for the range
# also 99//100 = 0 but -1//100 = -1
def part2():
    dial=50
    zerocount=0
    with open('day1input.txt', 'r') as file:
        for line in file:
            direction=line[0]
            steps=int(line[1:])
            if direction=='L':
                zerocount += (dial - 1) // 100 - (dial - steps - 1) // 100
                dial=(dial-steps)%100
            else:
                zerocount += (dial + steps) // 100
                dial=(dial+steps)%100

    print(f"Zerocount in part2: {zerocount}")
    
part2()


# naive loop method
def part2():
    dial=50
    zerocount=0
    with open('day1input.txt', 'r') as file:
        for line in file:
            direction=line[0]
            steps=int(line[1:])
            
            for _ in range(steps):
                if direction == 'L':
                    dial = (dial - 1) % 100
                else:
                    dial = (dial + 1) % 100
                
                if dial == 0:
                    zerocount+=1
    print(f"Zerocount in part2: {zerocount}")

part2()