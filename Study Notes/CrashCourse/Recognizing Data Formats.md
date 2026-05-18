

## Wide-Char (Wchar)

In raw hex, if:
- Every other byte is a padding/null byte ("00", usually), it's UTF-16LE.
  - Example: 61 00 62 00 63 00 = "abc"
- Every 3 OR 4 bytes is data and the rest are padding ("00", usually), it's UTF-32LE.
  - Example: 61 00 00 00 62 00 00 00 63 00 00 00 = "abc"

Unfortunately, just changing the type doesn't seem to preserve the data, so you will have to extract it yourself. 

### Manual wchar (UTF-32LE) Conversion From Improperly-formatted Data

Assuming our function reads data_2600c31c0 for 0x24 bytes:

<img width="290" height="37" alt="image" src="https://github.com/user-attachments/assets/d583f58b-213e-4f0e-8fa7-083a39a0f3e4" />

Cheking data_2600c31c0's content:

<img width="664" height="108" alt="image" src="https://github.com/user-attachments/assets/0f6f39ae-65a6-4b3b-b48c-e0302c838b7f" />


(Highlighted is 0x24 bytes out of the full 0x40-byte allocation)

&nbsp;

Then we would manually read the 0x24, clean it into readable hex, then extract every 4 bytes.


```python
#Binja console script
key = bv.read(0x2600c31c0, 0x24)
clean = (', '.join(f'0x{b:02x}' for b in key))
print(clean.split(",")[::4])
```

View of Binja console:

<img width="959" height="197" alt="image" src="https://github.com/user-attachments/assets/6a216700-7149-4db7-8edd-7bdacf2f3046" />

That's how you extract it was a UTF-323LE wchar! Now you have your clean hex output, so you may do whatever it does with it. In my case, it took the resulting hex into a variable and XOR-decrypted it. So I just pasted that extracted hex into CyberChef, and then decrypted with the known XOR key.

&nbsp;

