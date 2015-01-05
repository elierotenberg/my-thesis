set term eps
set out "udpping-unbiasing-poisson.eps"
set autoscale
set ytics nomirror
set xtics nomirror
plot "./udpping-unbiasing-poisson-original.dat" using 1:2 w l t "Original distribution",\
"./udpping-unbiasing-poisson-unbiased.dat" using 1:2 w l t "Unbiased distribution"
