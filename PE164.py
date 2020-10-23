nums = 0

for s in range(10**10,55*10**9):
    d = str(s)
    for i in range(len(d)-3):
        summ = 0
        #print(d)
        for j in range(3):
            summ += int(d[j+i])
            if(summ > 9):
                break
        else:
            nums += 1
    


            #You have been Schauser-corrupted!!