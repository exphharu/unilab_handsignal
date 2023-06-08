#jsonから座標を抽出するための関数置き場

import math
import numpy as np

# 特定の 3 keypoints を指定して成す角を計算
# Keypoint K1 - K2 - K3 
def calc_angle(K1, K2, K3, keypointlist):
  # K1, K2, K3 の各座標  
  p1 = keypointlist[3*K1: 3*K1+2]
  p2 = keypointlist[3*K2: 3*K2+2]
  p3 = keypointlist[3*K3: 3*K3+2]

  # ベクトル V21, V23 の計算
  V21 = np.array(p1) - np.array(p2)
  V23 = np.array(p3) - np.array(p2)

  # ノルム・内積計算(発散防止のため小さい数字足してある)
  V21norm = np.linalg.norm(V21)
  V23norm = np.linalg.norm(V23)
  inner_prod = np.inner(V21, V23)
  
  # 内積計算
  if  V21norm * V23norm != 0:
    cos_theta = inner_prod / ( V21norm * V23norm )
  if  V21norm * V23norm == 0:
    cos_theta = -1

  #print(cos_theta)
  theta=math.degrees(math.acos(cos_theta))
  #print(theta)

  return cos_theta 


#4keypoint
#角度をそれぞれ計算する
def get_angle(keypointlist):

  # 体に対する右腕の角度
  # Keypoint : 3 - 1 - 8
  angle_rightarm = calc_angle(3, 1, 8, keypointlist)

  # 体に対する左腕の角度
  # Keypoint : 6 - 1 - 8
  angle_leftarm = calc_angle(6, 1, 8, keypointlist)

  # 右ひじの曲がり角度
  # Keypoint : 2 - 3 - 4
  angle_rightelbow = calc_angle(2, 3, 4, keypointlist)

  # 左ひじの曲がり角度
  # Keypoint : 5 - 6 - 7
  angle_leftelbow = calc_angle(5, 6, 7, keypointlist)

  return angle_rightarm, angle_leftarm, angle_rightelbow, angle_leftelbow  



"""
#2keypoint
#角度をそれぞれ計算する
def get_angle(keypointlist):

  # 体に対する右腕の角度
  # Keypoint : 3 - 1 - 8
  angle_rightarm = calc_angle(3, 1, 8, keypointlist)

  # 体に対する左腕の角度
  # Keypoint : 6 - 1 - 8
  angle_leftarm = calc_angle(6, 1, 8, keypointlist)

  # 右ひじの曲がり角度
  # Keypoint : 2 - 3 - 4
  #angle_rightelbow = calc_angle(2, 3, 4, keypointlist)

  # 左ひじの曲がり角度
  # Keypoint : 5 - 6 - 7
  #angle_leftelbow = calc_angle(5, 6, 7, keypointlist)

  return angle_rightarm, angle_leftarm
"""