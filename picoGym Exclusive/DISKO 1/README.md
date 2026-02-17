# DISKO 1
## Category: Easy, Forensic, picoGym Exclusive
### Author: Darkraicg492

### Description
Can you find the flag in this disk image?
Download the disk image <a href="https://artifacts.picoctf.net/c/538/disko-1.dd.gz">here</a>.

### Write-Up
Jadi simple saja sih di challenge ini kita diberikan sebuah dump File Allocation Table, kita diminta untuk menganalisis sebuah file system yang diberikan. Disini untuk menemukan flagnya, kita hanya perlu strings dan mencari pola picoCTF dan kita akan mendapatkan flagnya

```
└─$ strings disko-1.dd | grep -i "pico"        
_ZN13QsciScintilla10apiContextEiRiS0_
:/icons/appicon
PICONV      
# $Id: piconv,v 2.8 2016/08/04 03:15:58 dankogai Exp $
piconv -- iconv(1), reinvented in perl
  piconv [-f from_encoding] [-t to_encoding]
  piconv -l
  piconv -r encoding_alias
  piconv -h
B<piconv> is perl version of B<iconv>, a character encoding converter
a technology demonstrator for Perl 5.8.0, but you can use piconv in the
piconv converts the character encoding of either STDIN or files
Therefore, when both -f and -t are omitted, B<piconv> just acts
picoCTF{1t5_ju5t_4_5tr1n9_e3408eef}
runtime.(*piController).reset
runtime.(*piController).next
type:runtime.piController
type:oDpiCOiQ
```
**Flag: picoCTF{1t5_ju5t_4_5tr1n9_e3408eef}**
