import numpy 
import matplotlib as mpl 
import matplotlib.pyplot as plt 

x = 1
a1 = numpy.sin(float(x)/5) * numpy.exp(float(x)/10) + 5 * (numpy.exp(float(-x)/2))

x = 15
a15 = numpy.sin(float(x)/5) * numpy.exp(float(x)/10) + 5 * (numpy.exp(float(-x)/2))

M1 = numpy.array([[1., 1.], [1., 15.]])
v1 = numpy.array([a1, a15])

w1 = numpy.linalg.solve(M1,v1)

x = numpy.linspace(0,16,200)
y = numpy.sin(x/5) * numpy.exp(x/10) + 5 * (numpy.exp((-x)/2))

plt.plot(x, y)
plt.show()

z = w1[0] + w1[1] * x

plt.plot(x, z)
plt.show()

x = 8
a8 = numpy.sin(float(x)/5) * numpy.exp(float(x)/10) + 5 * (numpy.exp(float(-x)/2))

M2 = numpy.array([[1., 1., 1.], [1., 8., 64.], [1., 15., 225.]])
v2 = numpy.array([a1, a8, a15])
w2 = numpy.linalg.solve(M2,v2)

x = numpy.linspace(0,16,200)
q = w2[2]*x**2 + w2[1]*x + w2[0] 

plt.plot(x, q)
plt.show()

x = 4
a4 = numpy.sin(float(x)/5) * numpy.exp(float(x)/10) + 5 * (numpy.exp(float(-x)/2))

x = 10
a10 = numpy.sin(float(x)/5) * numpy.exp(float(x)/10) + 5 * (numpy.exp(float(-x)/2))

M3 = numpy.array([[1., 1., 1., 1.], [1., 4., 16., 64.], [1., 10., 100., 1000.], [1., 15., 225., 3375.]])
v3 = numpy.array([a1, a4, a10, a15])
w3 = numpy.linalg.solve(M3,v3)

x = numpy.linspace(0,16,200)
p = w3[3]*x**3 + w3[2]*x**2 + w3[1]*x + w3[0]

plt.plot(x, p)
plt.show()