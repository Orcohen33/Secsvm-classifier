import staticAnalyzer
import sys
import os
from glob import glob
result = [y for x in os.walk(sys.argv[1]) for y in glob(os.path.join(x[0], '*.apk'))]
with open(sys.argv[2]+"/results/x.json","a+") as r:
        r.write("[")
r.close()
last=len(result)-1
for i in result:
        ind=result.index(i)
        try:
                staticAnalyzer.run(i, sys.argv[2],ind,last)
        except:
                print("file "+str(ind)+" failed")
                continue
