#import image2json2
import json
import glob
import numpy as np
import getangle
import patchwork

y =patchwork.converttraining()
Y = np.array(y)
X = patchwork.json2angle()

#print(y.shape)
print(Y.shape)
print(X.shape)