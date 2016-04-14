"""" Test """

class Flight:
    
    """No one needs to know about the aircraft class which simplifies the system"""
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
        self._export = aircraft
        
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
        return self._export.model()
    
    #Need to return this
    def returnseating(self):
        return self._seating()

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted (self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())


    def _passenger_seats(self):
        """An iterable series of passenger seating allocations"""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))  

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
        return (range(1, self._num_rows + 1), 
            "ABCDEFGHIJK"[:self._num_seets_pr_row])

def make_flight():
    f = Flight("BA758", aircraft("YY8890", "Boeing 747", num_rows=22, num_seets_pr_row=6))
    f.allocate_seat("12A", "Guido Van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders Hejlsberg")
    f.allocate_seat("1c", "John McCarty")
    f.allocate_seat("1d", "Richard Hickey")
    return f

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = " | Name:   {0}"   \
             "   Flight: {1}"   \
             "   Seat:   {2}"   \
             "   Aircraft{3}"   \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()