from puzzle import Puzzle


class NQueens(Puzzle):
    """
    - ♛ - - - - - -
    - - - ♛ - - - -
    - - - - - ♛ - -
    - - - - - - - ♛
    - - ♛ - - - - -
    ♛ - - - - - - -
    - - - - - - ♛ -
    - - - - ♛ - - -

    Given n=8 queens, place them on an n × n chessboard so that no two queen
    attach each other in line, column and diagonal.
    """

    n = 8
    pos = tuple()  # type: ignore

    def isgoal(self):
        return len(self.pos) == self.n

    def __repr__(self):
        n = len(self.pos)
        return "\n".join(
            [
                " ".join("♛" if j == self.pos[i] else "-" for j in range(n))
                for i in range(n)
            ]
        )

    def __iter__(self):
        i = len(self.pos)
        for qi in range(8):
            if all(
                qi != qj and abs(qi - qj) != abs(i - j)
                for j, qj in enumerate(self.pos)
            ):
                yield NQueens(tuple([*self.pos, qi]))


if __name__ == "__main__":
    solution = NQueens().solve(depthFirst=True)[-1]
    print(solution)
