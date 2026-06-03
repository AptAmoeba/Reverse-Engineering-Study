Most Antivirus engines & EDR have the capability to emulate at least a part of a program when it is subject to more scrunity. 

When the malware makes calls for resources or files, it will feed it emulated handles/fakes of those resources in order to allow it to continue "executing."
Malware can take advantage of this by calling intentionally fake/nonexistent files, using them as canaries.

&nbsp;

Within their analysis engines, if the malware makes a call to a file it knows doesn't exist and it recieves a valid handle to it, it means that it's in an emulated environment.


## Common Examples
```C
i = <Calling some super obscure function to do something, where it will 99.9999% give you an error in a real env>
if (i = 0){ //Remember that 0 is a success, meaning that i did not product an error. 
    <exit program> //Since this is probably emulated, we exit instead of detonating.
}

```
(or)
```C
i = <Calling some super obscure function to do something, where it will 99.9999% give you an error in a real env>
<Some check using LastError> ~= <No Error Result>
    <exit program> //Since this is probably emulated, we exit instead of detonating.
}
```
(or)
```C
i = <call a file that doesn't exist>
check if succeeded> // If it succeeded, it's probably an emulated env
    <exit program> //Since this is probably emulated, we exit instead of detonating.
}
```

&nbsp;

### Originally Learned Via
2:52 in https://youtu.be/8jckguVRHyI?si=r2JqvSMBVgGVWPGB&t=172
