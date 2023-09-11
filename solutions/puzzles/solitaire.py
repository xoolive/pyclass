from puzzle import Puzzle


class Solitaire(Puzzle):
    """
        ·
       x x
      x x x
     x x x x
    x x x x x

    Starting from the following puzzle, jump the tees like checkers,
    one at a time, removing each one you jump, until only one remains.

    """

    pos = (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # type: ignore

    def isgoal(self):
        return sum(self.pos) == 1

    def __repr__(self):
        cumul = []
        for i in range(5):
            idx = i * (i + 1) // 2
            cumul.append(
                (4 - i) * " "
                + " ".join(
                    "x" if j == 1 else "·" for j in self.pos[idx : idx + i + 1]
                )
            )
        return "\n".join(cumul)

    def idx(self, line, column):
        return line * (line + 1) // 2 + column

    def possible(self, line, column, line2, column2):

        if not self.valid(line, column):
            return False

        if not self.pos[self.idx(line, column)]:
            return False

        if not self.valid(line2, column2):
            return False

        if not self.pos[self.idx(line2, column2)]:
            return False

        return True

    def valid(self, line, column):
        return 0 <= line < 5 and 0 <= column <= line

    def __iter__(self):

        for idx, x in enumerate(self.pos):

            if x == 1:
                continue

            # find an empty spot to jump to

            cur_line = max(i for i in range(5) if i * (i + 1) // 2 <= idx)
            cur_col = idx - cur_line * (cur_line + 1) // 2

            # left
            if self.possible(cur_line, cur_col - 1, cur_line, cur_col - 2):
                copy = list(self.pos)
                copy[idx] = 1
                copy[self.idx(cur_line, cur_col - 1)] = 0
                copy[self.idx(cur_line, cur_col - 2)] = 0
                yield Solitaire(tuple(copy))

            # right
            if self.possible(cur_line, cur_col + 1, cur_line, cur_col + 2):
                copy = list(self.pos)
                copy[idx] = 1
                copy[self.idx(cur_line, cur_col + 1)] = 0
                copy[self.idx(cur_line, cur_col + 2)] = 0
                yield Solitaire(tuple(copy))

            # above left
            if self.possible(
                cur_line - 1, cur_col - 1, cur_line - 2, cur_col - 2
            ):
                copy = list(self.pos)
                copy[idx] = 1
                copy[self.idx(cur_line - 1, cur_col - 1)] = 0
                copy[self.idx(cur_line - 2, cur_col - 2)] = 0
                yield Solitaire(tuple(copy))

            # above right
            if self.possible(cur_line - 1, cur_col, cur_line - 2, cur_col):
                copy = list(self.pos)
                copy[idx] = 1
                copy[self.idx(cur_line - 1, cur_col)] = 0
                copy[self.idx(cur_line - 2, cur_col)] = 0
                yield Solitaire(tuple(copy))

            # below left
            if self.possible(cur_line + 1, cur_col, cur_line + 2, cur_col):
                copy = list(self.pos)
                copy[idx] = 1
                copy[self.idx(cur_line + 1, cur_col)] = 0
                copy[self.idx(cur_line + 2, cur_col)] = 0
                yield Solitaire(tuple(copy))

            # below right
            if self.possible(
                cur_line + 1, cur_col + 1, cur_line + 2, cur_col + 2
            ):
                copy = list(self.pos)
                copy[idx] = 1
                copy[self.idx(cur_line + 1, cur_col + 1)] = 0
                copy[self.idx(cur_line + 2, cur_col + 2)] = 0
                yield Solitaire(tuple(copy))


if __name__ == "__main__":
    t = Solitaire()
    for seq in t.solve(depthFirst=True):
        print(seq)
