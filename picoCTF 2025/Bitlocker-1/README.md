# Bitlocker-1
## Category: Medium, Forensic, picoCTF 2025
### Author: Venax

> This problem cannot be solved in the webshell.

### Description
Jacky is not very knowledgable about the best security passwords and used a simple password to encrypt their BitLocker drive. See if you can break through the encryption!
Download the disk image <a href="https://challenge-files.picoctf.net/c_verbal_sleep/9e934e4d78276b12e27224dac16e50e6bbeae810367732eee4d5e38e6b2bb868/bitlocker-1.dd">here</a>

### Write-Up
Jadi di sini kita diberikan sebuah disk image file yang ter-enkripsi oleh bitlocker. Tugas kita di sini adalah untuk menemukan password atau key agar bisa mendekripsi file systemnya

Pertama, di sini aku menggunakan tools "bitlocker2john" untuk melakukan pengecekan pada disk image dan menemukan hashnya yang kemudian aku simpan di .txt file
```
└─$ bitlocker2john -i bitlocker-1.dd > bitlocker_hash.txt

Signature found at 0x3
Version: 8 
Invalid version, looking for a signature with valid version...

Signature found at 0x2195000
Version: 2 (Windows 7 or later)

VMK entry found at 0x21950c5

VMK encrypted with Recovery Password found at 0x21950e6
Searching AES-CCM from 0x2195102
Trying offset 0x2195195....
VMK encrypted with AES-CCM!!

VMK entry found at 0x2195241

VMK encrypted with User Password found at 2195262
VMK encrypted with AES-CCM

Signature found at 0x2c1d000
Version: 2 (Windows 7 or later)

VMK entry found at 0x2c1d0c5

VMK entry found at 0x2c1d241

Signature found at 0x373a000
Version: 2 (Windows 7 or later)

VMK entry found at 0x373a0c5

VMK entry found at 0x373a241
```


Ketika kita coba baca hasil dari temuan hashnya, kita bisa memilih menggunakan beberapa temuan bitlocker hash. Karena deskripsi soal memberitahu kalau password yang digunakan itu lemah, kita bisa menggunakan $bitlocker$0$ untuk melakukan cracking dengan JTR dengan mode cepat, meskipun false positive kemungkinan lebih tinggi tapi ini bisa dicoba karena memang password user yang digunakan tergolong rentan
```
└─$ cat bitlocker_hash.txt
Encrypted device bitlocker-1.dd opened, size 100MB
Salt: 2b71884a0ef66f0b9de049a82a39d15b
RP Nonce: 00be8a46ead6da0106000000
RP MAC: a28f1a60db3e3fe4049a821c3aea5e4b
RP VMK: a1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58

UP Nonce: d04d9c58eed6da010a000000
UP MAC: 68156e51e53f0a01c076a32ba2b2999a
UP VMK: fffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d


User Password hash:
$bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
Hash type: User Password with MAC verification (slower solution, no false positives)
$bitlocker$1$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
Hash type: Recovery Password fast attack
$bitlocker$2$16$2b71884a0ef66f0b9de049a82a39d15b$1048576$12$00be8a46ead6da0106000000$60$a28f1a60db3e3fe4049a821c3aea5e4ba1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58
Hash type: Recovery Password with MAC verification (slower solution, no false positives)
$bitlocker$3$16$2b71884a0ef66f0b9de049a82a39d15b$1048576$12$00be8a46ead6da0106000000$60$a28f1a60db3e3fe4049a821c3aea5e4ba1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58
```


Di sini kita dapat kandidat password, meskipun ada tanda ini false positive (?) tapi kita tetap bisa coba password/key tersebut untuk dekripsi bitlockernya. Karena aku melakukan mounting di direktori saat ini, aku membuat dua direktori baru dulu untuk raw dan hasil dekripsi

```
└─$ john --format=bitlocker --wordlist=/usr/share/wordlists/rockyou.txt hash.txt                                                                                                                      
Note: This format may emit false positives, so it will keep trying even after finding a possible candidate.
Using default input encoding: UTF-8
Loaded 1 password hash (BitLocker, BitLocker [SHA-256 AES 32/64])
Cost 1 (iteration count) is 1048576 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
jacqueline       (?)     
1g 0:00:13:03 0.37% (ETA: 2026-02-25 00:54) 0.001276g/s 82.33p/s 82.33c/s 82.33C/s bolaji..bloomer
Session aborted

┌──(w4llnut_07㉿kali)-[~/forensic/Bitlocker-1]
└─$ mkdir hasil_raw    
                                                                                                                                                                                                                                            
┌──(w4llnut_07㉿kali)-[~/forensic/Bitlocker-1]
└─$ mkdir hasil_isi
```


Dari sini kita bisa gunakan dislocker untuk mendekripsi seluruh isi disk dan mount hasil dislocker-file dengan loop ke direktori hasil isi untuk hasil yang sudah bersih. Setelah itu ketika kita cek direktori hasil_isi maka kita bisa menemukan sebuah file flag.txt di dalamnya
```
┌──(w4llnut_07㉿kali)-[~/forensic/Bitlocker-1]
└─$ sudo dislocker -V bitlocker-1.dd -ujacqueline -- hasil_raw 
                                                                                                                                                                                                                                            
┌──(w4llnut_07㉿kali)-[~/forensic/Bitlocker-1]
└─$ sudo mount -o loop hasil_raw/dislocker-file hasil_isi 
The disk contains an unclean file system (0, 0).
Metadata kept in Windows cache, refused to mount.
Falling back to read-only mount because the NTFS partition is in an
unsafe state. Please resume and shutdown Windows fully (no hibernation
or fast restarting.)
Could not mount read-write, trying read-only

┌──(w4llnut_07㉿kali)-[~/forensic/Bitlocker-1]
└─$ sudo ls -la hasil_isi 
total 13
drwxrwxrwx 1 root       root 4096 Jul 16  2024  .
drwxr-xr-x 4 w4llnut_07 kali 4096 Feb 22 14:50  ..
drwxrwxrwx 1 root       root    0 Jul 16  2024 '$RECYCLE.BIN'
-rwxrwxrwx 1 root       root   43 Jul 16  2024  flag.txt
drwxrwxrwx 1 root       root 4096 Jul 16  2024 'System Volume Information'
                                                                                                                                                                                                                                            
┌──(w4llnut_07㉿kali)-[~/forensic/Bitlocker-1]
└─$ sudo cat hasil_isi/flag.txt 
picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1} 
```

**Flag: picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}**
