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
    # abs() untuk mengubah bilangan negatif menjadi bilangan positif sebelum disimpan sebagai digit biner.
    # return str(n % 2) + desimal_biner(n // 2) akan mengembalikan string yang berisi digit biner dari n dalam urutan terbalik.
    return "".join(reversed(str(abs(n % 2)) + desimal_biner(abs(n // 2))))
def desimal_biner2(desimal: int):
    ans = ""

    if (desimal == 0):
        return 0
    while (desimal):
        ans += str(desimal & 1)
        desimal = desimal >> 1

    ans = ans[::-1]

    return ans

print(desimal_biner2(222))
print(desimal_biner(222))

print(desimal_biner2(3))
print(desimal_biner(3))

print(desimal_biner2(2))
print(desimal_biner(2))