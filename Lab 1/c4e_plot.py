from maplotlib import pyplot

# 1. prepare data
label = ["Android","ios","Web"]
value = [300,400,300]
colors = ['red','gold','green']
explode = [0, 0.2, 0]
# 2. Plot
pyplot.pie(value, labels=labels, colors=colors, explode=explode, shadow=Ture)
pyplot.axis('euqal')
# 3. Show

# Tat ca seach
