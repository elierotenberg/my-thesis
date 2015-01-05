from math import exp, factorial, log
def pdf(mu, k):
    return exp(-mu) * (mu**k) / factorial(k)

Kmin = 1
Kmax = 30
incr = 1
mu = 10
k = Kmin
while(k <= Kmax):
    p = pdf(mu, k)
    print ("%d %lf %lf" % (k, p, p/k))
    k = k + incr
