---
layout: default
title: Solving puzzles
permalink: /puzzles
---

## Solving puzzles

This problem is to encourage you to follow the excellent presentation by Raymond Hettinger at PyCon 2019. In particular, you should now be able to solve the following problems with the generic solver presented [on this page](https://rhettinger.github.io/puzzle.html). You will find the model for two problems.

<div class="alert alert-warning">
<b>Note</b> &nbsp;&nbsp;
The video is embedded here for reference, I recommend you do watch the video, but later, as it may be easier to understand the subtle parts after you completed at least one of the puzzles.
</div>

<iframe width="420" height="315" src="https://www.youtube.com/embed/_GP9OpZPUYc"></iframe>

The solver is based on the iteration protocol, in particular the `__iter__` method and `yield` keywords to generate neighbouring positions. The author insist in their video, but a breadth-first search (BFS) is called, which is the safest option when the shortest path solution needs to be found or when some paths have a potential to wander around infinitely (i.e. you can randomly twist a Rubik's cube all day and never come near a solution). However, you may want to switch to depth-first search (DFS) for the puzzles below, using the option `solve(depthFirst=True)`.

<div class="alert alert-danger">
<b>Warning</b> &nbsp;&nbsp;
When you work on the puzzles, you may encounter the following exception:
<br/>
<code>
IndexError: pop from an empty deque exception
</code>
<br/>
This means you finished exploring the search without finding a solution: check your <code>isgoal()</code> function first, then that you did not miss any possible neighbour during the iteration.

</div>

### The n-queen problem (easy)

```python
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
    pos = tuple()

    def isgoal(self) -> bool:
        pass # <<-- FILL HERE

    def __repr__(self):
        return "" #  <<-- FILL HERE

    def __iter__(self):
        # This is wrong, but you should yield such a structure
        #  >> FILL HERE <<
        yield NQueens(self.pos)
```

### The Solitaire problem (complicated, not hard)

```python
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

    pos = (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    def isgoal(self) -> bool:
        return sum(self.pos) == 1

    def __repr__(self):
        return ""  # <<-- FILL HERE

    def __iter__(self):
        # This is wrong, but you should yield such a structure
        #  >> FILL HERE <<
        yield Solitaire(self.pos)
```

[↑ Home](.) \| [>> Next](asyncio)
