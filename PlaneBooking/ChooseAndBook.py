"""" Test """

class Flight:
    
    def __init__(self, number, aircraft):
        
        #
        if not number[:2].isalpha():
            raise ValueError("Not a valid flight: {0}".format(number))
        #
        if not (number[2:].isdigit() and int(number[2:]) <= 99999):
            raise ValueError("Not a valid flight: Incorrect numeric value")
        #
        self._number = number
        self._aircraft = aircraft
        self._export = aircraft.model
        
        #
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
        
        #
        print("The assigned value is: {0}".format(self._number))

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
        self._model = model
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