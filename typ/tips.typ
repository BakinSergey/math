#set heading(numbering: "1.")

#set page(
  paper: "a5",
  margin: (x: 1.8cm, y: 1.5cm),
)
#set text(
  // font: "Comic Sans MS",
  font: "New Computer Modern",
  size: 10pt
)
#set par(
  justify: true,
  leading: 0.52em,
)

=== приближенное вычисление квадратного корня из N

$ root(2, N) approx X + (N - X^2) / (2X) $
#[$X^2$ - ближайший квадрат]

#[Например:] 
$ root(2, 20) approx 4 + (20 - 16) / (2 dot 4) approx 4.5 $
$ root(2, 20) eq 4.47 $
