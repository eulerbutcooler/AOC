def reading():
    dialen = 100
    dial=50
    zerocount=0
    with open('day1input.txt', 'r') as file:
        for line in file:
            direction=line[0]
            steps=int(line[1:])
            if direction=='L':
                dial=(dial-steps)%dialen
            elif direction=='R':
                dial=(dial+steps)%dialen
            if dial==0:
                zerocount+=1
            print(f"{line} -> Dial position: {dial}")
           
    print(f"Zero counts: {zerocount}")
    
reading()
            