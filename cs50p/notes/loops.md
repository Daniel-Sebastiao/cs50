# 📘 CS50P Notes – Loops in Python

## 🧠 Topic: Repetition with Loops

This lesson introduces **loops**, which are used to **execute blocks of code repeatedly**.  
Python supports multiple ways to implement repetition, and this example demonstrates the use of both `while` and `for` loops.

---

## 🔁 Using `while` Loop

```python
iterator = 0
while iterator < 3:
    print("meow")
    iterator += 1
```
## Using For
__Att:__ For is usually used to loop over a list, which is a data type in Python.
```python
for i in range(3):
    print("meow")
```
When not using a variable, do the following...
```python
for _ in range(3):
    print("meow")
```
