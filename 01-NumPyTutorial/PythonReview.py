print("Hello")

a = 10
a = 11.9
a = "Tom"
b = 19
c = 2.50345

print("Hello %s you are %d years old you own me %.2f dollars" % (a, b, c))

for i in range(0, 5):
	print(i)
	print("fun")

x = 4
while (x > 0):
	print(x)
	x = x - 1

l = []
l = [2,3,"t"]
l.append(44)

print(l)

for s in l:
	print(s)

x = float(input("Eneter your age:"))
print(x)

def run(n):
	for i in range(0,n):
		print(i)
	return 100

w = run(3)
print(w)

w = "AbcDef"
for c in w:
	print(c)

print(w[2])
