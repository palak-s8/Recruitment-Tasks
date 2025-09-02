# Customer Review Analyzer

A Python-based sentiment analysis tool that analyzes customer reviews to extract meaningful insights about products, services, or experiences.

## Features

- **Sentiment Analysis**: Determines if a review is positive, negative, or neutral
- **Rating Extraction**: Finds numerical ratings and star mentions in reviews
- **Feedback Analysis**: Identifies specific praise and complaints
- **Recommendation Detection**: Determines if the reviewer recommends or warns against the product/service
- **Word Frequency Analysis**: Shows the most frequently mentioned meaningful words
- **Comprehensive Reporting**: Provides detailed analysis with emojis and clear formatting

## Installation

No additional dependencies required! This tool uses only Python standard library modules:

- `re` (regular expressions)
- `collections.Counter` (word counting)

## Usage

### Basic Usage

```python
from task22 import ReviewAnalyzer

# Create an analyzer instance
analyzer = ReviewAnalyzer()

# Analyze a review
review_text = "I love this product! It's amazing and works perfectly."
analysis = analyzer.analyze_review(review_text)

# Print the analysis
analyzer.print_analysis(analysis)
```

### Running the Demo

```bash
python task22.py
```

This will run the built-in demo with three sample reviews showing different sentiment types.

## Class Methods

### `ReviewAnalyzer()`

Main class for analyzing customer reviews.

#### Methods:

- **`clean_review(text)`**: Cleans and normalizes review text
- **`calculate_sentiment(text)`**: Calculates sentiment score and classification
- **`extract_rating_info(text)`**: Extracts numerical ratings and star mentions
- **`complaints_or_praise(text)`**: Identifies specific positive and negative feedback
- **`recommendations(text)`**: Detects recommendation patterns
- **`meaningful_words(text)`**: Finds most frequent meaningful words
- **`analyze_review(text)`**: Comprehensive analysis combining all methods
- **`print_analysis(analysis)`**: Pretty-prints analysis results

## Analysis Output

The analyzer provides:

### 📊 Overview
- Review length in characters

### 😊 Sentiment Analysis
- Overall sentiment (Positive/Negative/Neutral)
- Sentiment score (-1 to 1)
- Count of positive and negative words found

### 👌 Rating Information
- Numerical ratings (e.g., "4 out of 5")
- Star mentions (e.g., "5 stars")

### 💕 Specific Feedback
- Strong praise sentences
- Strong complaint sentences

### 👍 Recommendation Status
- Whether the review recommends or warns against the product
- Specific recommendation phrases found

### 📝 Word Analysis
- Top 6 most frequently mentioned meaningful words
- Word frequency counts

## Sentiment Classification

The tool uses a predefined dictionary of positive and negative words to calculate sentiment:

- **Positive words**: excellent, amazing, great, good, love, perfect, awesome, etc.
- **Negative words**: terrible, awful, bad, hate, horrible, worst, disappointed, etc.

Sentiment is classified as:
- **Positive**: Score > 0.2
- **Negative**: Score < -0.2
- **Neutral**: Score between -0.2 and 0.2

## Example Output

```
============================================================
CUSTOMER REVIEW ANALYSIS
============================================================

📊 OVERVIEW:
REVIEW LENGTH: 245 characters

😊 SENTIMENT ANALYSIS:
OVERALL SENTIMENT: Positive
SENTIMENT SCORE: 0.67 (range: -1 to 1)
POSITIVE WORDS FOUND: 4
NEGATIVE WORDS FOUND: 0

👌 RATING INFORMATION:
RATING: 5 out of 5

💕 SPECIFIC FEEDBACK:
STRONG PRAISE: I absolutely love this laptop!, The design is sleek and modern

👍 RECOMMENDATION STATUS:
REVIEW RECOMMENDS THE PRODUCT
PHRASES: recommend

📝 MOST MENTIONED WORDS:
laptop: 2 times
design: 1 times
performance: 1 times
```

## Use Cases

- **E-commerce**: Analyze product reviews to understand customer satisfaction
- **Restaurant Reviews**: Extract feedback about food, service, and experience
- **Customer Service**: Monitor and analyze customer feedback
- **Market Research**: Understand customer opinions and preferences
- **Quality Assurance**: Identify common issues and positive aspects

## Customization

You can easily customize the analyzer by modifying:

- **Positive/Negative word lists** in the `__init__` method
- **Aspect keywords** for different product categories
- **Recommendation patterns** in the `recommendations` method
- **Stopwords** in the `meaningful_words` method

## Limitations

- Uses simple word-based sentiment analysis (not machine learning)
- May not capture context or sarcasm
- Limited to English language
- Predefined word lists may not cover all domains

## Future Enhancements

- Machine learning-based sentiment analysis
- Multi-language support
- Aspect-based sentiment analysis
- Integration with review platforms
- Export to JSON/CSV formats
