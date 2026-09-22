persentase = int(input("Masukkan persentase siswa (%): "))

if persentase >= 90:
    print("Excellent performance")
elif persentase >= 80:
    print("Very Good performance")
elif persentase >= 70:
    print("Good performance")
elif persentase >= 60:
    print("Average performance")
else:
    print("Performance di bawah rata-rata")