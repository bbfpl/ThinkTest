# coding=utf-8
from core.core import Core

class Run(Core):
	def __init__(self):
		print('run init')
		# core._start
		self._start()

if __name__ == '__main__':
	Run()