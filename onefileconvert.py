#1ファイルだけ行うためのもの
#フォルダ内の画像をrun.pyしてjsonに書き起こす
#このファイルはなぜかターミナルから実行しないとエラーするので注意

import os
import json
import getangle

filepath = './unilabimage/test1.jpg'
filename = 'test1'

os.system('python run.py  --model=mobilenet_thin  --image={0} --output_json=./outputjson/ --filename={1}'.format(filepath, filename))


#jsonファイルの読み込みとロード
f = open('./output_json/{0}_keypoints.json'.format(filename))
j = json.load(f)

#座標の吸い出し
A = j["people"][0]["pose_keypoints_2d"]

anglelist = getangle.get_angle(A)

print(anglelist)