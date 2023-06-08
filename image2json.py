#フォルダ内の画像をrun.pyしてjsonに書き起こす
#このファイルはなぜかターミナルから実行しないとエラーするので注意

import os
import glob

#fineのそれぞれのpathを受け取る
filepath = glob.glob("./unilabimage/*")

#file名を受け取る
path = "./unilabimage"     #['./unilabimage/sample1.jpg', './unilabimage/sample3.jpg', './unilabimage/sample2.jpg']
files = os.listdir(path)   #['.DS_Store', 'sample1.jpg', 'sample3.jpg', 'sample2.jpg']


print(len(filepath),len(files))
print(filepath,files)


#os.system('python run.py  --model=mobilenet_thin  --image={0} --output_json=./outputjson/ --filename={1}'.format(filepath[0], files[1]))

for i in range(len(filepath)) : 
    os.system('python run.py  --model=mobilenet_thin  --image={0} --output_json=./outputjson/ --filename={1}'.format(filepath[i], files[i+1]))
