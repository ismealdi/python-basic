def desimal_biner(n):
  """
  Mengkonversi bilangan desimal menjadi biner dengan algoritma rekursif.

  Args:
    n: Bilangan desimal yang akan dikonversi.

  Returns:
    Bilangan biner dari n.
  """

  # Basis kasus
  if n == 0:
    return ""

  # Rekursi
  else:
    # return str(n % 2)
    return "".join(reversed(str(abs(n % 2)) + desimal_biner(abs(n // 2))))

print(desimal_biner(222))
print(desimal_biner(3))
print(desimal_biner(2))