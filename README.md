<h1 style="front-size: 20px; color: blue;">                                     Devanagari UPI PIN Generator</h1> 

This Python script is inspired by **Axis Bank's Devanagari UPI PIN generation![link alt](https://www.devanagaripin.com/)** feature. It allows users to generate a UPI PIN based on a Devanagari (Hindi) word input. Each Devanagari character is mapped to a specific number, and the script generates both 4-digit and 6-digit UPI PINs from the input word.

 ![image alt](https://github.com/cjasoncode/Devanagari_UPI_Pin_Generator/blob/bf042fea6c8a65ba616c3be78b4ed3a553f966cc/Screenshot_20250201-023359~2.png)

<h2 style="front-size: 15px; color: blue;">Features :</h2

- **Devanagari to Number Mapping**: Each Devanagari character is mapped to a unique number, similar to Axis Bank's implementation.
- **UPI PIN Generation**: Generates both 4-digit and 6-digit UPI PINs.
- **Input Validation**: Ensures the input is a valid Devanagari word.
- **Word Separation**: Displays the separated characters of the input word for clarity.
- **Error Handling**: Provides clear error messages for invalid inputs.


<h2 style="front-size: 15px; color: blue;">How It Works : </h2

1. The user inputs a word in Devanagari script (e.g., `भारद्वाज`).
2. The script breaks the word into individual characters.
3. Each character is mapped to a corresponding number using a predefined mapping.
4. The numbers are concatenated to form a base PIN.
5. If the base PIN is 3 digits long, it is duplicated to create a 6-digit PIN.
6. The script outputs both 4-digit and 6-digit UPI PINs.

 
