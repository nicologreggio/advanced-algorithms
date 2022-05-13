import matplotlib.pyplot as plt

random_run_times_str =  "933217.92 80965.42 7374922.5 79593973.75 371442502.08 892292.5 13633413.75 17449066.67 3367187.92 3422815.0 65058308.75 101111.25 184125.42".split(' ')
random_run_times = [float(x) for x in random_run_times_str]

random_error_str = "0.1036 0.0599 0.0879 0.1169 0.1255 0.0563 0.1284 0.0849 0.0502 0.061 0.1415 0.0 0.0396".split(' ')
random_error = [float(x) for x in random_error_str]

closest_run_times_str= "6973916.0 245664.0 157577402.0 4969189590.0 57705632278.0 6147059.0 305868566.0 444129410.0 40726611.0 39814562.0 3480400421.0 330714.0 694886.0".split(' ')
closest_run_times = [float(x) for x in closest_run_times_str]

closest_error_str = "0.1921 0.0797 0.2206 0.1845 0.2178 0.1596 0.1746 0.1651 0.2155 0.1843 0.2037 0.1244 0.1145".split(' ')
closest_error = [float(x) for x in closest_error_str]

two_app_run_times_str = "1760910.75 247376.11 10413336.66 87986897.16 332234818.19 1585990.79 17066759.96 21014195.51 5111543.92 5222765.33 68504505.92 250642.03 431134.09".split(' ')
two_app_run_times = [float(x) for x in two_app_run_times_str]

two_app_error_str = "0.3410 0.1478 0.2782 0.2843 0.3444 0.3380 0.2946 0.3384 0.2840 0.2732 0.3232 0.1522 0.1979".split(' ')
two_app_error = [float(x) for x in two_app_error_str]

x = [i for i in range(1,14)]

'''
# RUNTIMES
plt.scatter(x, random_run_times, label="Random Insertion", marker=".")
plt.scatter(x, closest_run_times, label="Closest Insertion", marker="|")
plt.scatter(x, two_app_run_times, label="2-approximation", marker="_")

plt.title("Comparison between algorithms runtimes")
plt.xlabel("Graph")
plt.ylabel("Time")
plt.legend()
plt.show()
'''

# ERRORS
plt.scatter(x, random_error, label="Random Insertion", marker="o")
plt.scatter(x, closest_error, label="Closest Insertion", marker="v")
plt.scatter(x, two_app_error, label="2-approximation", marker="s")

plt.title("Comparison between algorithms relative errors")
plt.xlabel("Graph")
plt.ylabel("Relative Error")
plt.legend()
plt.show()


