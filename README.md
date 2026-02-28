# Resume Analyzer (TF‑IDF & Cosine Similarity)

This project demonstrates a **basic resume–job description matching system** using **Natural Language Processing (NLP)** techniques in Python. It compares multiple resumes against a job description and ranks them based on textual similarity.

---

## 📌 Objective

To identify resumes that best match a given job description by:

* Converting text into numerical vectors using **TF‑IDF**
* Measuring similarity using **Cosine Similarity**
* Filtering resumes based on a similarity threshold

---

## 🧠 How It Works

1. **Input Data**

   * A list of resumes (text)
   * A single job description

2. **Text Vectorization**

   * Uses `TfidfVectorizer` with English stopwords removed
   * Converts text into TF‑IDF feature vectors

3. **Similarity Calculation**

   * Compares the job description with each resume
   * Uses cosine similarity to compute matching scores

4. **Filtering**

   * Resumes scoring above a defined threshold are selected

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn

  * TF‑IDF Vectorizer
  * Cosine Similarity

---

## 📂 Project Structure

```
resume_analyzer/
│
├── resume_analyzer.py
├── README.md
├── .gitignore
```

---

## ▶️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/your-username/resume_analyzer.git
cd resume_analyzer
```

2. **Install dependencies**

```bash
pip install pandas scikit-learn
```

3. **Run the script**

```bash
python resume_analyzer.py
```

---

## 📊 Sample Output

```
Resume ID | Similarity Score
----------------------------
1         | 0.72
2         | 0.05
3         | 0.41
```

Only resumes with a similarity score **≥ 0.2** are considered a match.

---

## ⚙️ Customization

* Replace sample resumes with real resume text
* Modify the job description
* Adjust the similarity threshold
* Extend for PDF/DOCX resume parsing

---


## 📜 License

This project is for educational purposes and open for enhancement.


