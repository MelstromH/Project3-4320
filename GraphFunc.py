import pygal as py
import lxml as lx
import datetime
import pandas as pd

def printLineGraph(symbol, begDate, endDate, noDays, timeScale):

    x = 24
    if (timeScale == 1):
        x = noDays * 24
    if (timeScale == 2):
        x = noDays * 1
    if (timeScale == 3):
        x = noDays / 7
    if (timeScale == 4):
        x = noDays / 30

    mydates = pd.date_range(begDate, endDate, periods=x).tolist()
    line = py.Line(x_label_rotation=20, width = 2000)
    line.title = symbol  # Set the title of the line chart
    line.x_labels = mydates  # Setting the labels for x-axis
    line.add('Salary in lakhs in INR', [None, 3, 5, 8, 10, 15])  # Setting the salary values to be plotted on graph
    line.render_in_browser()

def printBarGraph(symbol, begDate, endDate, noDays, timeScale):

    x = 24
    if (timeScale == 1):
        x = noDays * 24
    if (timeScale == 2):
        x = noDays * 1
    if (timeScale == 3):
        x = noDays / 7
    if (timeScale == 4):
        x = noDays / 30

    mydates = pd.date_range(begDate, endDate, periods = x).tolist()
    line_chart = py.Bar(width=2000, x_label_rotation=20)
    line_chart.title = symbol
    line_chart.x_labels = mydates
    line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    line_chart.render_in_browser()