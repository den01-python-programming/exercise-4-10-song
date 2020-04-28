# Exercise 4.10 Song

Create a class called `Song`. The song has the instance variables `name` (string) and `length` in seconds (integer). Both are set in the `def __init__(self, name, length)` constructor. Also, add to the object the methods `def name(self)`, which returns the name of the song, and `def length(self)`, which returns the length of the song.

The class should work as follows.

```python
garden = Song("In The Garden", 10910)
print("The song " + garden.name() + " has a length of " + str(garden.length()) + " seconds.")
```

```plaintext
The song In The Garden has a length of 10910 seconds.
```
