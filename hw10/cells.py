class Cell:
    def __init__(self, cell_count):
        self.cell_count = int(cell_count)

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Only Cell can be added')
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Only Cell can be substracted')
        if self.cell_count < other.cell_count:
            raise ValueError('Subtraction cannot be performed')
        return Cell(self.cell_count - other.cell_count)

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Only Cell can be multiplicated')
        return Cell(self.cell_count * other.cell_count)

    def __floordiv__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Only Cell can be divided')
        return Cell(self.cell_count // other.cell_count)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Only Cell can be divided')
        return Cell(self.cell_count / other.cell_count)

    def make_order(self, cells_in_row):
        rows = self.cell_count // cells_in_row
        last_row_count = self.cell_count - rows * cells_in_row
        return ('*' * cells_in_row + '\n') * rows + '*' * last_row_count


my_cell1 = Cell(10)
my_cell2 = Cell(4)

new_cell_sum = my_cell1 + my_cell2
print(f'{type(new_cell_sum)} {new_cell_sum.cell_count}')

new_cell_sub = my_cell1 - my_cell2
print(f'{type(new_cell_sub)} {new_cell_sub.cell_count}')

new_cell_mul = my_cell1 * my_cell2
print(f'{type(new_cell_mul)} {new_cell_mul.cell_count}')

new_cell_div = my_cell1 // my_cell2
print(f'{type(new_cell_div)} {new_cell_div.cell_count}')

print(my_cell1.make_order(4))