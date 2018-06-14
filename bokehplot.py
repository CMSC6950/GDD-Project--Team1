import pandas as pd
from bokeh.layouts import gridplot, column
from bokeh.io import output_file, save, show
from bokeh.plotting import figure


halifaxIntl = pd.read_csv("Data/50620-2016-GDD.csv", header=None)
ottawaIntl = pd.read_csv("Data/50430-2016-GDD.csv", header=None)
calgaryIntl = pd.read_csv("Data/49568-2016-GDD.csv", header=None)

gddOttawa =ottawaIntl.iloc[:][1].tolist()
gddCalgary =calgaryIntl.iloc[:][1].tolist()
gddHalifax =halifaxIntl.iloc[:][1].tolist()

days = list(range(0,len(calgaryIntl)))

halifaxIntlPlot = figure(title="GDD for Halifax for the year 2015", tools='hover, pan, box_zoom')
halifaxIntlPlot.grid.grid_line_alpha=0.3
halifaxIntlPlot.xaxis.axis_label = "Days"
halifaxIntlPlot.yaxis.axis_label = "GDD"
halifaxIntlPlot.line(days, gddHalifax, color='#000080')

ottawaIntlPlot = figure(title="GDD for Ottawa for the year 2015", tools='hover, pan, box_zoom')
ottawaIntlPlot.grid.grid_line_alpha=0.3
ottawaIntlPlot.xaxis.axis_label =  "Days"
ottawaIntlPlot.yaxis.axis_label = "GDD"
ottawaIntlPlot.line(days, gddOttawa, color='#33A02C')

calgaryIntlPlot = figure(title="GDD for Calgary for the year 2015", tools='hover, pan, box_zoom')
calgaryIntlPlot.grid.grid_line_alpha=0.3
calgaryIntlPlot.xaxis.axis_label = "Days"
calgaryIntlPlot.yaxis.axis_label = "GDD"
calgaryIntlPlot.line(days, gddCalgary, color='#FF5733')

output_file('docs/bokehplot.html')

save(column(halifaxIntlPlot, ottawaIntlPlot, calgaryIntlPlot), plot_width=800, plot_height=350)
