import dothat.lcd as lcd

total_rows=3
padding=" "*16

class Table():
    def __init__(self, *col_lenths, seperation_char=" ", gap_size=1):
        lcd.clear()
        self.cells = [[],[],[]]
        self.col_settings = []
        self.offset = 0
        if gap_size == 0:
            seperation_char=""
        elif len(seperation_char) > gap_size:
            raise ValueError('Seperation symbols cannot be longer than the gap.')
            pass
        self.col_lenths = col_lenths
        self.seperation_char = seperation_char
        self.starting_point = [0]
        self.seperation_char_location = []
        for col in range(len(col_lenths)):
            self.starting_point.append(self.starting_point[col] + self.col_lenths[col] + gap_size)
            self.seperation_char_location.append(self.starting_point[col] + self.col_lenths[col])
            self.col_settings.append(0)
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

    def set_column_normal(self, col):
        self.col_settings[col]=0

    def set_column_scrollable(self, col):
        self.col_settings[col]=1

    def set_column_right_aligned(self, col):
        self.col_settings[col]=2

    def _write_cell(self, col, row):
        string = self.cells[row][col]
        lcd.set_cursor_position(self.starting_point[col], row)
        lcd.write(string[0:self.col_lenths[col]])

    def _write_cell_scrollable(self, col, row, offset):
        string = self.cells[row][col]
        lcd.set_cursor_position(self.starting_point[col], row)
        if len(string)<=self.col_lenths[col]:
            offset=0
        else:
            offset%=(len(string)+2)
        lcd.write((string+padding)[offset:self.col_lenths[col]+offset])

    def _write_cell_right_aligned(self, col, row):
        string = self.cells[row][col]
        lcd.set_cursor_position(self.starting_point[col], row)
        if len(string)<=self.col_lenths[col]:
            string=string.rjust(self.col_lenths[col])
        lcd.write(string[0:self.col_lenths[col]])

    def update(self):
        for col in range(len(self.col_lenths)):
            if self.col_settings[col] == 0:
                for row in range(total_rows):
                    self._write_cell(col,row)
            elif self.col_settings[col] == 1:
                for row in range(total_rows):
                    self._write_cell_scrollable(col,row,self.offset)
            elif self.col_settings[col] == 2:
                for row in range(total_rows):
                    self._write_cell_right_aligned(col,row)
            else:
                raise ValueError('Unknown col_settings')

    def scroll(self):
        self.offset+=1
        self.update()
