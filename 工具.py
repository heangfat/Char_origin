import pandas as pd;import numpy as np;from collections import Counter;import re
import matplotlib.pyplot as plt;import matplotlib.font_manager
冓 = {"⿰":2,"⿲":3,"⿱":2,"⿳":3,"⿴":2,"⿵":2,"⿶":2,"⿷":2,"⿸":2,"⿹":2,"⿺":2,"⿻":2,"⿼":2,"⿽":2,"⿾":1,"⿿":1,"▤":4,"𝍤":5,"Ｔ":3,"Ｙ":3,"⸫":1,"⸬":1,"▥":4,"∪":2,"∃":2,"∞":2}# 所有構形及其後所領下級數
挪用歸并件 = ["戶戸","辛⾟","宀𰃦","鳥𩾑","十⼗"]# 肩、倒〬三角頭飾、牢、鷄之初文、古上
挪用反倒轉件 = ["阜阝","舟⾈","水⽔","弓⼸𢎜","矢⽮","臣⾂","𠂤𠕉","皿亚"]# 雋之弓與矰之初文、受之舟、臦之反臣、益之水、射之矢、殿所从
歸并件 = ["一●乛","囗〇","冈网","尞㶫","厂丆","上丄","下丅","凵𠙴","朩汖","兕𤉡","中𠁩","且𠀃","叀𤰔","卣㔽","乂㐅","乙𠃉","几𠘧","冉冄","田龱","眉𦭝","垂𠂹","壼𡆵","井丼","卩㔾","角甪","𫢉佘","于亐","皃㫐","車𠦴𨏖"]+ 挪用歸并件
反倒轉件 = ["止𣥂夂㐄","爪仉𠂇又","永𠂢","人匕𠤎𠂈","身㐆","大屰","卩㔿","孑孓","了巳","欠旡","口亼","目罒","矢𢆉","刀𱍸","冉𠀎","司后","彳亍","戶𠃛","毛氺","上下","亅𠄌","一丨","凹𠕄"]+ 挪用反倒轉件
訛宂次 = {"異體":1, "偏旁":2, "倭":3, "国字":3, "簡体":3, "共產":3, "附":4, "訛":5}
def 構字遞歸(構字式:str, 到=0, 級=0, 報=True):
	""" 僅遞歸，不生成圖像。結構符歬置 """
	構成 = ''
	if 到 >= len(構字式):
		if 報:print('終了（歬）')
		return 構成, 到
	if 構字式[到] in 冓.keys():
		件數 = 冓[構字式[到]]
		if 報:print(('　'*級)+構字式[到], 件數,'件')
		構成 = 構字式[到]
		for 件第 in range(件數):
			到 += 1
			件,到 = 構字遞歸(構字式, 到, 級+1, 報=報)
			if 報:print('　'*級,件, str(到+1),'['+str(件第+1)+']')
			構成 += 件
		if 報:print(('　'*級)+構成+'→☯')
		return '☯', 到
	else:
		return 構字式[到], 到
def 檢構字式(構字式:str, 報=False):
	構 = 構字遞歸(構字式, 報=報)
	if 構[1] == len(構字式)-1 or len(構字式)==0:
		if 報:
			print('正確');return True
		else:
			return 1
	elif 構[1] > len(構字式)-1:
		if 報:
			raise ValueError('構字式有誤！或有宂餘結構符（缺少部件），或順序有誤。')
		else:
			return 2
	else:
		if 報:
			raise ValueError('構字式有誤！或有宂餘部件（缺少結構符），或順序有誤。')
		else:
			return 3

def 綜敘(字):
	歸并組 = [x for x in 歸并件 if 字 in x]
	反倒轉組 = [x for x in 反倒轉件 if 字 in x]
	if len(歸并組):
		代排字 = 歸并組[0][0]
	elif len(反倒轉組):
		代排字 = 反倒轉件[0][0]
	else:
		代排字 = 字
	敘 = ord(代排字)
	if 敘 >= 0x3400 and 敘 < 0x4e00:#A
		敘 += 0x10000
	return 敘
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
	序 = []
	for 註 in 註列:
		if 註 in 訛宂次.keys():
			序.append(訛宂次[註])
		else:
			序.append(0)
	return 序
