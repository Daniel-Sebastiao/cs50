# 📘 CS50P Notes – Grading Program

## 🧠 Exercise Summary

This program reads a numeric score from the user and prints a corresponding letter grade based on standard grading thresholds.

---

## 🧾 Code Analyzed

```python
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
