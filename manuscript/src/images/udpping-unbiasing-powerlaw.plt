set term eps
set out "udpping-unbiasing-powerlaw.eps"
set autoscale
set ytics nomirror
set xtics nomirror
plot "./udpping-unbiasing-powerlaw.dat" using 1:2 w l t "Original distribution",\
"./udpping-unbiasing-powerlaw.dat" using 1:3 w l t "Unbiased distribution"
