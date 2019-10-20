import time

def time_this(num_runs):
	def decorator(func):
		def wrap(*args, **kwargs):
			avg_time = 0
			for _ in range(num_runs):
				t0 = time.time()
				func(*args, **kwargs)
				t1 = time.time()
				avg_time += (t1 - t0)
			avg_time /= num_runs
			fc = func.__name__
			print("Среднее время выполнения функции %s за %s запусков,сек = %.5f" % (
			fc,
			num_runs,
			avg_time))
		return wrap
	return decorator
	
@time_this(10)
def res(x): #функция для проверки работы декоратора
	for i in range(x):
		a = i**2

res(10000)