import os
import glob

"""
#フォルダ内のfileのpathをそれぞれ受け取る
filepath = glob.glob("./unilabimage/traindata/*")
print(filepath)

#pathからファイル名だけ切り出してリストに加える
filename = []
for f in filepath:
    filename.append(os.path.split(f)[1])
print(filename)

#順番が対応したpathとfilenameのリストが得られる
print(len(filepath),len(filename))
"""


def maketrainlabel(folderpath, labellist, label): #folderpathの例　"./unilabimage/traindata/*"
    
    #フォルダ内のfileのpathをそれぞれ受け取る; 名前順にソートしておく
    filepath = sorted(glob.glob(folderpath))
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
        os.system('python run.py  --model=mobilenet_thin  --image={0} --output_json=./outputjson/ --filename={1}'.format(filepath[i], filename[i]))

    return labellist


#訓練用の正解ラベル格納リスト
Y_train = []
#実際に探索するフォルダ
maketrainlabel('./unilabimage/traindata/pose0/*', Y_train, 0)
maketrainlabel('./unilabimage/traindata/pose1/*', Y_train, 1)
maketrainlabel('./unilabimage/traindata/pose2/*', Y_train, 2)
maketrainlabel('./unilabimage/traindata/pose3/*', Y_train, 3)
maketrainlabel('./unilabimage/traindata/pose4/*', Y_train, 4)

print(Y_train)
