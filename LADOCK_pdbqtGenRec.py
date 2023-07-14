import os

# Path ke direktori AutoDockTools
autodocktools_path = "/home/arga/MGLTools-1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24"

# Mengubah direktori kerja ke direktori saat ini
current_dir = os.getcwd()
os.chdir(current_dir)

# Daftar file PDB dalam folder
pdb_files = [file for file in os.listdir() if file.endswith(".pdb")]

# Mengubah setiap file PDB menjadi PDBQT
for pdb_file in pdb_files:
    # Membuat nama file output PDBQT dengan mengganti ekstensi file
    pdbqt_file = pdb_file.replace(".pdb", ".pdbqt")
    
    # Menjalankan perintah pdb_to_pdbqt untuk konversi
    command = f"{autodocktools_path}/prepare_receptor4.py -r {pdb_file} -o {pdbqt_file}"
    os.system(command)
    
    # Menampilkan pesan setelah setiap konversi selesai
    print(f"Konversi {pdb_file} ke {pdbqt_file} selesai.")
