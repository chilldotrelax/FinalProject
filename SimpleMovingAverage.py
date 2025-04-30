'''
Andy Huang ECE 160 (creepto sma calculator.)

'''

while True: #Pure retardium special >:)
    num_Days = int(input())

    if num_Days == 1:
        t_and_w = input().split()
        data = input().split()
        t = int(t_and_w[0])
        w = int(t_and_w[1])

        #Calculate sma at specific t.
        for i in range(1,(t + 1)): #t = 1, 2, 3, 4, ...
            summedValue = 0
            for j in range(1,10):
                if (i - w) + j <= i and ((i - w) + j) > 0:
                    summedValue += (float(data[((i - w) + j) - 1]) / w)
            print(f'{summedValue:.2f}',end=' ')
        break
    
    elif num_Days > 1:
        t_and_w = input().split()
        data = input().split()
        t = int(t_and_w[0])
        w = int(t_and_w[1])

        #Calculate sma at specific t.
        for i in range(1,(t + 1)): #t = 1, 2, 3, 4, ...
            summedValue = 0
            for j in range(1,10):
                if (i - w) + j <= i and i > 0:
                    summedValue += (float(data[((i - w) + j) - 1]) / w)
            print(f'{summedValue:.2f}',end=' ')
        
        num_Days += -1
        continue        
    
    else: break


