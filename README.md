
![Project Header](https://capsule-render.vercel.app/api?type=blur&height=300&color=gradient&text=Expense%20Tracker%20(PySide6)&textBg=false)


A simple desktop expense tracker built with **PySide6 (Qt for Python)**.
Log daily expenses quickly and automatically save every entry into a **JSON file**.
Clean UI + Material theme + zero complicated validation - just enter and save.

---

##  Features

* Add expense details:

  * Type
  * Amount
  * Note
  * Payment Method
  * Date of expense

* Auto‑generated creation timestamp
* Saves data to `JSON`
* Creates `output/expenses.json` automatically
* Material UI theme (qt-material)
* Statement preview after every entry
* Error box (hidden by default, shown on submit)
* No strict validation (logs exactly what you type)

---

###  Installation

### 1. Install Python (3.9+ recommended)

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run the app

From project root:

```bash
python menu.py
```

---

### UI Overview

##### Expense Section

Enter:

* Type (dropdown)
* Amount
* Note (optional)
* Payment method

##### Date Section

* Pick expense date
* Shows today’s date
* Shows selected date label

##### Statement Section

* Displays last saved entry

##### Error Section

* Hidden initially
* Appears on submit

---

###  File Structure

```
src/
   menu.py
   output/
       expenses.json
```

* `output/` folder is auto-created on first save

---

###  JSON Format

Each entry is appended like this:

```json
[
  {
    "type": "Foods",
    "amount": "250",
    "note": "Burger",
    "method": "UPI",
    "date_given": "09/02/2026",
    "date_created": "10/02/2026 18:32:11"
  }
]
```

### Fields

| Field        | Description               |
| ------------ | ------------------------- |
| type         | Expense category          |
| amount       | Any text/number           |
| note         | Description or "None"     |
| method       | Payment method            |
| date_given   | Date user selected        |
| date_created | Auto timestamp when saved |

---

### License

Free for personal or learning use.
