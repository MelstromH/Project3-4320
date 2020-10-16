import pygal as py
import lxml as lx

def printGraph():
    print("Hello from a function")
    line = py.Line()
    line.title = "Salary variation of Shweta in the past 5 years"  # Set the title of the line chart
    line.x_labels = (2014, 2015, 2016, 2017, 2018)  # Setting the labels for x-axis
    line.add('Salary in lakhs in INR', [None, 3, 5, 8, 10, 15])  # Setting the salary values to be plotted on graph
    line.render_to_file("salary_variation.svg")  # This saves the chart in the current library in the file salary_year_variation.svg
    line.render_in_browser()
