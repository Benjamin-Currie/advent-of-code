# advent-of-code


## Set Up

1. Create a virtual environment
2. Install requirements from `requirements.txt`
3. Log in to [advent of code](https://adventofcode.com/2024) and then open the browsers dev tools to access your session cookie
4. Add your token to `/Users/[YOUR_USER]/.config/aocd/token`

## General Guide

1. When each new puzzle is available you should navigate to the correct directory:

```
$ cd 2024/day_01
```

and then run:

```
python aoc202401.py
```

Replacing `aoc202401.py` with the correct date i.e. on the 5th day you would replace that with `aoc202405.py`

This will fetch the puzzle input for that day and create a new file named `input.txt` in the current directory.

It will also output the solutions for you once you've filled in `part_one` and `part_two` for that day or `None` where the
functions haven't been updated yet.

## Testing

The first part of this is a little more manual. You'll need to copy the values from the example given in the puzzle and add them
to `example_one.txt` (for part one) and `example_two.txt` (for part two).

There are some boilerplate tests set up for each day that are currently being skipped. When you're ready to run the tests just delete
lines 17, 22, 27, 32.

Once you're ready to test your solution, it's best to check it works against the examples and that's exactly what these tests will do for you.

You can run all the tests for that day by simply running `pytest` from the directory of the day you're working on.
