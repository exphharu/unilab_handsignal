#-*- coding: utf-8 -*-
import cv2
import numpy as np
import pickle
from sklearn import svm
import os
import patchwork
import time
import client3
cli = client3.InetClient()


# まず写真を撮り、それがunilab/batchにほぞんされる。qを押して撮影は終了する
def takepic(device_num=0, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    n = 0
    count = 0

    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('1'):
            cv2.imwrite('{}/pic_{}.{}'.format('unilabimage/batch', count, ext), frame)
 
            filepath = '{}/pic_{}.{}'.format('unilabimage/batch', count, ext)
            filename = 'pic_{}'.format(count)
            print(filename)
            count += 1   

        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)

    return


#撮った写真をangle（特徴量X）に直す
def picbatch2angle():
    print('START PIC TO ANGLE')
    dummy = []
    patchwork.make_json_label('unilabimage/batch/*','./batchjson/', dummy, 0)
    #jsonをangleに
    X_batch = patchwork.json2angle('./batchjson/*')
    print(X_batch)
    
    return X_batch


#実際に推論してシグナルを送る
def predpic(): 
    print('START PREDICTION')
    X_batch = picbatch2angle()
    #学習済みモデルの読み込み
    model = 'trained_svm.pkl'
    loaded_svm = pickle.load(open(model, 'rb'))

    #推論
    test_result = loaded_svm.predict(X_batch)
    print(test_result)

    v = input("電車を動かす準備が出来ました > ")
    for i in range(len(test_result)):
        if test_result[i] == 0:
            #停止
            cli.send(str(0))
            print('0')
            time.sleep(8)
        elif test_result[i] == 1:
            #前進
            cli.send(str(40))
            print('40')
            time.sleep(8)
        elif test_result[i] == 2:
            #急進
            cli.send(str(80))
            print('80') 
            time.sleep(8)       
        elif test_result[i] == 3:
            #後退
            cli.send(str(-40))
            print('-40')
            time.sleep(8)
        elif test_result[i] == 4:
            #急退
            cli.send(str(-80))
            print('-80')
            time.sleep(8)   
    #停止して終了        
    cli.send(str(0))        
    print('0')  


takepic(device_num=0, ext='jpg', delay=1, window_name='frame') 
predpic()

   