def 攏(字列):
	序 = []
	for 字 in 字列:
		歸并組 = [x for x in 歸并件 if 字 in x]
		反倒轉組 = [x for x in 反倒轉件 if 字 in x]
		if len(歸并組):
			代排字 = 歸并組[0][0]
		elif len(反倒轉組):
			代排字 = 反倒轉件[0][0]
		else:
			代排字 = 字
		序.append(代排字)
	return 序
def 補全褈件(構字式:str):
	""" 將品、㗊結構複製補全至應有之數量 """
	if 構字式.count('⸫')==0 and 構字式.count('⸬')==0:
		return 構字式
	欲複製之冓 = {"⸫":3,"⸬":4}
	for 冓名 in 欲複製之冓.keys():
		到 = 0
		始位 = 構字式.find(冓名)
		while 始位 >= 0:
			後接 = 構字式[始位+1:始位+2]
			if 後接 in 冓.keys():
				_, 長 = 構字遞歸(構字式[始位+1:], 報=False)
				到 = 始位+長+2
				重複段 = 構字式[始位+1:到]
				構字式 = 構字式[:始位+1] + 重複段*欲複製之冓[冓名] + 構字式[到:]
			else:
				到 = 始位+2
				構字式 = 構字式[:始位+1] + 後接*欲複製之冓[冓名] + 構字式[始位+2:]
			始位 = 構字式.find(冓名, 到)
	return 構字式
def 後置主冓(構字式:str):
	"""	去〫除分支冓，僅留主冓，并置于尾，變成實際擊鍵之次序 """
	if len(構字式) < 2:# 无解或文
		return 構字式
	主冓 = 構字式[0]
	部件 = re.sub('['+(''.join(冓.keys()))+']','',構字式)
	return 部件 + 主冓
