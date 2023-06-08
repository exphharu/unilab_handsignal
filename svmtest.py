from sklearn import datasets, svm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# あやめの分類でSVMの動作確認

# アヤメのデータをロードし、変数irisに格納
iris = datasets.load_iris()

# 特徴量のセットを変数Xに、ターゲットを変数yに格納
X = iris.data
y = iris.target

# 特徴量を外花被片の長さ(sepal length)と幅(sepal width)の
# 2つのみに制限(2次元で考えるため)
X = X[:,:2]

#模擬データ

X0 = np.ones((20, 2)) * np.array([2,1])  +  np.random.randn(20, 2)
X1 = np.ones((20, 2)) * np.array([0.5,3])  +  np.random.randn(20, 2)
X2 = np.ones((20, 2)) * np.array([-2,-1])  +  np.random.randn(20, 2)

Y0 = np.ones(20)*0
Y1 = np.ones(20)*1 
Y2 = np.ones(20)*2  

X = np.r_[X0,X1,X2]
Y = np.r_[Y0,Y1,Y2]

# 分類用にサポートベクトルマシンを用意
clf = svm.SVC(C=1.0, kernel='linear', decision_function_shape='ovr')
# 'auto'を指定すると1/(次元)がセットされる。この場合、1/2=0.5
#clf = svm.SVC(C=1.0, kernel='rbf', gamma='auto', decision_function_shape='ovr')
# gammaを大きくすると、曲率が大きい（よく曲がる）境界となる
#clf = svm.SVC(C=1.0, kernel='rbf', gamma=1.0, decision_function_shape='ovr')
# データに最適化
clf.fit(X, Y)

##### 分類結果を背景の色分けにより表示

# 最小値と最大値からそれぞれ1ずつ広げた領域を
# グラフ表示エリアとする
x_min = min(X[:,0]) - 1
x_max = max(X[:,0]) + 1
y_min = min(X[:,1]) - 1
y_max = max(X[:,1]) + 1

# グラフ表示エリアを縦横500ずつのグリッドに区切る
# (分類クラスに応じて背景に色を塗るため)
XX, YY = np.mgrid[x_min:x_max:500j, y_min:y_max:500j]

# グリッドの点をscikit-learn用の入力に並べなおす
Xg = np.c_[XX.ravel(), YY.ravel()]

# 各グリッドの点が属するクラス(0～2)の予測をZに格納
Z = clf.predict(Xg)

# グリッド上に並べなおす
Z = Z.reshape(XX.shape)

# クラス0 (iris setosa) が薄オレンジ (1, 0.93, 0.5, 1)
# クラス1 (iris versicolor) が薄青 (0.5, 1, 1, 1)
# クラス2 (iris virginica) が薄緑 (0.5, 0.75, 0.5, 1)
cmap0 = ListedColormap([(0, 0, 0, 0), (1, 0.93, 0.5, 1)])
cmap1 = ListedColormap([(0, 0, 0, 0), (0.5, 1, 1, 1)])
cmap2 = ListedColormap([(0, 0, 0, 0), (0.5, 0.75, 0.5, 1)])

# 背景の色を表示
plt.pcolormesh(XX, YY, Z==0, cmap=cmap0, shading='auto')
plt.pcolormesh(XX, YY, Z==1, cmap=cmap1, shading='auto')
plt.pcolormesh(XX, YY, Z==2, cmap=cmap2, shading='auto')

# 軸ラベルを設定
plt.xlabel('sepal length')
plt.ylabel('sepal width')

##### ターゲットに応じた色付きでデータ点を表示

# (y=0) のデータのみを取り出す
Xc0 = X[Y==0]
# (y=1) のデータのみを取り出す
Xc1 = X[Y==1]
#z(y=2) のデータのみを取り出す
Xc2 = X[Y==2]

# データXc0をプロット
plt.scatter(Xc0[:,0], Xc0[:,1], c='#E69F00', linewidths=0.5, edgecolors='black')
# データXc1をプロット
plt.scatter(Xc1[:,0], Xc1[:,1], c='#56B4E9', linewidths=0.5, edgecolors='black')
# データXc2をプロット
plt.scatter(Xc2[:,0], Xc2[:,1], c='#008000', linewidths=0.5, edgecolors='black')

# サポートベクトルを取得
SV = clf.support_vectors_
# サポートベクトルの点に対し、赤い枠線を表示
svgraph = plt.scatter(SV[:,0], SV[:,1], linewidths=1.0, edgecolors='red')
svgraph.set_facecolor((0,0,0,0))

#グラフを表示
plt.show()

result = clf.predict(X)

# データ数をtotalに格納
total = len(X)
# ターゲット（正解）と予測が一致した数をsuccessに格納
success = sum(result==Y)
              

# 正解率をパーセント表示
print('正解率')
print(100.0*success/total)