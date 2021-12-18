import os

print("Starting")

os.chdir("C:\Users\jakob\Documents\Gamemaking\AllGoodKingsARG\CheckBehindTheBarn")
print(os.getcwd())
for a in range(1,6):
    for b in range(1,6):
        for c in range(1,6):
            for d in range(1,6):
                for e in range(1,6):
                    dir = "/"+str(a)+"/"+str(b)+"/"+str(c)+"/"+str(d)+"/"+str(e)

                    if not os.path.exists(dir):
                        os.mkdir(dir)
print("Done")
