import dothat.lcd as lcd

total_rows=3

class Table():
    def __init__(self, *col_lenths, seperation_char=" ", gap_size=1):
        if len(seperation_char) > gap_size:
            raise ValueError('Seperation symbols cannot be longer than the gap.')
            pass
        self.col_lenths = col_lenths
        self.seperation_char = seperation_char
        self.starting_point = [0]
        self.seperation_char_location = []
        for col in range(len(col_lenths)):
            self.starting_point.append(self.starting_point[col] + self.col_lenths[col] + gap_size)
            self.seperation_char_location.append(self.starting_point[col] + self.col_lenths[col])
        del self.seperation_char_location[-1]
        self.draw_seperation_char()

    def draw_seperation_char(self):
        for row in range(total_rows):
            for loc in range(len(self.seperation_char_location)):
                lcd.set_cursor_position(self.seperation_char_location[loc], row)
                lcd.write(self.seperation_char)

    def write_cell(self, string, col, row):
        lcd.set_cursor_position(self.starting_point[col], row)
        lcd.write(string)
