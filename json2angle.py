#jsonファイルから特定の座標情報を手に入れる
# getangle.pyの関数を読んで行なっている

import json
import glob
import numpy as np
import getangle


"""
#jsonファイルの読み込みとロード
f = open('./output_json/sample3.jpg_keypoints.json')
j = json.load(f)

#座標の吸い出し
A = j["people"][0]["pose_keypoints_2d"]

anglelist = getangle.get_angle(A)

print(anglelist)
"""


#jsonファイルを渡すとangleのリストを返してくれる関数
def json2angle():
    filepath = sorted(glob.glob("./outputjson/*"))
    #print(filepath)
    
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


