## Why is this string incorrect in Hex View?
While analyzing a demo malware loader I built, I noticed something interesting:

In the malware source code, we have a variable in the .text section (code) called "XOR-Key", which stores a key in the form of bytes:

<img width="681" height="66" alt="image" src="https://github.com/user-attachments/assets/4567cfa4-ad61-4692-8d14-f851e524ce4b" />

(Malware source code)

&nbsp;

In Binja's High-Level Interpreted Language, it resolves the bytes correctly into a plaintext string automatically:
<img width="649" height="66" alt="image" src="https://github.com/user-attachments/assets/e8d9f811-f2ba-45fd-8fcc-447058aea799" />




However, opening this in the Hex Editor view, the key is incorrect:
<img width="619" height="49" alt="image" src="https://github.com/user-attachments/assets/4bdb7963-30f8-4b1d-aa4e-2da54d052aae" />

It's also incorrect in other Hex Editors, like HxD:
<img width="690" height="231" alt="image" src="https://github.com/user-attachments/assets/2c97d388-1aff-4ec3-ad5c-aefc0fa0ce73" />


Showing "XORKey10H.......9" instead of "XORKey109"... why is this?

&nbsp;

### Answer

The answer to our problem reveals itself in the Disassembly view! Let's swap from PE>Hex to PE>Linear>Disassembly above the window and look at that same variable initialization:
<img width="1508" height="176" alt="image" src="https://github.com/user-attachments/assets/d0ec48c8-3bfb-4375-92d4-44983b7312ba" />

Because the string is 9 bytes, it is being handled by two different MOV instructions, rather than one!

The first MOV is setting a qword, which is 8 bytes. But what about the last byte? That's handled by the next MOV instruction as a byte:
<img width="749" height="45" alt="image" src="https://github.com/user-attachments/assets/f9f12cbb-2c3c-4923-bc2b-bd981055f2db" />

And in fact, looking all the way to the right, we see each part of the string being moved in byte form:
<img width="769" height="424" alt="image" src="https://github.com/user-attachments/assets/4311f1ab-7598-4141-aea9-11d802889dea" />

^Using CyberChef to convert 0x303179654b524f58 into plaintext: "01yeKROX"

(It's backwards because it's Little Endian!)

So, what about the "9" that's still missing? Immediately below, we see 0x39 being moved, which is the byte representation of "9"!

Turns out, the Hex Editor view included the opcodes that handle these strings rather than just the stings existing alone.

&nbsp;

### >Subsequent Questions
So, what are all the "H" characters in the Hex View, exactly? idk! Supposedly "H" is the first hex byte of the specific MOV instructions which is why they are there. But... idk.

&nbsp;

### >What if the variable was stored in a different Section? What if it was larger than 9 bytes?

