# Text Transformation Tool

A Python utility that performs various text transformations including phone number redaction, date formatting, common typo corrections, and emoji replacements.

## Features

### 🔒 **Privacy Protection**
- Automatically redacts phone numbers in the format `XXX-XXX-XXX` with `[REDACTED]`
- Example: `123-456-789` → `[REDACTED]`

### 📅 **Date Formatting**
- Converts dates from `YYYY-MM-DD` format to readable text with proper ordinal suffixes
- Example: `2006-05-08` → `8th May 2006`
- Supports all date formats with proper day suffixes (1st, 2nd, 3rd, 4th, etc.)

### 🐍 **Python Branding**
- Replaces "Python" and "python" with snake emoji (🐍)

### ✏️ **Typo Correction**
- `teh` → `the`
- `youre` → `you're`
- `taht` → `that`
- `adn` → `and`
- `dont` → `don't`

## Usage

### Interactive Mode
```bash
python task1.py
```
The program will prompt you to enter text and then display the transformed version.

### Example Input

```
my name is Palak. I was born on 2006-05-08. my phone number is 123-456-789 and i like python more than java
```

### Example Output
```
my name is Palak. I was born on 8th May 2006. my phone number is [REDACTED] and i like 🐍 more than java
```

## Requirements

- Python 3.x
- No external dependencies (uses only built-in modules)

## Installation

1. Clone or download the project files
2. Ensure Python is installed on your system
3. Run the script: `python task1.py`

## Code Structure

- **`convert_date(match)`**: Converts date strings to readable format with ordinal suffixes
- **`transform_text(input_text)`**: Main function that applies all transformations
- **Date parsing**: Handles year-month-day format and converts to day-month-year display
- **Month mapping**: Maps numeric months to full month names

## Customization

You can easily add more transformations by:
1. Adding new `.replace()` calls for simple text substitutions
2. Adding new `re.sub()` calls for pattern-based replacements
3. Creating new helper functions for complex transformations


