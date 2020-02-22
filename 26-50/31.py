count = 0

for i in range(0,200):
    print(i)
    for j in range(0,100):
        for k in range(0,40):
            for l in range(0,20):
                for m in range(0,10):
                    for n in range(0,4):
                        for o in range(0,2):
                            if(i*1 + j*2 + k*5 + l*10 + m*20 + n*50 + o*100 == 200):
                                count += 1

print(count+1+1+1+1+1+1+1+1) # The ones come from removing obvious combinations from loops to make them run faster ie: 200*1, 100*2, etc
