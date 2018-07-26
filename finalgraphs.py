import matplotlib.pyplot as plt
import numpy as np
# label = ['2-3', '4-8', '9-13', '14-18', '19-30', '31-50', '51+']
# no_activew = [
#     1000,
#     1200,
#     1600,
#     1800,
#     2000,
#     1800,
#     1600,
# ]



noactive2 = 1000
noactive4 = 1200
noactive9 = 1600
noactive14 = 1800
noactive19 = 2000
noactive31 = 1800
noactive51 = 1600


modactive2 = 1200
modactive4 = 1500
modactive9 = 1800
modactive14 = 2000
modactive19 = 2100
modactive31 = 2000
modactive51 = 1800


active2 = 1200
active4 = 1600
active9 = 2000
active14 = 2400
active19 = 2400
active31 = 2200
active51 = 2100



n_groups = 7
err = (0,0,0,0,0,0,0)

noactive = (noactive2, noactive4, noactive9, noactive14, noactive19, noactive31, noactive51)
modactive = (modactive2, modactive4, modactive9, modactive14, modactive19, modactive31, modactive51)
active = (active2, active4, active9, active14, active19, active31, active51)


#plt.rcdefaults()
fig, ax = plt.subplots()


index = np.arange(n_groups)
bar_width = 0.15
space = 0.05

opacity = 0.7
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, noactive, bar_width,
                alpha=opacity, color='pink',
                yerr=err, error_kw=error_config,
                label='Sedentary')

rects2 = ax.bar(index + bar_width + space, modactive, bar_width,
                alpha=opacity, color='lightblue',
                yerr=err, error_kw=error_config,
                label='Moderately Active')

rects3 = ax.bar(index + bar_width + bar_width + space + space, active, bar_width,
                alpha=opacity, color='purple',
                yerr=err, error_kw=error_config,
                label='Active')



ax.set_xticks(range(7))
ax.set_xticklabels(['2-3','4-8','9-13','14-18','19-30','30-50','51+'])
#ax.invert_yaxis()
ax.set_xlabel('Ages')
ax.set_ylabel('Number of Calories Burned')
ax.set_title('Daily Calories Burned for Women')
ax.legend()

fig.tight_layout()
plt.show()

import matplotlib.pyplot as plt
# import matplotlib.ticker import MaxNLocator
# from collection import namedtuple
import numpy as np


noactive2m = 1000
noactive4m = 1400
noactive9m = 1800
noactive14m = 2200
noactive19m = 2400
noactive31m = 2200
noactive51m = 2000


modactive2m = 1200
modactive4m = 1500
modactive9m = 2000
modactive14m = 2600
modactive19m = 2700
modactive31m = 2500
modactive51m = 2300


active2m = 1200
active4m = 1800
active9m = 2300
active14m = 3000
active19m = 3000
active31m = 2900
active51m = 2600




n_groups = 7
err = (0,0,0,0,0,0,0)

noactivem = (noactive2m, noactive4m, noactive9m, noactive14m, noactive19m, noactive31m, noactive51m)
modactivem = (modactive2m, modactive4m, modactive9m, modactive14m, modactive19m, modactive31m, modactive51m)
activem = (active2m, active4m, active9m, active14m, active19m, active31m, active51m)


#plt.rcdefaults()
fig, ax = plt.subplots()


index = np.arange(n_groups)
bar_width = 0.15
space = 0.05

opacity = 0.7
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, noactivem, bar_width,
                alpha=opacity, color='pink',
                yerr=err, error_kw=error_config,
                label='Sedentary')

rects2 = ax.bar(index + bar_width + space, modactivem, bar_width,
                alpha=opacity, color='lightblue',
                yerr=err, error_kw=error_config,
                label='Moderately Active')

rects3 = ax.bar(index + bar_width + bar_width + space + space, activem, bar_width,
                alpha=opacity, color='purple',
                yerr=err, error_kw=error_config,
                label='Active')



ax.set_xticks(range(7))
ax.set_xticklabels(['2-3','4-8','9-13','14-18','19-30','30-50','51+'])
#ax.invert_yaxis()
ax.set_xlabel('Ages')
ax.set_ylabel('Number of Calories Burned')
ax.set_title('Daily Calories Burned for Men')
ax.legend()

fig.tight_layout()
plt.show()


from pylab import *

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Carbohydrates', 'Fruits and Vegetables', 'Dairy', 'Protein', 'Fats and Sugars'
fracs = [33, 33, 15, 12, 7]
explode=(0, 0, 0, 0, 0)

pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=False, startangle=90)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

title('A Healthy Plate')

show()

import matplotlib.pyplot as plt
# import matplotlib.ticker import MaxNLocator
# from collection import namedtuple
import numpy as np


wdep = 83
wanx = 88
wmood = 30
wbip = 1
weat = 1
wadhd = 2
wdem = 1


mdep = 69
manx = 79
mmood = 24
mbip = 1
meat = 0.3
madha = 0.6
mdem = 2



n_groups = 7
err = (0,0,0,0,0,0,0)

women = (wdep, wanx, wmood, wbip, weat, wadhd, wdem)
men = (mdep, manx, mmood, mbip, meat, madha, mdem)


#plt.rcdefaults()
fig, ax = plt.subplots()


index = np.arange(n_groups)
bar_width = 0.2
space = 0.05

opacity = 0.7
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, women, bar_width,
                alpha=opacity, color='magenta',
                yerr=err, error_kw=error_config,
                label='Women')

rects2 = ax.bar(index + bar_width + space, men, bar_width,
                alpha=opacity, color='blue',
                yerr=err, error_kw=error_config,
                label='Men')


ax.set_xticks(range(7))
ax.set_xticklabels(['Depression','Anxiety','Mood','Bipolar','Eating','ADHD','Dementia'])
#ax.invert_yaxis()
ax.set_xlabel('Disorders')
ax.set_ylabel('Percent Within Population')
ax.set_title('Mental Health Disorders')
ax.legend()

fig.tight_layout()
plt.show()

import matplotlib.pyplot as plt
# import matplotlib.ticker import MaxNLocator
# from collection import namedtuple
import numpy as np


no = 67
year = 68.5
month = 71
week = 74.5
day = 77.45



n_groups = 5
err = (0,0,0,0,0)

med = no, year, month, week, day


#plt.rcdefaults()
fig, ax = plt.subplots()


index = np.arange(n_groups)
bar_width = 0.6
space = 0.05

opacity = 0.7
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, med, bar_width,
                alpha=opacity, color='aqua',
                yerr=err, error_kw=error_config,
                )



ax.set_xticks(range(5))
ax.set_xticklabels(['Never','Yearly','Monthly','Weekly','Everyday'])
#ax.invert_yaxis()
ax.set_xlabel('Meditation')
ax.set_ylabel('Score on Mindfullness Test (out of 100)')
ax.set_title("Meditation's Effect on Mindfullness")
ax.legend()

fig.tight_layout()
plt.show()
