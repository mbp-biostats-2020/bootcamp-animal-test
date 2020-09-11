import pandas as pd
from plotnine import ggplot, aes, geom_point, geom_histogram

msleep = pd.read_csv("Data/mammal-sleep-data.tsv", sep="\t")
print(msleep)

