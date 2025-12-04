<h1 align="center">🌿 Food Chain Simulator</h1>

<p align="center">
  A <b>Class 11 Biology Mini Project</b> built using <b>Python</b> — interactively build and explore food chains! 🐛🦎🦅
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"></a>
  <img src="https://img.shields.io/badge/Subject-Biology-lightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Level-Class%2011-success?style=for-the-badge">
</p>

---

## 🧠 Overview

**Food Chain Simulator** is an interactive Python project for **Class 11 Biology students**.  
It allows users to **build food chains** by selecting organisms at different trophic levels:

- Producer → Primary Consumer → Secondary Consumer → Tertiary Consumer → Apex Predator

The program ensures **trophic logic validation** and can generate **random food chains** with a CSV export option.

---

## ⚙️ Features

✅ Interactive organism selection  
✅ Trophic logic validation  
✅ Random food chain generation  
✅ CSV export (`--random` mode)  
✅ User-friendly CLI  

---

## 🧪 Demo Preview

> **Interactive Mode**

```
Producer:
  1. Grass
  2. Algae
  3. Oak tree
Choose Producer (1-3) or press Enter to pick random: 1

Primary consumer:
  1. Grasshopper
  2. Rabbit
Choose Primary consumer (1-2) or press Enter to pick random: 

Food chain:
Grass → Grasshopper → Frog → Snake → Eagle
```

> **Random Mode (`--random 5`)**

```
✔ Exported 5 chains to chains.csv
```

`chains.csv` example:

```
Producer,Primary consumer,Secondary consumer,Tertiary consumer,Apex predator
Grass,Grasshopper,Frog,Snake,Eagle
Algae,Rabbit,Weasel,Hawk,Lion
```

---

## 🧩 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/himalipatil25/Biology-Projects.git
cd Biology-Projects/Food Chain Simulator
```

### 2. Run the Program

```bash
python simulator.py
```

### 3. Generate Multiple Random Chains (CSV Export)

```bash
python simulator.py --random 10
```

---

## 🧰 Tech Stack

- 🐍 Python 3.x  
- 🎲 Random module  
- 📄 CSV module  
- 🧠 Basic Python logic & lists  

---

## 🎯 Educational Purpose

This project helps students:

- Understand food chains and trophic levels  
- Learn Python fundamentals  
- Explore ecology using programming  
- Practice data generation and CSV handling  

---

## 👩‍🔬 Author

**Himali Patil**

- 📘 Class 11 Science — Biology Project  
- 💼 LinkedIn: https://www.linkedin.com/in/himalipatil26  
- ✉️ Email: your-email@example.com  

---

<h3 align="center">✨ Thanks for visiting my project! ✨</h3>
<p align="center">
  If you like this project, consider giving it a ⭐ on GitHub! <br><br>
  <img src="https://img.shields.io/badge/Keep%20Learning-Explore%20Biology%20+%20Code-orange?style=for-the-badge&logo=python"> 
  <img src="https://img.shields.io/badge/Open%20Source-Contributions%20Welcome-blue?style=for-the-badge&logo=github">
</p>
