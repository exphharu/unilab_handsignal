import os
import glob
import json
import numpy as np
import getangle


#訓練画像からjsonファイルを作り、さらに正解ラベルのリストまで返してくれる関数
def make_json_label(input_folderpath,output_folderpath, labellist, label): #folderpathの例　"./unilabimage/traindata/*"
    
    #フォルダ内のfileのpathをそれぞれ受け取る; 名前順にソートしておく
    filepath = sorted(glob.glob(input_folderpath))
    print(filepath)

    #pathからファイル名だけ切り出してリストに加える
    filename = []
    for f in filepath:
        filename.append(os.path.split(f)[1])
        #正解ラベルをここで自動登録
        labellist.append(label) 
    print(filename)

    # run.pyを実行してjsonを作る
    for i in range(len(filepath)) : 
        os.system('python run.py  --model=mobilenet_thin --resize=432x368  --image={0} --output_json={1} --filename={2}'.format(filepath[i], output_folderpath, filename[i]))

    return labellist


#訓練用写真が保存されたフォルダに対して上のmaketrainlabelを行う
def Pre_training():
    #訓練用の正解ラベル格納リスト
    Y_train = []
    #実際に探索するフォルダ
    make_json_label('./unilabimage/traindata/pose0/*', './outputjson/', Y_train, 0)
    make_json_label('./unilabimage/traindata/pose1/*', './outputjson/', Y_train, 1)
    make_json_label('./unilabimage/traindata/pose2/*', './outputjson/', Y_train, 2)
    make_json_label('./unilabimage/traindata/pose3/*', './outputjson/', Y_train, 3)
    make_json_label('./unilabimage/traindata/pose4/*', './outputjson/', Y_train, 4)
    print(Y_train)
    return Y_train    

#UniLabで実際にとった写真を学習する
def OJ_training():
    #訓練用の正解ラベル格納リスト
    Y_OJtrain = []
    #実際に探索するフォルダ
    make_json_label('./unilabimage/traindata_at_unilab/pose0/*', Y_OJtrain, 0)
    make_json_label('./unilabimage/traindata_at_unilab/pose1/*', Y_OJtrain, 1)
    make_json_label('./unilabimage/traindata_at_unilab/pose2/*', Y_OJtrain, 2)
    make_json_label('./unilabimage/traindata_at_unilab/pose3/*', Y_OJtrain, 3)
    make_json_label('./unilabimage/traindata_at_unilab/pose4/*', Y_OJtrain, 4)
    print(Y_OJtrain)
    return Y_OJtrain   

#UniLabで実際にとった写真を分類する
def OJ_test():
    #訓練用の正解ラベル格納リスト
    y = []
    #実際に探索するフォルダ
    make_json_label('./unilabimage/batch/*', y, 0)
    return

#jsonファイルを渡すとangleのリストを返してくれる関数
def json2angle(PATH):
    filepath = sorted(glob.glob(PATH))
    print(filepath)
    
    #後にanglearrayになる空のリスト
    anglelist = []

    for file in filepath:
        #一つずつロードする
        f = open(file)
        print(file)
        j = json.load(f)
        
        #座標の吸い出し
        A = j["people"][0]["pose_keypoints_2d"]
        #角度特徴量に変換
        angles = getangle.get_angle(A)
        #print(angles)

        
        #リストに追加
        anglelist.append(angles)
        #print(anglelist)

    anglearray = np.array(anglelist)
    return anglearray


#リアルタイム用のjson2angle
def json2angle_realtime(filepath):

    #後にanglearrayになる空のリスト
    anglelist = []

    #一つずつロードする
    f = open(filepath)
    j = json.load(f)
    
    #座標の吸い出し
    A = j["people"][0]["pose_keypoints_2d"]
    #角度特徴量に変換
    angles = getangle.get_angle(A)
    #print(angles)

    #リストに追加
    anglelist.append(angles)
    #print(anglelist)

    anglearray = np.array(anglelist)
    return anglearray

   