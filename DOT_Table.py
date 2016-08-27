import dothat.lcd as lcd

total_rows=3

class Table():
    def __init__(self, *col_lenths, seperation_char=" ", gap_size=1):
        lcd.clear()
        self.cells = [[],[],[]]
        self.scrollable_cols = []
        self.offset = 0
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
            self.scrollable_cols.append(False)
        for row in range(total_rows):
            self.cells[row] = [""] * len(col_lenths)
        del self.seperation_char_location[-1]
        self.draw_seperation_char()

    def draw_seperation_char(self):
        for row in range(total_rows):
            for loc in range(len(self.seperation_char_location)):
                lcd.set_cursor_position(self.seperation_char_location[loc], row)
                lcd.write(self.seperation_char)

    def set_cell(self, string, col, row):
        self.cells[row][col] = string

    def _write_cell(self, col, row):
        string = self.cells[row][col]
        lcd.set_cursor_position(self.starting_point[col], row)
        lcd.write(string[0:self.col_lenths[col]])

    def _write_cell_scrollable(self, col, row, offset):
        string = self.cells[row][col]
        if len(string)<=self.col_lenths[col]:
            offset=0
        else:
            offset%=(len(string))
        lcd.set_cursor_position(self.starting_point[col], row)
        lcd.write(string[offset:self.col_lenths[col]+offset])

    def update(self):
        for col in range(len(self.col_lenths)):
            if self.scrollable_cols[col] == True:
                for row in range(total_rows):
                    self._write_cell_scrollable(col,row,self.offset)
            else:
                for row in range(total_rows):
                    self._write_cell(col,row)

    def scroll(self):
        self.offset+=1
        self.update()
