def f1(x):
	fun = pow(x, 2) + 1
	return fun


def f2(x):
	fun = 1 / pow(x, 2)
	return fun


def f3(x):
	fun = pow(x, 2) - 1
	return fun


def f(x):
	if x <= 0:
		return f1(x)
	elif 0 < x < 1:
		return f2(x)
	else:
		return f3(x)
