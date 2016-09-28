words = ['cat', 'sugar', 'beets']
for w in words:
	print(w, len(w))

for i in range(5):
	print(i)

print(range(12))

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end = ' ')
		a, b = b, a+b
	print()

fib(4000)
