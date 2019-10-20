import time

class time_see:
	def __init__(self, func):
		self.num_runs = 10
		self.func = func


	def __call__ (self, *args, **kwargs):
		avg_time = 0
		for _ in range(self.num_runs):
			t0 = time.time()
			self.func(*args, **kwargs)
			t1 = time.time()
			avg_time += (t1 - t0)
		avg_time /= self.num_runs
		fc = self.func.__name__
		print("Среднее время выполнения функции %s за %s запусков,сек = %.5f" % (
			fc,
			self.num_runs,
			avg_time))
		return self.func(*args, **kwargs)


@time_see
def res(): #функция для проверки работы декоратора
	for i in range(1000):
		a = i**2
res()
	