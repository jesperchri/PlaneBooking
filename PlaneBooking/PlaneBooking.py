from ChooseAndBook import * #Flight + Aircraft
from BoardingCardCreate import *
import ChooseAndBook
from pprint import pprint as pp
from Files import NewDoc

""" Book """

#Create plane
a = AirbusA319()
f = Flight("JJ8989", aircraft("YY8890", "Boeing 747", num_rows=22, num_seets_pr_row=6))
print("This is airplane data:\n{0}\n{1}\n{2}".format(f.exportcleanvalue(), f.number(), f.exportcleanvalue()))
f.allocate_seat("1A", "Guido Van Rossum")
f.allocate_seat("12A", "Anders Hejlsberg")
f.allocate_seat("12B", "Richard Hickey")
pp(f._seating)
f.relocate_passenger("1A", "12C")
#pp(f._seating)
print(f.num_available_seats())
f.allocate_seat("12D", "Richard Nielsen")
print(f.num_available_seats())
#print(f.make_boarding_cards(console_card_printer))
print(a.model())
#NewDoc.writethis("Hello is this working???")

#Choose seats


#Print boardingcard

