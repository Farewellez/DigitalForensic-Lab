# Hidden in plainsight
## Category: Easy  Forensics  picoMini by CMU-Africa  browser_webshell_solvable  
### AUTHOR: YAHAYA MEDDY  H

### Description
You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.
Download the jpg image <a href="https://challenge-files.picoctf.net/c_amiable_citadel/0e679342e0fe04fa2efa860dda0923cba52108031ac4e1ab519df850c2764b5c/img.jpg">here</a>.

### Write-Up
Jadi di challenge kali ini kita diberikan sebuah image jpeg yang tidak ada yang aneh jika dilihat sekilas. Hanya gambar biasa. Jadi aku coba cek tipe file dengan file command

```
└─$ file img.jpg
img.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9", baseline, precision 8, 640x640, components 3
```
Dan yah ada yang aneh disini yaitu ada encoded base64 "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9". Jadi aku coba decode dan cek hasilnya. <br>
Jika dicek hasilnya di cyberchef seperti ini

<img width="1538" height="576" alt="image" src="https://github.com/user-attachments/assets/d1a0a64e-609b-499a-a173-a00af7db324a" />

Jadi aku berpikir, ini pasti ada hubungannya dengan steghide jadi aku coba extract menggunakan steghide untuk cek apakah ada yang disembunyikan di gambar ini

```
└─$ steghide extract -sf img.jpg
Enter passphrase: 
steghide: could not extract any data with that passphrase!
```
seperti yang terlihat, aku butuh sebuah passphrase untuk melakukan ekstraksi jadi aku coba kembali ke hasil decode tadi

```
steghide:cEF6endvcmQ=
```
Masih ada potongan encoded base64 setelah "steghide: " yang jika didecode di cyberchef akan menghasilkan kata seperti ini

<img width="1541" height="585" alt="image" src="https://github.com/user-attachments/assets/5fbe1b5e-5ee5-4058-ba7c-6acaecee9d03" />

dari sini kita mendapatkan passphrase untuk image ini yaitu: **pAzzword**, kita hanya perlu extract sekali lagi dengan passphrase yang didapat

```
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/forensicpicoCTF/Hiddeninplainsight]
└─$ steghide extract -sf img.jpg
Enter passphrase: 
wrote extracted data to "flag.txt".
                                                                                                                                                                                                                                            
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/forensicpicoCTF/Hiddeninplainsight]
└─$ ls
flag.txt  img.jpg
                                                                                                                                                                                                                                            
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/forensicpicoCTF/Hiddeninplainsight]
└─$ cat flag.txt            
picoCTF{h1dd3n_1n_1m4g3_54e31417}    
```
**Flag: picoCTF{h1dd3n_1n_1m4g3_54e31417}**
