import pickle
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import json2angle
import getangle
import json
import patchwork

import client3
#cli = client3.InetClient()


#学習時はonに
Pretrain = True
OnJobtrain = False

# modelの設定
clf = svm.SVC(C=1.0, kernel='rbf', gamma=1.6, decision_function_shape='ovr')

if Pretrain:
    # 訓練画像をjsonに＆正解ラベル取得 
    y =patchwork.Pre_training()
    Y = np.array(y)
    # 特徴量
    X = patchwork.json2angle("./outputjson/*")
    print(X)
    # modelの設定
    #clf = svm.SVC(C=1.0, kernel='rbf', gamma='auto', decision_function_shape='ovr')

    # データに最適化
    clf.fit(X, Y)

    # データを分類器に与え、予測を得る
    result = clf.predict(X)
    
    print('correct label are {0}'.format(Y))
    print('predictions are   {0}'.format(result) )

    # データ数をtotalに格納
    total = len(X)
    # ターゲット（正解）と予測が一致した数をsuccessに格納
    success = sum(result==y)

    # 正解率をパーセント表示
    print('正解率')
    print(100.0*success/total)

    # モデルを保存する
    filename = 'trained_svm.pkl'
    pickle.dump(clf, open(filename, 'wb'))

if OnJobtrain:
    # 訓練画像をjsonに＆正解ラベル取得 
    y =patchwork.OJ_training()
    Y = np.array(y)
    # 特徴量
    X = patchwork.json2angle()

    # modelの設定
    #clf = svm.SVC(C=1.0, kernel='rbf', gamma='auto', decision_function_shape='ovr')

    # データに最適化
    clf.fit(X, Y)

    # データを分類器に与え、予測を得る
    result = clf.predict(X)
    print(X)
    print('correct label are {0}'.format(Y))
    print('predictions are   {0}'.format(result) )

    # データ数をtotalに格納
    total = len(X)
    # ターゲット（正解）と予測が一致した数をsuccessに格納
    success = sum(result==y)

    # 正解率をパーセント表示
    print('正解率')
    print(100.0*success/total)

    # モデルを保存する
    filename = 'trained_svm_oj.pkl'
    pickle.dump(clf, open(filename, 'wb'))