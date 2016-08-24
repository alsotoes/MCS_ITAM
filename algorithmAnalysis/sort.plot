echo "
  set datafile separator ','
  set ylabel 'Data set size'
  set xlabel 'Sort time (sec)'
  set title 'sort'
  set grid
  set style circle radius screen 0.0001
  plot 'test.data' using 1:2 with circles fillstyle solid noborder lc rgb 'forest-green'
" | gnuplot --persist
