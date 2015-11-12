import time
import matplotlib.pyplot as plt

def fib1(n):
	if n<2:
		return n
	return fib1(n-1) + fib1(n-2)

def fib2(n):
	i = 1
	j = 0
	for k in range(1,n+1):
		j = i + j
		i = j - i
	return j

def fib3(n):
	i = 1
	j = 0
	k = 0
	h = 1
	while n>0:
		if (n % 2 == 1):
			t = j*k
			j = i * h + j * k + t
			i = i * k + t
		t = h ** 2
		h = 2 * k * h + t
		k = k ** 2 + t
		n = n / 2
	return j

def getTime(function,argument):
	start = time.time()
	function(argument)
	end = time.time()
	return end - start

def Times(f, arr):
    allTimes = []
    for n in arr:
        allTimes.append(getTime(f, n))
    return allTimes

def plot(f, arr, title):
    plt.plot(arr, Times(f, arr))
    plt.title(title)
    plt.ylabel("times")
    plt.xlabel("Fn")
    plt.show()

plot(fib1, range(0, 30), title="Timeplot for 1st algorithm")
plot(fib2, range(0, 10000), title="Timeplot for 2nd algorithm")
plot(fib3, range(0, 20000,50), title="Timeplot for 3rd algorithm")
