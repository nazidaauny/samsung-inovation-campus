from utils import konversi_suhu

print("=== KONVERSI SUHU ===")

try:
    nilai = float(input("Masukkan nilai suhu: "))
    dari = input("Dari satuan (C/F/K): ").strip().lower()
    ke = input("Ke satuan (C/F/K): ").strip().lower()

    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        print("Error: Satuan harus hanya C, F, atau K.")
    else:
        hasil = konversi_suhu(nilai, dari, ke)

        if isinstance(hasil, str): 
            print(hasil)
        else:
            satuan_map = {"c": "°C", "f": "°F", "k": "K"}
            print(f"Hasil: {nilai}{satuan_map[dari]} = {hasil:.1f}{satuan_map[ke]}")

except ValueError:
    print("Error: Nilai suhu harus berupa angka.")
