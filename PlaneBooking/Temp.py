#"""" This is the plane booking tool """

#class flight:
    
#    def __init__(self, number):
#        if not number[:2].isalpha():
#            raise ValueError("Not a valid flight: {0}".format(number))

#        self._number = number
#        self._aircraft = aircraft

#        rows, seats = self._aircraft.seating_plan()
#        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

#    def number(self):
#        return self.number

#    def airline(self):
#        return self.number[:2]
    
#    def aircraft_model(self):
#        return self.aircraft_model

#class aircraft:

#    def __init__(self, registration, model, num_rows, num_seets_pr_row):
#        self._registration = registration
#        self._model = model
#        self._num_rows = num_rows
#        self._num_seets_pr_row = num_seets_pr_row

#    def registration(self):
#        return self.registration

#    def model(self):
#        return self.model

#    def seating_plan(self):
#        return (range(1, self._num_rows + 1), "ABCDEFGHIJK"[:self._num_seets_pr_row])