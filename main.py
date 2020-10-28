from GraphFunc import *
from Queries import *

userChoices = queries()

if userChoices[1] == 1:
    printBarGraph(userChoices[0], userChoices[2])
else:
    printLineGraph(userChoices[0], userChoices[2])

