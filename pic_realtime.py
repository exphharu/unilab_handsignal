#-*- coding: utf-8 -*-
import cv2
import numpy as np
import pickle
from sklearn import svm
import os
import patchwork
import client3

#サーバー立ててからこのファイルを実行しないとエラーするので注意
#cli = client3.InetClient()



def realtime(device_num=0, ext='jpg', delay=1, window_name='frame'):
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
            cv2.imwrite('{}/pic_{}.{}'.format('unilabimage/realtime', count, ext), frame)
 
            filepath = '{}/pic_{}.{}'.format('unilabimage/realtime', count, ext)
            filename = 'pic_{}'.format(count)
            print(filename)
            count += 1

            #画像をjsonに
            os.system('python run.py  --model=mobilenet_thin --resize=432x368  --image={0} --output_json=./realtimejson --filename={1}'.format(filepath, filename))
            #jsonをangleに
            filepath = './realtimejson/' + filename + '_keypoints.json'
            X_pic = patchwork.json2angle_realtime(filepath)
            print(X_pic)
            #推論
            test_result = loaded_svm.predict(X_pic)
            print(test_result)
            if test_result == 0:
                #停止
                #cli.send(str(0))
                print('0')
            elif test_result == 1:
                #前進
                #cli.send(str(40))
                print('40')
            elif test_result == 2:
                #急進
                #cli.send(str(80))
                print('80')       
            elif test_result == 3:
                #後退
                #cli.send(str(-40))
                print('-40')
            elif test_result == 4:
                #急退
                #cli.send(str(-80))
                print('-80')  

        elif key == ord('s'):
            #緊急停止
            #cli.send(str(0))
            print('0')
        elif key == ord('z'):
            #戻る
            #cli.send(str(-40))
            print('-40')
        elif key == ord('x'):
            #進む
            #cli.send(str(40))
            print('+40')

        elif key == ord('q'):
            break



    cv2.destroyWindow(window_name)


#学習済みモデルの読み込み
model = 'trained_svm.pkl'
loaded_svm = pickle.load(open(model, 'rb'))



realtime()



