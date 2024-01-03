def jumlah_kata(kalimat: str):

  # Membagi kalimat menjadi kata-kata
  kata_kata = kalimat.split()

  kata_kata = [kata for kata in kata_kata]

  # Menghitung jumlah kata
  return len(kata_kata)

kalimat = "Halo saya aldi"
jumlah = jumlah_kata(kalimat)

print(jumlah)