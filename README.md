 

<h1 align="center">
  Devanagari UPI PIN Generator
</h1>

<p align="center">
  Convert Hindi (Devanagari) words into secure UPI PINs using Python.
</p>

<p align="center">
  <img src="image/banner.png" alt="Devanagari UPI PIN Generator" width="500"/>
</p>



---

## 📌 About The Project
This Python script is inspired by **Axis Bank's Devanagari UPI PIN Generation feature**.  
It allows users to **generate a UPI PIN based on a Hindi word written in Devanagari script**.  
Each character in the input word is mapped to a specific number according to a custom logic.

---

## ✅ Features
✔ Generate **4-digit and 6-digit UPI PINs** from Hindi words  
✔ Handles **matras** and special characters  
✔ Prevents invalid input (English letters, numbers)  
✔ Simple and clean CLI interface  
  

---

## 🛠 Tech Stack
- **Python 3**
- **Regex (Unicode)**
- **Time Module**

---

## 📂 Project Structure

```
Devanagari_UPI_PIN_Generator/
│
├── main.py/devanagari_pin.py  
│
├── image/banner.png
│
└── README.md 
```


---

## ▶ How It Works
1. User enters a **Hindi word in Devanagari script** (e.g., `भारद्वाज`, `पर्व`)
2. Each character is mapped to a numeric code
3. Program outputs:
   - **Word Separation**
   - **Numeric Representation**
   - **4-digit PIN**
   - **6-digit PIN**

---

## 📸 Sample Output

```
WELCOME TO DEVANAGARI UPI PIN GENERATOR

Enter a word in Devanagari (उदाहरण: भारद्वाज, पर्व): भारद्वाज

Word Separation: भ ा र द ् व ा ज
4 1 2 6 9 1 1
YOUR DEVANAGARI UPI 4 DIGITS PIN IS HERE: 4126
YOUR DEVANAGARI UPI 6 DIGITS PIN IS HERE: 412691

```
```
WELCOME TO DEVANAGARI UPI PIN GENERATOR

Enter a word in Devanagari (उदाहरण: भारद्वाज, पर्व): त्रिप्टि

Word Separation: त ् र ि प ् ट ि
7 2 1 1 4 0 0 1
YOUR DEVANAGARI UPI 4 DIGITS PIN IS HERE: 7211
YOUR DEVANAGARI UPI 6 DIGITS PIN IS HERE: 721140
```

---
## ⚙ How to Run

1. **Clone the repository**  
   - Open Project in VS Code  

   - Download or clone the repository:

     ```bash
     git clone https://github.com/cjasoncode/Devanagari_UPI_Pin_Generator
     ```
   - Open the folder in **Visual Studio Code**.

2. **Install Python Extension (if not installed)**  

   - Go to **Extensions → Search “Python” → Install**.

   - Make sure VS Code is using the correct Python interpreter (**Python 3.x**).

3. **Install Required Package**  

   - Open the VS Code terminal and run:
     ```bash
     pip install regex
     ```

4. **Run the Script**  
   - Open `devanagari_upi_pin.py` in VS Code. 

   - Click on **Run ▶ button** (top-right) OR run from terminal:
     ```bash
     python devanagari_upi_pin.py
     ```

5. **Enter a Devanagari Word**  
   Example:
   ```bash
      भारद्वाज 
      पर्व
      त्रिप्टि
     ```
## 🚀 Future Enhancements
- ✅ Add **Graphical User Interface (GUI)** with Tkinter  
- ✅ Support for **multiple Indian languages**  
- ✅ Add **export option for PINs**  
- ✅ Web version using **Flask or Django**  

---

## 🧩 Use Cases
- ✔ Educational purpose (learn Regex & Unicode in Python)  
- ✔ Banking concept simulation  
- ✔ Fun project for **Python beginners**  

---

## 📜 License
This project is **for educational purposes only** and is not affiliated with any bank.

---

## 🙌 Credits

- Concept inspired by **Axis Bank's Devanagari UPI PIN feature**  
- Developed by **[cjasoncode](https://github.com/cjasoncode)**  
- Special thanks to the **Python & Open Source Community**  


---

### ⭐ Show Your Support
If you like this project, **give it a star** ⭐ on [GitHub](https://github.com/cjasoncode/Devanagari_UPI_Pin_Generator)

