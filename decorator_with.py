import time

class time_see:
	def __init__(self, num_runs, func=None, param=None):
		self.num_runs = num_runs
		self.func = func
		self.param = param

	def __enter__(self):
		return self

	def __exit__ (self, *args):	 
		avg_time = 0
		for _ in range(self.num_runs):
			t0 = time.time()
			self.func(self.param)
			t1 = time.time()
			avg_time += (t1 - t0)
		avg_time /= self.num_runs
		fc = self.func.__name__
		print("Среднее время выполнения функции %s за %s запусков,сек = %.5f" % (
			fc,
			self.num_runs,
			avg_time))

def res(x): #функция для проверки работы декоратора
	for i in range(x):
		a = i**2

with time_see(num_runs=10, func=res, param=10000) as ts:
	
	ts.func(ts.param)
