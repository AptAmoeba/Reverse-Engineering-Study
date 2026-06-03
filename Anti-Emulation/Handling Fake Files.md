Most Antivirus engines & EDR have the capability to emulate at least a part of a program when it is subject to more scrunity. 

When the malware makes calls for resources or files, it will feed it emulated handles/fakes of those resources in order to allow it to continue "executing."
Malware can take advantage of this by calling intentionally fake/nonexistent files, using them as canaries.

&nbsp;

Within their analysis engines, if the malware makes a call to a file it knows doesn't exist and it recieves a valid handle to it, it means that it's in an emulated environment.

&nbsp;

### Originally Learned Via
2:52 in https://youtu.be/8jckguVRHyI?si=r2JqvSMBVgGVWPGB&t=172
