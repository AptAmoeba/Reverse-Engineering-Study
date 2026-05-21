Let me share something really cool I ran into. 

<img width="884" height="353" alt="image" src="https://github.com/user-attachments/assets/7c67d821-2b6e-4355-b3d0-8cbe55766f22" />

This is a snippet of code from the High-Level IL part of a function. The screenshoted code starts by checking if the internet handle works. If so, it proceeds.

It sets some variables, then later passes them into mw_DecryptXOR, and sets the decrypted strings into a new variable to user later on.

- Tyhe EncStr_3 and EncStr_2 make total sense, because they're setting a data range and then a string into a variable to get decrypted. That makes sense.

- But the following highlighted variables made ZERO sense:

<img width="884" height="372" alt="image" src="https://github.com/user-attachments/assets/6fc92c44-0380-4d55-bfc8-f18d581617c0" />

**The highlighted sections in yellow were what I was really confused about. They made no sense to me!!**

It looked like they were initializing and setting variables to something incomprehensible! Even knowing the manual decryption key, they didn't make sense decrypted like the other ones did. 

&nbsp;

NOTE my actual mouse highlight, where each &EncStr variable is passed to mw_Decrypt-XOR with a given length (0xNumber)(In this case, EncStr's length was 0x14), and the result of that is then stored in a NEW variable. 

&nbsp;

## Solution
After (now embarrassinly, as I realize) many hours, I had a thought, brought to me by a mentor:

What if:
- Either the decompilation was wrong initially in what Type these variables were (most are *supposedly* "int64_t") and it was messing them up?
- OR, what if the Malware Author initialized them in a gross way to confuse decompilers?

Therefore, looking at the lower section where those variables are passed through the XOR Decrypt function, what if they were originally meant to have the same Type as their final types that they are then assigned ("char")? 

So, I tested my theory. going up to the first variable assignment, I hovered over EncStr's "int64_t" type, pressed "Y" (to change the type), and followed this format:
```char EncStr[<Hex size>]```

So, knowing that the lower function set the first EncStr size to 0x14, here's what I set it to:
```char EncStr[0x14]```

I hit Accept to approve the Type change, and BAM!:

(### Todo: Put gif/video of converting type here)

<img width="884" height="120" alt="image" src="https://github.com/user-attachments/assets/f84a7365-2f28-42ed-ac55-11b767e2d496" />

Look at that!! EncStr is now properly formatted and makes sense! We have a usable encrypted source string that later gets passed to the decryption function!!! That was it!

EncStr_1 (and the others below it) are still not fixed. So, fixing all of them (and re-typing EncStr_3 to not be void and EncStr_2 to not be int64_t) anymore and to match the others!), here's what my original screenshot would look like now!:
<img width="885" height="327" alt="image" src="https://github.com/user-attachments/assets/866d1988-e792-4782-a5b5-1097d633825f" />

Look at that! It's so much cleaner now!

We see all of the encrypted strings right there in front of us, and can now clearly see that they are all placed into the decryption function below.

&nbsp;

-----

So, we've cleaned up the Types of these variables. You might be wondering how these variables were then used! What did they look like decrypted? Well, I'll show you!

Let's start with a part of the above code I left out:
<img width="844" height="156" alt="image" src="https://github.com/user-attachments/assets/5c1be8d5-b073-406f-a4ca-b4fadb3bbb55" />

This is a bit confusing if you only look at resize_t as-is, without marking up your sample. So... let's mark it up and take another look!:

<img width="883" height="158" alt="image" src="https://github.com/user-attachments/assets/6e15afaf-15b4-42fe-b8df-8ac368c84294" />

What I changed:
- Manually decrypted each part and renamed the final variables to _"<DecryptedContent>"

Great! Looks like it's building a URL, judging by the individual contents. This last bit about resizing (and now uint64_t after renaming a few) is just taking the length of each component and storing it in rax_13. You can probably guess that rax_13 is going to be used later as simply the total length to be allocated, likely for when the full URL is constructed!

&nbsp;

## Putting it All Together

Finally, let's show the code immediately after the original screenshot (you'll see where my first screenshot ends overlapping at the 2600c2a61 instruction.). This is what immediately follows it:

<img width="887" height="163" alt="image" src="https://github.com/user-attachments/assets/230dc118-b0df-4328-8dc1-8a3ecffad7fa" />

^### Replace the "CanReachInternet" with "hInternet"!

It is important that we know how strcat works in C to understand what this is doing! Strcat APPENDS data onto a given string, so it keeps the old data and concatenates (adds) your new data to it. 

(strcat example source c)

