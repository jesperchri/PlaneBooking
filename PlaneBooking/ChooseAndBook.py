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

        # [:2] = String slicing
        if not number[:2].isupper():
            raise ValueError("Invalid route number '{0}'".format(number))

        #
        self._number = number
        self._aircraft = aircraft
        self._export = aircraft
        
        #Unpacking tuples into seperate lists and then packing them into a dictionary
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
        
        #
        print("The assigned value is: {0}".format(self._number))

    def number(self):
        return self._number

    def airline(self):
        return self.number[:2]
    
    def aircraft_model(self):
        return self.aircraft_model()

    # "_" because its an implementation detail
    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter.  
        Args:
            Seat: A seat designator such as 12C
        Returns:
            A tuple containing an integer and a string for row and seat.
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter: {0}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row: {0}".format(row_text))

        if row not in row_numbers:
            raise ValueError("Invalid row number: {0}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.
        Args:
            Seat: a seat designator such as '12C' or '21F'.
            Passenger: The passenger name.
        Raises:
            ValueError: If the seat is unavailable
        """     
        row, letter = self._parse_seat(seat)
 
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.
        Args:
            from_seat: The existing seat designer

        Returns:

        """

        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))
        
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def aircraft_data(self):
        return self._aircraft
    
    def exportcleanvalue(self):
        return self._export.model()
    
    #Need to return this
    def returnseating(self):
        return self._seating()

    def  num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

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
    
    #Seat letters returned as tuple
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

class Aircraft:
    
    #Base class to be inherited
    def num_seat(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"

class Boeing747(Aircraft):
    pass
    #Create a new airplane
    
