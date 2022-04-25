from algorithms.measure_asymptotic_behaviour import measure_run_time, compute_asymptotic_constant
#from kruskal_naive import kruskal, kruskal_behaviour
#from prim_priority_queue import prim_priority_queue, prim_priority_queue_asymptotic_behaviour
import matplotlib.pyplot as plt
from graph.graph import read_all

run_times_str_k = "46755.83 57210.84 63493.33 49974.17 189552.5 186115.42 220902.5 206041.67 747797.5 673641.25 695365.0 737927.92 2748417.5 2599855.0 2722158.75 2862364.58 4160167.5 4110886.25 4408771.67 4214740.0 16178252.92 16571013.33 16456630.83 16361167.08 66657129.59 65564972.92 64991172.5 64030162.5 252870833.0 258125667.0 266030167.0 254777292.0 413280917.0 410499292.0 432456125.0 423710375.0 1625060167.0 1610621417.0 1606070834.0 1599820834.0 6561827833.0 6527104083.0 6455970417.0 6672152542.0 26695596416.0 25917777250.0 25963166959.0 27174726250.0 41687377417.0 41717724625.0 41611745083.0 40241656125.0 164400795875.0 165920714208.0 168644185625.0 163318472834.0 707232004249.0 700820313041.0 711829640126.0 767041730791.0 3522055746917.0 3214378721625.0 3411448440792.0 3210302314167.0 5419729002333.0 5366687891334.0 5350167152499.0 5389362351833.0".split(' ')
run_times_k = [float(x) for x in run_times_str_k]

run_times_str_k_u = "18016.43 20187.09 20765.93 17846.92 41261.77 40090.08 44618.65 44060.07 93122.68 87343.32 86413.01 91372.25 186675.53 175981.37 183575.03 206233.7 248721.73 230780.14 244384.84 241619.94 489065.11 483510.11 474057.17 471086.25 1027720.88 995184.82 1000393.82 986044.16 2112191.91 2135118.58 2135249.5 2087316.55 2617245.15 2618183.98 2696284.45 2693641.17 5552586.01 5586148.75 5628955.9 5607737.13 11586955.04 11444168.94 11484293.98 11641789.41 23799660.74 23853491.68 23898300.98 24519391.06 30662245.5 30562455.2 30533325.25 30682520.56 65820168.08 66955712.65 66446379.75 67624556.71 151880191.31 152134285.73 151891611.72 152198090.19 338456513.54 335893085.8 335337319.35 335816476.17 432770869.7 433467054.75 433071902.11 418800149.41".split(' ')         
run_times_k_u = [float(x) for x in run_times_str_k_u]

run_times_str_p = "68371.666 74362.25 87112.541 74741.083 220440.708 195012.208 209947.334 200191.459 514323.292 505162.833 514929.458 527084.583 1229287.042 1152658.667 1166463.625 1284979.75 1614801.667 1562933.584 1657815.334 1609519.041 3725183.0 3714950.0 3761651.041 3712237.791 8454728.625 8520341.584 8504253.584 8476757.709 19390325.0 19473375.0 19380091.7 19412825.0 25256712.5 25150091.7 25456958.4 25490754.2 57222270.9 56566304.1 56900583.3 56829820.8 124307629.2 122747987.5 122566191.7 122605395.8 267844604.2 267624370.8 268544287.5 269682533.4 347909804.2 345876445.8 345712287.5 339238791.6 734343850.0 746810487.5 747033845.8 740922354.2 1606015762.5 1619549466.7 1622485208.3 1624862991.6 3505104041.6 3495363600.0 3539552033.4 3552087700.0 4671771529.2 4536536020.8 4621599641.6 4606644816.7".split(' ')
run_times_p = [float(x) for x in run_times_str_p]

run_times_str_p_s = "12709.6 12094.7 13426.4 11418.0 29576.0 33763.9 36154.0 42444.0 64187.0 75246.8 61235.5 59139.4 125881.0 139356.3 118867.7 134435.0 174101.1 170681.5 176905.2 155051.0 330288.6 329402.6 322284.5 318817.0 700282.4 668889.7 688842.9 666485.5 1456353.7 1448070.7 1629129.7 1504143.0 1842784.4 1929709.5 1874482.4 1880142.4 4069809.2 4183535.3 4253687.1 4120255.9 8635223.5 8711966.9 9048551.6 8372434.9 18336332.0 18021037.2 19949057.3 19100818.9 23239222.9 25166489.1 23501121.0 23820249.0 53845573.8 55998582.4 55239958.3 57104099.0 131250267.4 131968992.3 131675142.8 130776645.1 300595448.2 299341896.6 296663417.8 301969757.4 383387390.5 375701695.3 376290021.1 378562179.7".split(' ')
run_times_p_s = [float(x) for x in run_times_str_p_s]

path = 'dataset-1'

graphs = read_all(path)

graphs_dimensions = [(i.get_n(), i.get_m()) for i in graphs]

def plot_comparison(
  run_times_p,
  run_times_p_s,
  run_times_k_u,
  graphs_dimensions, 
):
  x = [n*m for n, m in graphs_dimensions]

  #plt.plot(x, run_times_k, label="Kruskal Naive Algorithm")
  plt.plot(x, run_times_p, label="Prim Algorithm")
  plt.plot(x, run_times_p_s, label = "Prim Smarter Algorithm")
  plt.plot(x, run_times_k_u, label="Kruskal Union Find Algorithm")
  
  plt.title("Comparison between algorithms runtimes")
  plt.xlabel("m*n")
  plt.ylabel("Time")
  plt.legend()
  plt.show()

def plot_complexity(
  C, 
  run_times,
  graphs_dimensions, 
  asymptotic_behaviour,
  title,
  expected_graphic_label,
  actual_graphic_label = 'Obtained complexity'
):
  x = [n*m for n, m in graphs_dimensions]
  reference_z = [C * asymptotic_behaviour(n, m) for n, m in graphs_dimensions]

  plt.plot(x, reference_z, label=expected_graphic_label)
  plt.plot(x, run_times, label=actual_graphic_label)
  
  plt.title(title)
  plt.xlabel("m*n")
  plt.ylabel("Time")
  plt.legend()
  plt.show()

plot_comparison(run_times_p, run_times_p_s, run_times_k_u, graphs_dimensions)

# plot_comparison(run_times_p_s, run_times_k_u, graphs_dimensions)

#plot_complexity(2782, run_times_p, graphs_dimensions, prim_priority_queue_asymptotic_behaviour, "Prim's algorithm priority queue version", "Expected complexity: O(m*log(n))")