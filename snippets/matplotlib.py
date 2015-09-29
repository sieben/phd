import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("my_results.csv")
df[df.pkt_type == "udp"].count().plot(kind="bar")