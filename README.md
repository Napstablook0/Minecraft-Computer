# Minecraft Redstone Computer Documentation


## User Manual for My Minecraft Computer

If you want to learn more about my computer or even program and run code on it, this is where I explain everything.

In general, my project is written in a mix of English and French.

I am only 17 years old at the moment of making this project, and it took me about 3 months to complete.

---

## Project Folder Structure

### Example Programs

- The `videos` folder contains recordings of my computer running various programs.
- The `assembly_program` file contains several assembler scripts along with their compiled machine code.

### Assembler and Code Writing

- The `instruction_set_and_screen_protocol` file contains the instruction set for my assembler.
- The `compiler` folder holds the assembler’s compiler, which converts assembly code into machine language that my computer can interpret.
  - For more details, read the comments at the beginning of the Python scripts in the `compiler` folder.
- The `images` folder contains various images to help visualize the physical structure of the computer.

---

## Details About My Computer

### 8-bit Computer

#### Computer Speed

- **7.8 Hz/min** when the game runs at normal speed (`20 ticks per second`).
- The game can be artificially accelerated using commands and the **Carpet mod**, increasing the computer’s processing speed.

#### Computer Memory

- **16 memory registers**  
  - `r0` is a **zero register**  
  - `r14` and `r15` are used to interact with the computer  
  - **Effectively, 13 bytes of usable memory**

#### Supported Operations

- **9 arithmetic and mathematical operations** (see the "assembly" section in `instruction_set_and_screen_protocol`).

#### Screen Interactions

- Ability to turn on a pixel using its **x and y coordinates**.
- Ability to **clear the entire screen** (but not a single pixel individually).

---

## Writing and Running a Program on My Minecraft Computer

### Step 1: Writing an Assembly Code

*If you already have an assembly code, skip this step.*

- To write your assembly code, read the **instruction set** (`instruction_set_and_screen_protocol` file).
- If you need to interact with the screen, also read the **screen protocol** in the same file.

### Step 2: Converting Assembly Code into a Python List

*If your code is already compiled, skip to Step 4.*

- You need to place your assembly script into a **Python list**, where each value in the list is a string containing a line of code.

Example:
```python
SCRIPT_EXAMPLE = [
    "LDI r1 255",
    "LDI r2 40",
    "LDI r3 25",
    "SUB r1 r1 r2",
    "ADD r1 r1 r3",
    "HLT"
]
```

If your script is too long to manually convert into a list, you can ask an AI to do it for you.

### Step 3: Compiling the Code

1. Open the `compiler` folder in a Python code editor.
2. Place your list in the `exemples.py` script.
3. Open `main.py` and replace the following line:  
   ```python
   instructions = EXAMPLE
   ```
   with:
   ```python
   instructions = YOUR_DEFINED_LIST_IN_EXEMPLE_PY
   ```
4. Run `main.py` to compile your code.

### Step 4: Opening the Minecraft World

*If you already have the Minecraft world open, skip this step.*

1. Launch the Minecraft world containing the computer (`redstone computer` folder in the project root).
2. To do this, create a **Forge modpack (version 1.21.1)** and install the **Carpet** and **WorldEdit** mods.  
   - Ensure you download compatible versions for **Minecraft 1.21.1**.
3. Click the **three dots** next to the "Play" button, then click "Open Folder."
4. Place the `redstone computer` world folder inside the `saves` directory.
5. Close the file manager and launch the Forge modpack by clicking "Play."
6. In **Singleplayer mode**, you should see the **"redstone computer"** world. Open it.

### Step 5: Writing the Code into the Minecraft Computer

1. Find the **large light green block** (this is the **instruction memory** where the code will be placed).  
   - (See the image `instruction_memory` in the `images` folder.)
2. Go to the **top of the instruction memory** where a **black block** marks a corner.
3. Each **column** represents one line/instruction of machine language.  
   - The **top bit of each column** is the **most significant bit** in the instruction.  
   - (See `bits_colonne` image in the `images` folder.)
4. The **first instruction** goes in the **column directly below the black block** at the **top-left corner** of the memory.
5. The **second instruction** is placed **to its left** (from the front view), the **third** to the left of the second, and so on.
6. After 8 instructions, the next instruction should be placed **behind** the very first column (front view).
7. In summary, when viewed **from above**, with the **black block at the top-left**, instructions should be placed in **left-to-right, top-to-bottom order**.  
   - (See the image `ordre_ecriture` in the `images` folder.)

8. **Placing a bit:**
   - Open your inventory and search for a **Redstone Block** (not a red wool block).
   - Place the Redstone Block on the **green wool block** in front of the light-emitting block.  
   - (See `placer_bit` image in the `images` folder.)
   - **Redstone Block = `1`**, **No block = `0`**.

### Step 6: Running the Code

1. Between the **instruction memory** and the **screen**, find the **small yellow tower** (the **Program Counter**).  
   - (See `program_counter` in `images` folder.)
2. Press the **right button** at the end of the brown bridge at the base of the yellow tower.  
   - (See `bouton_execution` in `images` folder.)
3. Your program is now **running**!  
   - You can watch the **screen** to your **left** (from the button view).
4. When the **brown bridge circuit stops looping**, it means the program has finished executing (via the `HLT` instruction).
5. To check the **register values**, go to the **large pink structure** to the right of the screen.
   - Each **light-emitting block** represents **one bit**.
   - Each **column of bits** forms a **byte (a register)**, with the **MSB (Most Significant Bit) at the top**.  
   - (See `registres` in `images` folder.)
6. To re-run the program, reset the **Program Counter**:
   - Return to the **execution button** and press the **other button** to its left.
   - The **Program Counter** is now reset, and you can execute a new program.

---

## Conclusion

This project represents a **fully functional 8-bit redstone computer** in Minecraft. It includes:
- A **custom instruction set** for assembly programming.
- **16 memory registers**.
- An **interactive screen**.
- A **compiler** that converts assembly into machine code.
- Big thanks to Mattbatwings and his youtube series, without his videos i would never have done it.


## License

*MIT License

Copyright (c) 2025 HUC Raphael - Napstablook0

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*

## Authors

- **HUC Raphael - Napstablook0** – [GitHub Profile](https://github.com/Napstablook0)  

