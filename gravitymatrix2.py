'''
Andy Huang ECE 160: Gravity Matrix: revision 6

'''

class GravityMatrix:
    def __init__(self, matrix):
        self.matrix = [row[:] for row in matrix]
        self._apply_gravity()
#PLEASE WOrK PLEASE FUCKING WOrK I AM DYING tryna figure this shit out 
    def __str__(self):
        cols = len(self.matrix[0])
        out  = []
        for row in self.matrix:
            line = ''
            for i, val in enumerate(row):
                line += str(val) + ('\t' if i < cols - 1 else '\n')
            out.append(line)
        return ''.join(out)

    def RotateRight(self):
        """Rotate 90° clockwise, then settle with gravity."""
        self.matrix = self._rot_cw_once()
        self._apply_gravity()

    def RotateLeft(self):
        """Rotate 90° counter‑clockwise, then settle with gravity."""
        self.matrix = self._rot_ccw_once()
        self._apply_gravity()

    def _apply_gravity(self):
        rows, cols = len(self.matrix), len(self.matrix[0])
        for c in range(cols):
            keep = [self.matrix[r][c] for r in range(rows) if self.matrix[r][c] != 'm']
            new_col = ['m'] * (rows - len(keep)) + keep
            for r in range(rows):
                self.matrix[r][c] = new_col[r]

    def _rot_cw_once(self):
        rows, cols = len(self.matrix), len(self.matrix[0])
        return [[self.matrix[r][c] for r in reversed(range(rows))] for c in range(cols)]

    def _rot_ccw_once(self):
        rows, cols = len(self.matrix), len(self.matrix[0])
        return [[self.matrix[r][c] for r in range(rows)] for c in reversed(range(cols))]


if __name__ == "__main__":
    matrix = [[1, 'm', 3],
              [4, 'm', 6],
              [7, 8,  'm']]

    gm = GravityMatrix(matrix)
    print("Initial (after gravity):")
    print(gm)

    gm.RotateRight()
    print("After RotateRight:")
    print(gm)

    gm.RotateLeft()
    print("After RotateLeft:")
    print(gm)
