import plotly.plotly as py
import plotly.tools as tls

import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime

multiple_bars = plt.figure()

x = [datetime.datetime(2011, 1, 4, 0, 0),
     datetime.datetime(2011, 1, 5, 0, 0),
     datetime.datetime(2011, 1, 6, 0, 0)]
x = date2num(x)

y = [4, 9, 2]
z=[1,2,3]
k=[11,12,13]

ax = plt.subplot(111)
ax.bar(x-0.2, y,width=0.2,color='b',align='center')
ax.bar(x, z,width=0.2,color='g',align='center')
ax.bar(x+0.2, k,width=0.2,color='r',align='center')
ax.xaxis_date()

plotly_fig = tls.mpl_to_plotly(multiple_bars)
py.iplot(plotly_fig, filename='mpl-multiple-bar')