# DISKO 3
## Category: Medium, Forensic, picoGym Exclusive
### Author: Darkraicg492

### Description
Can you find the flag in this disk image? This time, its not as plain as you think it is!
Download the disk image here.

### Write-Up
Jadi kali ini kita dapat sebuah FAT filesystem yang kita diminta untuk mencari flag yang kemungkinan ada di partisi file ini. Jadi aku langsung buka menggunakan salah satu tools command line dari sleuth kit yaitu fls. Disini aku menemukan sebuah flag yang di compress dengan gunzip yang berada di offset
522628. Jadi dari situ aku langsung coba extract menggunakan icat.

```
└─$ fls -f fat -r disko-3.dd
d/d 4:	log
+ d/d 22:	private
+ d/d 24:	sysstat
+ d/d 26:	stunnel4
++ r/r 70:	stunnel.log
+ d/d 28:	mysql
+ d/d 30:	inetsim
++ d/d 102:	report
+ d/d 32:	installer
++ d/d 134:	cdebconf
+++ r/r 150:	questions.dat
+++ r/r 152:	templates.dat
++ r/r 136:	Xorg.0.log
++ r/r 138:	partman
++ r/r 140:	syslog
++ r/r 143:	hardware-summary
++ r/r 145:	status
++ r/r 519091:	lsb-release
+ r/r 519123:	vmware-vmsvc-root.2.log
+ r/r 519125:	kern.log.4.gz
+ r/r 519127:	Xorg.0.log
+ r/r 519130:	vmware-network.4.log
+ r/r 519132:	boot.log
+ r/r 519134:	syslog.3.gz
+ r/r 519137:	vmware-vmtoolsd-root.log
+ r/r 522627:	daemon.log
+ r/r 522628:	flag.gz
+ r/r * 522629:	_ESSAGES
+ r/r 522632:	alternatives.log.2.gz
+ r/r 522634:	debug
```

Setelah kita extract data yang berada di offset tersebut, kita dapat sebuah flag: picoCTF{n3v3r_z1p_2_h1d3_26d4f233}
```
┌──(w4llnut_07㉿kali)-[/tmp]
└─$ icat -f fat disko-3.dd 522628 > flag.gz
                                                                                                                                                                                                                                            
┌──(w4llnut_07㉿kali)-[/tmp]
└─$ ls                      
disko-3.dd  flag  flag.gz
                                                                                                                                                                                                                                            
┌──(w4llnut_07㉿kali)-[/tmp]
└─$ cat flag
Here is your flag
picoCTF{n3v3r_z1p_2_h1d3_26d4f233}
```

**Flag: picoCTF{n3v3r_z1p_2_h1d3_26d4f233}**
