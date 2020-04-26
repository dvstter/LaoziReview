# -*- coding:utf-8 -*-

"""
使用方法：
1.修改chaps.txt
2.修改pere_round，每轮章节数，total置位None为全复习，否则设置为总的随机复习章节数
"""

import random
import re

class RandomRevive:
	def __init__(self):
		self.chaps = {}
		
	def read_chaps(self):
		f = open("chaps.txt", "rt")
		for l in f.readlines():
			# jump over the empty linee
			if len(l) == 0:
				continue
				
			tmp = l.strip().split(" ")
			cnum = int(re.findall("\d+", tmp[0])[0])
			self.chaps[cnum] = tmp[1]
			
	def output(self, per_round, total=None):
		f = open("output.txt",  "w")
		keys = [x for x in self.chaps.keys()]
		if total:
			keys = random.choices(keys, k=total)
		random.shuffle(keys)
		rounds = []
		rnum = int(len(keys) / per_round)
		left = int(len(keys) % per_round)
		for i in range(rnum):
			rounds += [keys[i*per_round:(i+1)*per_round]]
			
		if left != 0:
			rounds += [keys[-left:]]
		
		for rnd in rounds:
			for idx in rnd:
				f.write(f"{idx}章 {self.chaps[idx]}\n")
				
			f.write("\n")
			
	def run(self, per_round, total=None):
		self.read_chaps()
		self.output(per_round, total)
		
if __name__ == "__main__":
	rr = RandomRevive()
	rr.run(5, total=20)