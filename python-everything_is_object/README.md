# Python - Everything is object
## Task 1 - Where are you?

- `id()` returns the unique identifier of an object.
- In CPython, this identifier represents the object's memory address.
## Task 2 - Right count

- Two variables can point to different objects even if both are integers.
- Here, `a = 89` and `b = 100`, so they do not point to the same object.
## Task 3 - Right count =

- In CPython, small integers are cached and reused.
- Since both `a` and `b` are assigned the value `89`, they point to the same object.
## Task 4 - Right count =

- `b = a` makes `b` reference the same object as `a`.
- Assignment does not create a new copy of the object.
## Task 5 - Right count =+

- `b = a + 1` creates a result with a different value.
- `a` points to `89`, while `b` points to `90`, so they do not reference the same object.
