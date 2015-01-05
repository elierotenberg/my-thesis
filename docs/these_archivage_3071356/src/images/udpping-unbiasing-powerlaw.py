from math import exp, factorial, log
def pdf(a, k):
    return a * (k**(a-1))

Kmin = 1
Kmax = 1000
incr = 1
a = 2.5
k = Kmin
sumOriginal = 0
sumUnbiased = 0
while(k <= Kmax + 1):
    p = pdf(a, k)
    sumOriginal = sumOriginal + p
    sumUnbiased = sumUnbiased + p/k
    k = k + incr
cumulOriginal = 0
cumulUnbiased = 0
k = Kmin
while(k <= Kmax):
    p = pdf(a, k)
    cumulOriginal = cumulOriginal + p
    cumulUnbiased = cumulUnbiased + p/k
    print ("%d %lf %lf" % (k, (sumOriginal - cumulOriginal)/sumOriginal, (sumUnbiased - cumulUnbiased)/sumUnbiased))
    k = k + incr
