# Flag in Flame
## Category: Forensics, picoMini by CMU-Africa, browser_webshell_solvable
### Author: Prince Niyonshuti N.

### Description
The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log. <br>
Download the encoded data here: Logs Data. Be prepared—the file is large, and examining it thoroughly is crucial.

### Write-Up
Jadi di chall kali ini kita diminta untuk menganalisis suatu log file tapi isi dari log file tersebut tidak biasa dan ada teks yang di encoded dengan base64 encode. kurang lebih isinya seperti ini

```
iVBORw0KGgoAAAANSUhEUgAAA4AAAASACAIAAAAh8bSOAAEAAElEQVR4nOz919MsyZUniP3OcY....
```
jadi aku coba buka file ini di cyberchef kemudian coba decode from base64 untuk lihat hasilnya. Jika diperhatikan, hasilnya adalah sebuah png file, dilihat dari signature filenya yang mngandung kata PNG

<img width="1541" height="781" alt="image" src="https://github.com/user-attachments/assets/5a0b865d-8f5b-44ff-87e3-dd759bdf43a6" />

dari sini kita bisa langsung saja download hasil decodenya dan simpan di direktori. kemudian ketika kita cek file hasil download tadi seperti ini

```
└─$ file download.dat 
download.dat: PNG image data, 896 x 1152, 8-bit/color RGB, non-interlaced
```
terlihat ini adalah PNG image data yang bisa kita buka


Jika kita buka filenya, maka kita akan menmukan sebuah baris hexadecimal: 7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F62653836303237397D

<img width="763" height="415" alt="image" src="https://github.com/user-attachments/assets/69aa7cbc-25cc-47d8-be0a-bcc1b15d8e80" />

Coba ubah hexadecimal tersebut menjadi sebuah ascii letter maka kita akan dapat hasil sebuah flag: picoCTF{forensics_analysis_is_amazing_be860279}

**Flag: picoCTF{forensics_analysis_is_amazing_be860279}**
