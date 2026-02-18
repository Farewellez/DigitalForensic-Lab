# RED
## Category: Easy, Forensic, picoCTF 2025, browser_webshell_solveable
### Author: Shuailin Pan (LeConjuror)

### Description
RED, RED, RED, RED
Download the image: <a href="https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png">red.png</a>

### Write-Up
Jadi pada challenge kali ini, kita diberikan sebuah png image yang berwarna merah. Karena sudah jelas ini kemungkinan adalah steganography jadi aku coba strings gambarnya

```
┌──(w4llnut_07㉿kali)-[/tmp]
└─$ strings red.png                           
IHDR
tEXtPoem
Crimson heart, vibrant and bold,
Hearts flutter at your sight.
Evenings glow softly red,
Cherries burst with sweet life.
Kisses linger with your warmth.
Love deep as merlot.
Scarlet leaves falling softly,
Bold in every stroke.x
IDATx
IEND
```
aku ga nemu apa-apa disini, ketika aku gunakan xxd dan binwalk juga tidak ada apa-apa. Jadi kemungkinan kecurigaanku ada pada antara bitplane atau LSB yang biasanya dibuat tempat untuk menyembunyikan data biner yang digabung. kenapa? karena jika kita mengubah nilai biner (1 atau 0) dari bit paling kanan maka warna tidak akan terlihat ada perubahan.

Di sini aku menggunakan tools StegOnline untuk mengecek bit paling kanan dari pixel RGBA dan aku dapat sebuah strings base64 encoded: cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ== 
<br> Jika kita decode maka kita akan dapat flagnya <br>
<img width="1902" height="841" alt="image" src="https://github.com/user-attachments/assets/28b4e915-b305-4ac2-ab28-0c31057b5e75" />

```
┌──(w4llnut_07㉿kali)-[/tmp]
└─$ echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}                                                                                                                                                                                                                                            
```
**Flag: picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}**
