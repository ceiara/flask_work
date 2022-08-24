import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

plt.style.use("ggplot")
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False

# plt.style.use("seaborn-ticks")
data = pd.read_excel('static/data/carprice/carprice.xlsx')

# 막대그래프
# ta = data.groupby('년식').mean()
# print(ta)
# print(type(ta))
# print(ta.columns)
# print(ta.index.to_numpy())

# plt.bar(ta.index.to_numpy()-0.1,ta['가격'].to_numpy(),width=0.1,alpha=0.5, label='가격')
# plt.bar(ta.index.to_numpy(),ta['배기량'].to_numpy(),width=0.1,alpha=0.5, label='배기량')
# plt.bar(ta.index.to_numpy()+0.1,ta['중량'].to_numpy(),width=0.1,alpha=0.5, label='중량')
# plt.xticks(rotation=30)
# plt.yticks(rotation=30)
# # plt.grid()
# plt.legend()
# # plt.show()
# plt.savefig('x3_y1.png')

# 년식별 차 종류 count
# ta2 = data.groupby("년식")['종류'].sum()
# print(ta2)
# str_count1 = ta2[2015].count('대형')
# str_count2 = ta2[2015].count('중형')
# str_count3 = ta2[2015].count('준준형')
# str_count4 = ta2[2015].count('소형')
# print("대형 = ",str_count1)
# print("중형 = ",str_count2)
# print("준준형 = ",str_count3)
# print("소형 = ",str_count4)

# category_names = ['대형','중형','준준형','소형']

# results = {
#     '2011': [0,0,0,4],
#     '2012': [0,0,1,3],
#     '2013': [0,0,0,3],
#     '2014': [4,0,0,2],
#     '2015': [22,28,0,4]
# }

#년도 count
# ta = data.groupby('년식').count()
# print(ta)

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["54 대 2015",
          "6 대 2014",
          "3 대 2013",
          "4 대 2012",
          "4 대 2011"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="년도",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=6, weight="bold")

ax.set_title("년식별 차량수")

# plt.show()
plt.savefig('year of car.png')