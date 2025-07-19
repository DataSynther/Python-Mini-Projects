# 🖼️ Bitmap Message Program

This program displays a custom user message by overlaying it onto an ASCII art bitmap. It uses a pre-generated bitmap file (`ascii_art.txt`) where each non-space character is replaced by characters from the user’s input, styled based on brightness levels.

---

## 📌 How It Works

- The bitmap is a multiline string loaded from a `.txt` file (`ascii_art.txt`).
- Space characters (`' '`) are treated as empty space.
- Non-space characters (e.g., `@`, `#`, `*`, `:`) define the **intensity** or **darkness** of a pixel.
- Characters from your message replace non-space pixels, styled by intensity:
  - **Darker areas** → UPPERCASE
  - **Medium areas** → Original character
  - **Lighter areas** → lowercase or `.`
- The result is a stylized rendering of your message embedded in the shape of the image.

---

## 📂 Files

- `bitmap_message.py`: The main script that takes user input and renders the message on the bitmap.
- `ascii_art.txt`: The ASCII art bitmap used for display.
- `bitmap_txt_generator.py`: *(Optional)* Script to generate `ascii_art.txt` from an image (not included here).

---

## ▶️ Usage

1. Ensure you have Python 3 installed.
2. Make sure `ascii_art.txt` exists in the same directory. If not, generate it using the `bitmap_txt_generator.py` script.
3. Run the program:

```bash
python bitmap_message.py
```

4. Enter your message (max 100 characters) when prompted.
5. Watch it beautifully render over your ASCII image!

---

## 💡 Example

**Input message:**
```
HelloWorld
```

**Rendered output:**
```
   HHHHHHHHHH   e  lll lo  W      oooooooooooooooooooooooooooooooooooo
  oooooooooooooooor ld ld l  d l dddddddddddddddddddddddddddddddddd o
 oo      ooooooooooo       ldddddddddddddddddddddddddddddddddddddd
         ooooooooooo        H  e lll lo W oooooooooooooooo
          oooooooo         Wooooo   oooooooooooooooooooo l
           ooooooo        ooooooooooooooooooooooo  lll l
 H        H lll ll        ooooooooooo oooooo  WW l
     ...
```

---

## 🔧 Customization

You can modify:
- `ASCII_CHARS = "@%#*+=-:. "` to change shading behavior.
- Character styling rules inside `get_intensity()` and render loop for creative effects.
- `ascii_art.txt` to use different shapes and designs.

---

## ❗ Error Handling

- If `ascii_art.txt` is missing, the program will notify you and exit gracefully.
- Input exceeding 100 characters or left empty will also trigger helpful messages.

---

## 📥 Dependencies

- Pure Python (no external libraries required).
- Optional: `Pillow` if you want to generate ASCII art from `.bmp` files.

---

## 🧠 Future Improvements (Optional Ideas)

- Support for colorized terminal output using ANSI escape codes.
- Integration with image-to-ASCII conversion.
- Saving the rendered message to a text or HTML file.

---

## 👩‍💻 Author

Program inspired by Python bitmap examples and extended for interactive message rendering with intensity mapping.
