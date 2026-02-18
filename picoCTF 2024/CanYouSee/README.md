# CanYouSee
## Category: Easy, Forensic, picoCTF 2024, browser_webshell_solveable
### Author: Mubarak Mikail

### Description
How about some hide and seek?
Download this file <a href="https://artifacts.picoctf.net/c_titan/131/unknown.zip">here</a>.

### Write-Up
Jadi di chall ini kita diberikan sebuah gambar, tapi ketika kita coba cek meta datanya dengan exiftool terdapat sebuah encoded string base64: cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==, jadi kita cukup decode aja hehe

```
┌──(w4llnut_07㉿kali)-[/tmp]
└─$ echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==" | base64 -d                
picoCTF{ME74D47A_HIDD3N_d8c381fd}
```
**Flag: picoCTF{ME74D47A_HIDD3N_d8c381fd}**
