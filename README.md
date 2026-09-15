# 📚 Book Recommendation System

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A machine learning project designed to recommend books based on user preferences and content similarity.

---

## 📸 Demo & Screenshots
<!-- Add a GIF or screenshot of your project here -->
![App Demo](images/demo.png)

## ✨ Key Features
* 🔍 **Personalized Recommendations:** Suggests books based on cosine similarity algorithms.
* 📊 **Data Processing:** Cleaned and preprocessed large book rating datasets.
* ⚡ **Interactive UI:** Built with Streamlit / Flask for seamless user interaction.

## 🛠️ Technologies Used

### **Programming Language**
* ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) **Python 3**

### **GUI Framework**
* **Tkinter** – Built-in Python library used for creating the graphical user interface, event handling, dynamic menus, and layout management.

### **Libraries & Dependencies**
* **[Requests](https://pypi.org/project/requests/)** – Handles asynchronous HTTP requests to fetch JSON data and image assets from external APIs.
* **[Pillow (PIL)](https://pypi.org/project/Pillow/)** – Handles image processing, dynamic resizing, and formatting cover art for Tkinter display (`Image`, `ImageTk`).
* **`urllib.parse`** – Sanitizes and URL-encodes user input for safe web API querying.
* **`io.BytesIO`** – Reads raw binary image data directly from HTTP responses into memory without saving temporary files to disk.

### **External APIs & Services**
* **[Open Library Search API](https://openlibrary.org/developers/api)** – Fetches book metadata including titles, publication years, ratings, and cover IDs.
* **[Open Library Covers API](https://openlibrary.org/dev/docs/api/covers)** – Retrieves book cover images dynamically.

## 🚀 Quick Start
```bash
# Clone repository
git clone [https://github.com/tanishkapednekar1102/Book-Recommendation-System.git](https://github.com/tanishkapednekar1102/Book-Recommendation-System.git)

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
