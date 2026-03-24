import numpy as np

a=np.array([1,2,3])
print(a.max())
ab=np.array(('1','4','4'))
print(ab)

print(a.mean())

x=np.linspace(1,2.5,5)
print(x)

y=np.sin(x)
print(y)

a=np.array([1,2,3])
a[1:2]=5
print(a[1])
print(a)

print(a.ndim)
print(a.shape, a.size, a.dtype)

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
b = [[11, 12, 1], [21, 22, 1], [31, 32, 1]]
ab=np.array(a)
ac=np.array(b)
print(a, b , ab)
az=np.dot(ab,ac)

print(az)

A='123456'
print(A[1::2])

print(A[1:4])

print(az[1,0])