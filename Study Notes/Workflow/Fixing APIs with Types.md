When reviewing malware, you will encounter things like API hashing that cause Binja to avoid recognizing and formatting official typing for called functions. 

&nbsp;

**Take the following 2 screenshots of the exact same code:**

(**before**) This guide will show you how to go from this default HLIL interpretation:

<img width="841" height="61" alt="image" src="https://github.com/user-attachments/assets/dc834d75-3b6d-42e9-b149-c8e2a7a50b6a" />



(**after!**) To THIS, after cleanup:

<img width="1006" height="80" alt="image" src="https://github.com/user-attachments/assets/66b935e0-627f-4e39-aee9-c3d93c1ccc95" />

*^Note: "data_Evil-Payload" is the memory location where the payload is inserted. This is Reserving that location to have ReadWrite perms in order to set up the payload, and it will later use another API to set the perms to Execute for detonation.*

*So much cleaner! Woah!*

&nbsp;

## Understanding When to Do this
To clean these up, you can set Types and Enums yourself which will inherently clean up the High-Level IL view!


Simply press Y when highlighting what should be an MS API, and input the correct type information.

(Examples to come)

## Applying Types / Creating Custom Types


## Applying Enums / Creating Custom Enums



### Searching for Existing Enums in Binja
Binja might already have an enum for what you're looking for.



