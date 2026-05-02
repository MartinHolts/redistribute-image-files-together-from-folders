# 🛠️ Image Consolidator: Script to EXE Guide

Follow these steps to set up your environment, create the script, and compile it into a single `.exe` file.

---

## 1️⃣ Setup (If Python is missing)
If you don't have Python installed:
1. Download it from [python.org](https://www.python.org/downloads/).
2. **IMPORTANT:** During installation, check the box that says **"Add Python to PATH"**.

---

## 2️⃣ Create the Script File
1. Create a new folder on your Desktop.
2. Right-click inside the folder > **New** > **Text Document**.
3. Rename it to `consolidate.py` (make sure the `.txt` extension is gone).
4. Right-click the file > **Edit** (with Notepad or VS Code) and paste your Python code into it. Save and close.

---

## 3️⃣ Build the EXE (The One-Liner)
1. Open your folder where `consolidate.py` is saved.
2. Click the **Address Bar** at the top of the window, type `cmd`, and press **Enter**. This opens the terminal directly in that folder.
3. **Copy and paste the entire line below** into the black window and press **Enter**:

```bash
pip install pyinstaller && pyinstaller --onefile --noconsole consolidate.py
```

---

## 4️⃣ Result
The process will take about 30-60 seconds.
Once finished, open the new **dist** folder.
Your **consolidate.exe** is ready!
Move this EXE into the folder with your "N1, N2, MH" folders and run it. It will work silently and close itself when finished.

**Cleanup:** You can delete the build folder and consolidate.spec file once the EXE is created.
