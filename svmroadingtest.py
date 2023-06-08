import numpy as np
import pickle
from sklearn import svm
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import json2angle
import getangle
import json
import patchwork
import time

import client3
#cli = client3.InetClient()

X_test = np.array([[  0.12539315, -0.32315829, -0.99852574, -0.99951975],
                    [ 0.21818836, -0.19128591, -0.99965407, -0.99963343], 
                    [ 0.34740685, -0.06554687, -0.62535462, -0.65699034]])


#学習済みモデルの読み込み
filename = 'trained_svm.pkl'
loaded_svm = pickle.load(open(filename, 'rb'))

test_result = loaded_svm.predict(X_test)
print(test_result)

for i in range(len(test_result)):
    if test_result[i] == 0:
        #停止
        #cli.send(str(0))
        print('0')
        time.sleep(2)
    elif test_result[i] == 1:
        #前進
        #cli.send(str(40))
        print('40')
        time.sleep(2)
    elif test_result[i] == 2:
        #急進
        #cli.send(str(80))
        print('80') 
        time.sleep(2)       
    elif test_result[i] == 3:
        #後退
        #cli.send(str(-40))
        print('-40')
        time.sleep(2)
    elif test_result[i] == 4:
        #急退
        #cli.send(str(-80))
        print('-80')
        time.sleep(2)   
#停止して終了        
#cli.send(str(0))        
print('0')       