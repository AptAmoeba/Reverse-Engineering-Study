## Manual
When you see a 256-byte array (or super close to 256 with some adjustments) being looped (usually there are two arrays doing this), it's likely RC4.

If the operation also has a modulo with some value "i % <n>" thrown in there, usually the <n> is being used as a key length?

### Originally Learned Via
1:51 in https://youtu.be/fEAGYjhKzJY?si=Xcwi6YCrStSz6e-A&t=111

&nbsp;

## Via Windows API
SystemFunction032 (from Advapi32.dll)
SystemFunction0322(data,key)
