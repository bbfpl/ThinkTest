# coding=utf-8
from core.core import Core

class Run(Core):
	def init(self):
		print('run init')
		


if __name__ == '__main__':
	r = Run()
	r.init()