import pandas as pd
import requests

data_mdl_new = requests.get("https://www.floatrates.com/daily/mdl.json")

data_mdl_new = data_mdl_new.json()

dataframe_new = pd.DataFrame(data_mdl_new).transpose()
dataframe_old = pd.read_json(
    "C:\\Users\\mariu\\PycharmProjects\\tekwillLiveV3\\lesson_23_homework\\conversion_rates.json"
).transpose()

difference = dataframe_old['inverseRate'] - dataframe_new['inverseRate']

dataframe_new['to_date'] = dataframe_new['date']
dataframe_new['from_date'] = dataframe_old['date']
dataframe_new['diffrence'] = difference

import seaborn as sns
import matplotlib.pyplot as plt

f, ax = plt.subplots(1, 1, figsize=(5, 5))
g = sns.barplot(x=dataframe_new['code'], y=dataframe_new['diffrence'])
t = g.set(title="Value counts of Pandas Series")

plt.savefig()

print(difference)
