# Glory of the Garden
## Author: jedavis/Danny
### Category: Easy, Forensic, picoCTF

### Description
This file contains more than it seems.
Get the flag from <a href="https://challenge-files.picoctf.net/c_fickle_tempest/150b6eaad43200d3dc91f98c390e4c6168620b57d0b95a7e9d04c92910bbbe16/garden.jpg">garden.jpg</a>.

### Write-Up
Jadi kita langsung saja cek beberapa byte terakhri raw datanya

```
└─$ xxd garden.jpg| tail -20 
00230460: ed36 9fea e3fa 2d61 5ab2 8548 4796 f75b  .6....-aZ..HG..[
00230470: dce9 c7d2 c463 7091 93c4 ce9a bbd2 27dd  .....cp.......'.
00230480: d696 560c abe4 f93f 2f18 5c71 5a66 dada  ..V....?/.\qZf..
00230490: 1e64 9634 e9d5 80af 9b3c 3fff 002c bf1a  .d.4.....<?..,..
002304a0: a9e2 cfba bf51 5c75 a71b b6e3 7b1f 97cb  .....Q\u....{...
002304b0: 25a5 f5c5 4bda c9a9 6ecf 7ed4 fc4f e1cd  %...K...n.~..O..
002304c0: 2919 e6bb 591b 9c2a 73d2 be71 bdf8 977d  )...Y..*s..q...}
002304d0: e27d 6574 fd3d 1a08 233f bd6e 99c7 6af9  .}et.=..#?.n..j.
002304e0: e2f7 fd6f fc09 ff00 9d6f fc2b ff00 9096  ...o.....o.+....
002304f0: adff 005d ff00 a0ae 7a51 8d4f 68f5 568a  ...]....zQ.Oh.V.
00230500: d9f9 9f63 4b2b c1e5 daf2 7b59 db49 4ba3  ...cK+....{Y.IK.
00230510: f43e b881 5e30 1060 8030 47d6 bacb 58cb  .>..^0.`.0G...X.
00230520: 1046 07b5 7216 df7e 5ff7 c576 363f ebab  .F..r..~_..v6?..
00230530: b70d 18ce 3ccd 6a7e 6b8d af56 b579 39ca  ....<.j~k..V.y9.
00230540: eeef 53ae 8620 31b8 751f 9514 f7fb cff5  ..S.. 1.u.......
00230550: a2bb bdac 9687 98e4 d3b2 e87f ffd9 4865  ..............He
00230560: 7265 2069 7320 6120 666c 6167 3a20 7069  re is a flag: pi
00230570: 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  coCTF{more_than_
00230580: 6d33 3374 735f 7468 655f 3379 3361 3633  m33ts_the_3y3a63
00230590: 6235 6232 377d 0a                        b5b27}.
```
Jadi probset menyembuntikan flagnya setelah byte terakhir dari end of file agar tidak merusak gambar

**Flag: picoCTF{more_than_m33ts_the_3y3a63b5b27}**
