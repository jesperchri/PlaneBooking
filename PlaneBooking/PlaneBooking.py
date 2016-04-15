from ChooseAndBook import * #Flight + Aircraft
from BoardingCardCreate import *
import ChooseAndBook

""" Book """


#Create plane
info = Flight("JJ8989", aircraft("YY8890", "Boeing 747", num_rows=22, num_seets_pr_row=6))
print("This is airplane data:\n{0}\n{1}\n{2}".format(info.exportcleanvalue(), info.number(), info.exportcleanvalue()))


#Choose seats


#Print boardingcard

