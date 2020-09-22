import pandas as pd
from scipy import stats
from plotnine import *

msleep = pd.read_csv("Data/mammal-sleep-data.tsv", sep="\t")
#print(msleep)
#print(msleep["vore"].value_counts())

# Test 1
# ------
# g = (
# 	# use ggplot function to make a plot
# 	ggplot(
# 		data=msleep,
# 		mapping=aes(x="bodywt")
# 	)
# 	# plot histogram of x axis values
# 	+ geom_histogram()
# )
# g.save("Plots/bodywt.histogram.png")

# Test 2
# ------
g = (
	ggplot(
		data=msleep,
		mapping=aes(x="vore", y="bodywt")
	)
	+ geom_jitter()
)
g.save("Plots/vore-bodywt.jitter.png")

# test_res = stats.mannwhitneyu(
# 	x=msleep.loc[(msleep["vore"] == "carni") & (msleep["bodywt"] < 2000), "bodywt"],
# 	y=msleep.loc[(msleep["vore"] == "herbi") & (msleep["bodywt"] < 2000), "bodywt"],
# )
# print(test_res)
