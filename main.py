import csv
import pandas as pd
import plotly.express as px
import statistics as stats

with open("DataStory.csv",newline = "")as f:
  reader = csv.reader(f)
  saving_data = list(reader)

saving_data.pop(0)

total_entries = len(saving_data)
total_people_given_reminder = 0

for i in saving_data:
  if int(i[3])== 1:
    total_people_given_reminder += 1

import plotly.graph_objects as go 

all_saving = []
for e in saving_data:
  all_saving.append(float(e[0]))

print(f"mean of savings - {stats.mean(all_saving)}")
print(f"median of savings - {stats.median(all_saving)}")
print(f"mode of savings - {stats.mode(all_saving)}")

reminded_savings = []
not_reminded_savings = []

for data in saving_data:
  if int(data[3])== 1:
    reminded_savings.append(float(data[0]))
  else:
    not_reminded_savings.append(float(data[0]))

print("people who were reminded")
print(f"mean of savings- {stats.mean(reminded_savings)}")
print(f"median of savings- {stats.median(reminded_savings)}")
print(f"mode of savings- {stats.mode(reminded_savings)}")
print("\n\n")
print("people who were not reminded")
print(f"mean of savings- {stats.mean(not_reminded_savings)}")
print(f"median of savings- {stats.median(not_reminded_savings)}")
print(f"mode of savings- {stats.mode(not_reminded_savings)}")

print(f"standard deviation all the data- {stats.stdev(all_saving)}")
print(f"standard deviation people who were reminded- {stats.stdev(reminded_savings)}")
print(f"standard deviation people who were not reminded- {stats.stdev(not_reminded_savings)}")

import numpy as np

age = []
savings = []
for q in saving_data:
  if float(q[5])!= 0:
    age.append(float(q[5]))
    savings.append(float(q[0]))

correlation = np.corrcoef(age,savings)
print(f"correlation between age and savings is- {correlation[0,1]}")

import plotly.figure_factory as ff
fig = ff.create_distplot([df["quant_saved"].tolist()],["Savings"],show_hist = False)
fig.show()
