import re
from collections import Counter

class ReviewAnalyzer():
    def __init__(self):

        self.positive_words = ['excellent', 'amazing', 'great', 'good', 'love', 'perfect', 'awesome',
            'fantastic', 'wonderful', 'outstanding', 'impressed', 'satisfied',
            'recommend', 'happy', 'pleased', 'quality', 'fast', 'helpful']

        self.negative_words = ['terrible', 'awful', 'bad', 'hate', 'horrible', 'worst', 'disappointed',
            'frustrated', 'annoying', 'useless', 'broken', 'slow', 'expensive',
            'poor', 'waste', 'regret', 'problem', 'issue', 'complain']

        self.aspect_keywords = {
            'price': ['price', 'cost', 'expensive', 'cheap', 'affordable', 'value', 'money'],
            'quality': ['quality', 'durable', 'sturdy', 'flimsy', 'build', 'material'],
            'service': ['service', 'staff', 'employee', 'support', 'help', 'customer'],
            'delivery': ['delivery', 'shipping', 'fast', 'slow', 'arrived', 'package'],
            'design': ['design', 'look', 'appearance', 'color', 'style', 'beautiful', 'ugly']}

    def clean_review(self,text):
        text = re.sub(r'\s+',' ',text.strip())
        return text

    def calculate_sentiment(self,text):
        text_lower = text.lower()

        positive_count = 0
        for word in self.positive_words:
            if word in text_lower:
                positive_count = positive_count+1

        negative_count = 0
        for word in self.negative_words:
            if word in text_lower:
                negative_count = negative_count+1

        total_sentiment_words = positive_count+negative_count

        if total_sentiment_words == 0:
            sentiment_score = 0
        else:
            sentiment_score = (positive_count-negative_count)/total_sentiment_words

        if sentiment_score>0.2:
            sentiment = "Positive"
        elif sentiment_score<-0.2:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return {
            'score' : round(sentiment_score,2),
            'classification' : sentiment,
            'positive_word_count' : positive_count,
            'negative_word_count' : negative_count
        }

    def extract_rating_info(self,text):
        
        # ratings like - 3 out of 5 
        star_patterns = re.findall(r'(\d+)\s*(?:out of|/)\s*(\d+)',text)
        # ratings like - 2 stars
        star_mentions = re.findall(r'(\d+)\s*stars?', text.lower())

        return {
            'numerical_ratings':star_patterns,
            'star_mentions':star_mentions
        }

    def complaints_or_praise(self , text):
        sentences = re.split(r'[.!?]+',text)

        positive_phrase = []
        negative_phrase = []

        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence)>10:
                sentence_lower = sentence.lower()

                positive = False
                for word in self.positive_words:
                    if word in sentence_lower:
                        positive = True

                if positive:
                    positive_phrase.append(sentence.capitalize())

                negative = False
                for word in self.negative_words:
                    if word in sentence_lower:
                        negative = True

                if negative:
                    negative_phrase.append(sentence.capitalize())

        return {
            'strong_praise':positive_phrase[0:2],
            'strong_complaints':negative_phrase[0:2]
        }

    def recommendations(self,text):
        text_lower = text.lower()

        recommended = [
            'recommend', 'would buy again', 'suggest', 'worth it',
            'go for it', 'try this', 'must buy'
        ]
        not_recommended = [
            'don\'t recommend', 'avoid', 'stay away', 'waste of money',
            'don\'t buy', 'not worth', 'skip this'
        ]

        recommendations = []
        for pattern in recommended:
            if pattern in text_lower:
                recommendations.append(pattern)

        warning = []
        for pattern in not_recommended:
            if pattern in text_lower:
                warning.append(pattern)

        return {
            'recommends':len(recommendations),
            'warnings':len(warning),
            'recommendations':recommendations,
            'warning_phrases':warning
        }

    def meaningful_words(self,text):
        stopwords = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'this', 'that', 'it',
            'have', 'has', 'had', 'will', 'would', 'could', 'i', 'my', 'me'
        }

        word_list = text.split()

        meaningful_words = []

        for word in word_list:
            is_long_enough = len(word)>=3
            contains_only_letters = word.isalpha()


            if is_long_enough and contains_only_letters:
                if word not in stopwords:
                    meaningful_words.append(word)

        words_count = Counter(meaningful_words)

        return words_count.most_common(10)

    def analyze_review(self,text):
        cleaned_text = self.clean_review(text)

        sentiment = self.calculate_sentiment(cleaned_text)
        rating = self.extract_rating_info(cleaned_text)
        complaints_or_praise = self.complaints_or_praise(cleaned_text)
        recommendations = self.recommendations(cleaned_text)
        word_frequency = self.meaningful_words(cleaned_text)

        return {
            'review_length':len(cleaned_text),
            'sentiment_analysis':sentiment,
            'rating_info':rating,
            'complaints_or_praise':complaints_or_praise,
            'recommendations':recommendations,
            'top_words':word_frequency[:6],
            'strong_praise':complaints_or_praise['strong_praise'],
            'strong_complaints':complaints_or_praise['strong_complaints']
        }

    def print_analysis(self,analysis):
        print("=" * 60)
        print("CUSTOMER REVIEW ANALYSIS")
        print("=" * 60)

        print(f"\n📊 OVERVIEW:")
        print(f"REVIEW LENGTH: {analysis['review_length']} characters")

        sentiment = analysis['sentiment_analysis']
        print(f"\n😊 SENTIMENT ANALYSIS:")
        print(f"OVERALL SENTIMENT: {sentiment['classification']}")
        print(f"SENTIMENT SCORE: {sentiment['score']} (range: -1 to 1)")
        print(f"POSITIVE WORDS FOUND: {sentiment['positive_word_count']}")
        print(f"NEGATIVE WORDS FOUND: {sentiment['negative_word_count']}")

        rating = analysis['rating_info']
        print(f"\n👌 RATING INFORMATION:")
        if rating['numerical_ratings']:
            for rating_pair in rating['numerical_ratings']:
                print(f"RATING: {rating_pair[0]} out of {rating_pair[1]}")
        if rating['star_mentions']:
            print(f'STAR RATINGS MENTIONED: {', '.join(rating['star_mentions'])}')
        if not rating['numerical_ratings'] and not rating['star_mentions']:
            print("NO NUMERICAL RATINGS FOUND")

        feedback = analysis['complaints_or_praise']
        print(f"\n💕 SPECIFIC FEEDBACK:")
        if feedback['strong_praise']:
            print(f"STRONG PRAISE: {', '.join(feedback['strong_praise'])}")
        if feedback['strong_complaints']:
            print(f"STRONG COMPLAINTS: {', '.join(feedback['strong_complaints'])}")

        rec = analysis['recommendations']
        print(f"\n👍 RECOMMENDATION STATUS:")
        if rec['recommends']:
            print(f"REVIEW RECOMMENDS THE PRODUCT")
            if rec['recommendations']:
                print(f"PHRASES: {', '.join(rec['recommendations'])}")
            elif rec['warnings']:
                print(f"REVIEW WARNS AGAINST THE PRODUCT")
                if rec['warning_phrases']:
                    print(f"PHRASES: {', '.join(rec['warning_phrases'])}")
        else:
            print(f"NO CLEAR RECOMMENDATIONS EITHER WAY")

        print(f"\n MOST MENTIONED WORDS:")
        for word , count in analysis['top_words']:
            print(f"\n {word}: {count} times")

        print(f"\n STRONG PRAISE:")
        if analysis['strong_praise']:
            print(f"STRONG PRAISE: {', '.join(analysis['strong_praise'])}")
        
        print(f"\n STRONG COMPLAINTS:")
        if analysis['strong_complaints']:
            print(f"STRONG COMPLAINTS: {', '.join(analysis['strong_complaints'])}")

