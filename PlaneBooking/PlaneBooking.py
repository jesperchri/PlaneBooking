"""" This is the plane booking tool """

class Flight:
    
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("Not a valid flight: {0}".format(number))

        self._number = number
        self._aircraft = aircraft
        self._export = aircraft.model

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self.number[:2]
    
    def aircraft_model(self):
        return self.aircraft_model

    def aircraft_data(self):
        return self._aircraft

    def exportcleanvalue(self):
        return self._export

class aircraft:

    def __init__(self, registration, model, num_rows, num_seets_pr_row):
        self._registration = registration
        #self._model = model
        self._num_rows = num_rows
        self._num_seets_pr_row = num_seets_pr_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHIJK"[:self._num_seets_pr_row])

    def export(self):
        return self._model

info = Flight("JJ8989", aircraft("YY8890", "Boeing 747", num_rows = 21, num_seets_pr_row = 6))
#planeinfo = aircraft("YY87878", "Boeing", num_rows = 21, num_seets_pr_row = 6)

print("This is airplane data:\n{0}\n{1}\n{2}".format(info.exportcleanvalue, info.number(), info.exportcleanvalue()))