# Task 1: Mischievous Text Transformer (Basic Python)

Imagine you are building a playful text-transformer. Given an input paragraph, your function should apply creative transformation rules, such as:

- **Redacting information** (e.g., replacing all phone numbers with `[REDACTED]`).  
- **Stylizing text** (e.g., converting all dates into words: `2025-08-23 → 23rd August 2025`).  
- **Inserting Easter eggs** (e.g., every time the word `"Python"` appears, change it to 🐍).  

---

### Your Task
Write a Python function:

```python
def transform_text(input_text: str) -> str:
    # apply transformations
    return transformed_text
```
This function should apply at least 3 transformations of your choice.

For Example:

Input:
```bash
Call me at 98123-45678 on 2025-08-23.  
I love Python more than Java.
```
Output:
```bash
Call me at [REDACTED] on 23rd August 2025.  
I love 🐍 more than Java.
```
Note:
There is no single solution to this.
What matters is your creativity and approach to solving the problem.