def main():
    analyzer = ReviewAnalyzer()
    sample_reviews = [
        """
    I absolutely love this laptop! The design is sleek and modern, and the performance 
    is outstanding. I've been using it for 3 months now and it handles everything I throw 
    at it. The battery life is amazing - easily 8-10 hours of use. The price was a bit 
    high at $1200, but honestly, it's worth every penny. The customer service was also 
    excellent when I had a question about setup. I would definitely recommend this to 
    anyone looking for a reliable laptop. 5 out of 5 stars!
    """,
    
    """
    This restaurant was a huge disappointment. We waited 45 minutes for our food, and 
    when it finally arrived, it was cold and tasteless. The service was terrible - our 
    waiter was rude and seemed annoyed by our questions. The prices are way too expensive 
    for what you get. My pasta was overcooked and the sauce was bland. I definitely won't 
    be coming back here, and I don't recommend this place to anyone. Save your money and 
    go somewhere else. 2 out of 5 stars at best.
    """,
    
    """
    Pretty decent phone overall. The camera quality is good for the price range, and 
    the interface is user-friendly. Battery life could be better - only lasts about 
    6 hours with heavy use. The build quality feels solid, though the plastic back 
    shows fingerprints easily. Customer support was helpful when I had issues with 
    the initial setup. For $400, it's a reasonable choice, but there might be better 
    options available.
    """
    ]

    print("CUSTOMER REVIEW ANALYSIS")
    print("=" * 60)
    print("This program analyzes customer reviews and extracts:")
    print("• Sentiment (positive, negative, neutral)")
    print("• Numerical ratings and data")
    print("• Specific praise or complaints")
    print("• Recommendation status")
    print("• Most frequently mentioned words")


    for i, review in enumerate(sample_reviews, 1):
        print(f"\n\n🔍 ANALYZING SAMPLE REVIEW #{i}")
        analysis = analyzer.analyze_review(review)
        analyzer.print_analysis(analysis)

    print("\n\n" + "=" * 60)
    
    print("\n🎉 Analysis complete! This could help businesses understand customer feedback!")


if __name__ == "__main__":
    main()