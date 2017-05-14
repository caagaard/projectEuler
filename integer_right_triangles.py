# For a given perimeter p of a right triangle with integer length sides
# there are only finitely many possible sets of sides lengths {a,b,c}
# This finds the value of p <= 1000 with the most possible sets of side lengths

squares = [0]
for i in range(1,501):
  squares.append(i**2)

perimeters = []

# get sum of valid sets of squares
for a in range(1, len(squares) - 1):
  for b in range(a, len(squares) - 1):
    if squares[a] + squares[b] in squares:
      c = squares.index(squares[a]+squares[b])
      if a+b+c <= 1000:
        perimeters.append(a+b+c)

# see what number under 1000 occurs the most
counters = {}
for length in perimeters:
  if length in counters:
    counters[length] = counters[length] + 1
  else:
    counters[length] = 1

maximum = perimeters[0]
for value in perimeters:
  if counters[value] > counters[maximum]:
    maximum = value

print(maximum, counters[maximum])
