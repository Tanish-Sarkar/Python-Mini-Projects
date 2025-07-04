# 🔢 Number to Text Converter 📝

-----

This Python script is a handy utility that converts numerical digits into their corresponding word representations. It supports both the **International** (Millions, Billions) and **Indian** (Lakhs, Crores) numbering systems, and keeps a persistent record of all your conversions.

-----

## ✨ Features

  * **Number to Words Conversion**: Converts integers into their English word equivalents.
  * **Dual Numbering Systems**: Choose between:
      * **International System**: (e.g., Thousand, Million, Billion)
      * **Indian System**: (e.g., Thousand, Lakh, Crore)
  * **Conversion History**: All successful conversions (number and its word form) are saved to a file.
  * **View History**: Easily display all past conversions from the saved file.
  * **Clear History**: Option to clear the entire conversion history.
  * **User-Friendly Interface**: Simple command-line interaction.

-----

## 🚀 How to Run

1.  **Save the Code**: Ensure the provided Python code is saved as `NumberToText.py`.
2.  **Run from Terminal**: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the script using:
    ```bash
    python NumberToText.py
    ```

-----

## 💡 How to Use

Upon running the script, you'll be prompted to choose a numbering system and then to enter numbers for conversion.

1.  **Select Numbering System**:

      * Enter `1` for the **International** system.
      * Enter `2` for the **Indian** system.

2.  **Enter Numbers for Conversion**:

      * Type a positive integer (e.g., `202`, `150000`, `12345678`) and press Enter.
      * The script will display the number and its word equivalent (e.g., `202 - Two Hundred Two`).
      * This conversion will also be appended to `numbers.txt`.
      * Continue entering numbers as long as you wish.

3.  **Quit Conversion Input**:

      * To stop entering numbers, simply press `Enter` without typing any number.

4.  **Manage History**:

      * After quitting the number input, you'll be prompted to either `View` or `Clear` the history:
          * Type `view` to display all saved conversions from `numbers.txt`.
          * Type `clear` to empty the `numbers.txt` file.
          * Any other input will simply exit the program without performing a history action.

-----

## 💾 History Storage

All your number-to-word conversions are automatically saved in a file named `numbers.txt` in the same directory as your `NumberToText.py` script. This ensures your conversion history is preserved across sessions.

-----