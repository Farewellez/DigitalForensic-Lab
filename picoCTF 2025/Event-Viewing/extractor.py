import csv
import sys

# Konfigurasi path file
input_file = '/tmp/chall.csv'
output_file = '/tmp/filtered_chall.csv'

# Daftar semua kolom yang ingin kamu ambil sesuai list tadi
target_columns = [
    "RecordNumber", "EventRecordId", "TimeCreated", "EventId", "Level",
    "Provider", "Channel", "ProcessId", "ThreadId", "Computer",
    "ChunkNumber", "UserId", "MapDescription", "UserName", "RemoteHost",
    "PayloadData1", "PayloadData2", "PayloadData3", "PayloadData4",
    "PayloadData5", "PayloadData6", "ExecutableInfo", "HiddenRecord",
    "SourceFile", "Keywords", "ExtraDataOffset", "Payload"
]

def extract_csv():
    print(f"[*] Membaca file dari: {input_file}...")
    
    try:
        # Buka file input untuk dibaca
        with open(input_file, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            
            # Cek apakah kolom yang di-request benar-benar ada di CSV
            actual_columns = reader.fieldnames
            if not actual_columns:
                print("[-] File CSV kosong atau format tidak dikenali.")
                return

            # Buka file output untuk ditulis
            with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
                # extrasaction='ignore' otomatis membuang kolom dari input yang tidak ada di target_columns
                writer = csv.DictWriter(outfile, fieldnames=target_columns, extrasaction='ignore')
                
                print("[*] Menulis header dan mengekstrak data...")
                writer.writeheader()
                
                row_count = 0
                for row in reader:
                    writer.writerow(row)
                    row_count += 1
                    
        print(f"[+] Selesai! {row_count} baris data berhasil diekstrak ke {output_file}")
        
    except FileNotFoundError:
        print(f"[-] Error: File {input_file} tidak ditemukan. Pastikan path sudah benar.")
    except Exception as e:
        print(f"[-] Terjadi error tidak terduga: {e}")

if __name__ == "__main__":
    extract_csv()