class 處理碼表():
	def __init__(self, 碼表:pd.DataFrame):
		self.碼表 = 碼表.fillna('')
		self.未列字 = []
		self.有字无解 = []
		self.解之名 = ['正解','或解','別解','又解']
	def 統計(self, 圖=False):
		所有構件 = self.碼表['迩原正解'].str.cat(sep='') + self.碼表['迩原或解'].astype(str).str.cat(sep='') + self.碼表['迩原別解'].astype(str).str.cat(sep='') + self.碼表['迩原又解'].astype(str).str.cat(sep='')
		所有部件 = re.sub('['+(''.join(冓.keys()))+']','',所有構件)
		計 = Counter(所有部件)
		if 圖:
			plt.rcParams["font.family"] = "Noto Sans CJK JP", "KaiXinSongB"
			plt.figure(dpi=100).set_figwidth(300)
			plt.bar(*zip(*計.most_common()), width=4)
			plt.show()
			plt.figure().get_dpi()
		return 計
	def 解幹(self, 構字式:str, 文=True):
		解式 = ''
		for 字幹 in 構字式:
			if 字幹 in 冓.keys():#ord(字幹) < 0x3000 or (ord(字幹) >= 0xff00 and ord(字幹) < 0xfff0) or 字幹 == '𝍤':
				解式 += 字幹
				continue
			解字幹 = self.碼表.loc[self.碼表["漢字"]==字幹, "迩原正解"]
			if len(解字幹) < 1:
				self.未列字.append(字幹)
				解式 += 字幹;continue
			解字幹 = 解字幹.item()
			if 解字幹 == '':
				self.有字无解.append(字幹)
				解式 += 字幹
			else:
				if 文 and 解字幹 != 字幹:
					解字幹 = self.解幹(解字幹)
				解式 += 解字幹
		return 解式
	def 迭代解幹(self):
		迭代一 = self.碼表既序["迩原正解"].copy()
		self.碼表既序["迩原正解窮"] = self.碼表既序["迩原正解"].apply(lambda x: self.解幹(x, False))
		異條 = self.碼表既序["迩原正解窮"] != 迭代一
		計數 = 0
		while (異條).any():
			迭代一 = self.碼表既序["迩原正解窮"].copy()
			self.碼表既序.loc[異條, "迩原正解窮"] = self.碼表既序.loc[異條, "迩原正解窮"].apply(lambda x: self.解幹(x, False))
			異條 = self.碼表既序["迩原正解窮"] != 迭代一
			計數 += 1
			print(f'迭代了 {計數} 次，餘 {len(異條.loc[異條==True])} 條未窮解')
		self.未列字 = list(set(self.未列字));self.有字无解 = list(set(self.有字无解))
		未列字數 = len(self.未列字);无解字數 = len(self.有字无解)
		if 未列字數 > 0:
			print(f'此 {未列字數} 字未列：{"、".join(self.未列字)}。')
		if 无解字數 > 0:
			print(f'此 {无解字數} 字无正解：{"、".join(self.有字无解)}。')
		if 未列字數 > 0 or 无解字數 > 0:
			print(f'請補齊上述 {未列字數+无解字數} 字後再運行。')
		else:
			print('蕆。')
		差異 = self.碼表既序["迩原正解"].compare(self.碼表既序["迩原正解窮"], result_names=('字幹式','文式'))
		self.碼表 = self.碼表既序.rename(columns={"迩原正解":"正解榦式","迩原正解窮":"迩原正解"})
		print('改了',str(len(差異)),'條：')
		return 差異
	def 改為擊鍵序(self):
		for 解名 in self.解之名:
			self.碼表[解名+"鍵"] = self.碼表["迩原"+解名].apply(lambda x: 後置主冓(補全褈件(x)))
	def 校覈(self):
		覈 = self.碼表["迩原正解"].apply(lambda z: 檢構字式(z,報=False))
		符多部少 = self.碼表["漢字"].loc[覈==2];符少部多 = self.碼表["漢字"].loc[覈==3]
		if len(符多部少) > 0:
			print(f'下列 {len(符多部少)} 字或有宂餘結構符（缺少部件），或順序有誤：{符多部少.str.cat(sep='、')}')
		if len(符少部多) > 0:
			print(f'下列 {len(符少部多)} 字或有宂餘部件（缺少結構符），或順序有誤：{符少部多.str.cat(sep='、')}')
		return [符多部少,符少部多]
	def 排序(self):
		碼表排序 = self.碼表.sort_values(by='漢字', axis=0)
		碼表排序["敘數"] = 碼表排序["漢字"].apply(lambda z: 綜敘(z))
		碼表排序.loc[碼表排序["漢字"]==碼表排序["迩原正解"], "敘數"] -= 0x100000
		# 碼表排序 = 碼表排序.sort_values(by=['漢字'], axis=0, key=攏)
		# 碼表排序 = 碼表排序.sort_values(by=['迩原正解'], axis=0, key=依構件排序)
		碼表排序 = 碼表排序.sort_values(by='敘數', axis=0)
		# 碼表排序 = 碼表排序.sort_values(by=['備註'], axis=0, key=依備註排序)
		碼表排序.drop(columns=['敘數'], inplace=True)
		self.碼表既序 = 碼表排序
		return 碼表排序
# def 并異體(表):
# 	異體類型 = ['共產','偏旁','倭','異體','附','訛']
# 	表.loc[表["六書"]!='共產', "異體類型"] = ''
# 	表.loc[(表["六書"]=='共產') & ((表["備註"]=='偏旁')|(表["備註"]=='倭')), "六書"] = '共產、'
# 	表.loc[(表["六書"]=='共產') & (表["備註"]=='異體'), "備註"] = ''
# 	表["異體"] = 表["備註"].apply(lambda z: z if z in 異體類型 else '')
# 	表["異體"] = 表["六書"] + 表["異體"]