import pandas as pd;import numpy as np;from collections import Counter
冓 = {"⿰":2,"⿲":3,"⿱":2,"⿳":3,"⿴":2,"⿵":2,"⿶":2,"⿷":2,"⿸":2,"⿹":2,"⿺":2,"⿻":2,"⿼":2,"⿽":2,"⿾":1,"⿿":1,"４":4,"５":5,"Ｔ":3,"Ｙ":3,"Ａ":1,"＋":1}
歸并件 = ['一乛','冈网']
def 構字遞歸(構字式:str, 到=0, 級=0):
	""" 僅遞歸，不生成圖像。結構符歬置 """
	構成 = ''
	if 到 >= len(構字式):
		print('終了（歬）')
		return 構成, 到
	if 構字式[到] in 冓.keys():
		件數 = 冓[構字式[到]];print(('　'*級)+構字式[到], 件數,'件')
		構成 = 構字式[到]
		for 件第 in range(件數):
			到 += 1
			件,到 = 構字遞歸(構字式, 到, 級+1);print('　'*級,件, str(到+1),'['+str(件第+1)+']')
			構成 += 件
		print(('　'*級)+構成+'→☯')
		return '☯', 到
	else:
		return 構字式[到], 到
def 檢構字式(構字式:str):
	構 = 構字遞歸(構字式)
	if 構[1] == len(構字式)-1:
		print('正確');return True
	elif 構[1] > len(構字式)-1:
		raise ValueError('構字式有誤！或有宂餘結構符（缺少部件），或順序有誤。')
	else:
		raise ValueError('構字式有誤！或有宂餘部件（缺少結構符），或順序有誤。')
def 依構件排序(構件列):
	序 = []
	for 構件 in 構件列:
		if len(構件)==1:
			序.append(1)
		elif len(構件)==0:
			序.append(np.inf)
		else:
			序.append(5)
	return 序
def 依備註排序(註列):
	訛宂次 = {"異體":1, "倭":3, "簡体":3, "訛":5}
	序 = []
	for 註 in 註列:
		if 註 in 訛宂次.keys():
			序.append(訛宂次[註])
		else:
			序.append(0)
	return 序