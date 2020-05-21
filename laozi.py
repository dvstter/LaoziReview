# -*- coding:utf-8 -*-

"""
参数说明：
	chaps_per_round 每轮章节数
	total           None为全复习，否则设置为随机复习章节数list
"""

import random
import re
import argparse

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
			temp = total.split("-")
			keys = [x for x in range(int(temp[0]), int(temp[1]))]
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
			
	def run(self, chaps_per_round, total=None):
		self.read_chaps()
		self.output(chaps_per_round, total)
		
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Generate Laozi review list.")
	parser.add_argument("-r", "--range", help="range like '1-32'", type=str)
	parser.add_argument("-t", "--times", help="chapters per round", type=int)
	args = parser.parse_args()
	rng = args.range
	chaps = args.times if args.times else 5
	
	rr = RandomRevive()
	rr.run(chaps, rng)