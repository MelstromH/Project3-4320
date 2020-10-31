import pygal as py
import lxml as lx
import datetime
import pandas as pd


def printLineGraph(symbol,dates, open_value, high_value, close_value, low_value):

    line = py.Line(x_label_rotation=20, width=2000)
    line.title = symbol  # Set the title of the line chart
    line.x_labels = dates  # Setting the labels for x-axis
    line.add('Open Values', open_value)  #setting data
    line.add('High Values', high_value)
    line.add('Close Values', close_value)
    line.add('Low Values', low_value)
    line.render_in_browser()


def printBarGraph(symbol, dates, open_value, high_value, close_value, low_value):

    line_chart = py.Bar(width=2000, x_label_rotation=20)
    line_chart.title = symbol
    line_chart.x_labels = dates
    line_chart.add('Open Values', open_value)  # setting data
    line_chart.add('High Values', high_value)
    line_chart.add('Close Values', close_value)
    line_chart.add('Low Values', low_value)
    line_chart.render_in_browser()
