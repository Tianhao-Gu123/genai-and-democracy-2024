from gnews import GNews
from newspaper import Article
import json
import os
from datetime import datetime

def retrieve_data(query):

    # Initialize GNews object
    google_news = GNews()

    # Define languages and their corresponding codes
    languages = {
        'English': 'en',
        'German': 'de',
        'French': 'fr'
    }

    # Define the maximum number of articles to fetch per language
    max_articles = 1

    # Clean the search_result directory
    output_dir = './Cache/search_result'
    os.makedirs(output_dir, exist_ok=True)

    # Loop through each language and fetch news articles
    for lang, lang_code in languages.items():
        print(f"Fetching articles in {lang} ({lang_code})\n")
        
        # Perform the search
        google_news.language = lang_code
        try:
            articles = google_news.get_news(query)
        except Exception as e:
            print(f"Failed to fetch articles for {lang} ({lang_code}). Error: {e}")
            continue
        
        # Process each article
        for idx, article in enumerate(articles[:max_articles]):  # Limit to max_articles
            # Extract article URL
            url = article['url']
            
            try:
                # Fetch full article content using newspaper3k
                newspaper_article = Article(url, language=lang_code)
                newspaper_article.download()
                newspaper_article.parse()
                
                # Extract the publication date and source URL
                timestamp = newspaper_article.publish_date
                if timestamp is None:
                    timestamp = datetime.now()  # Fallback to current date if no publish date is available
                timestamp_str = timestamp.strftime('%Y-%m-%d %H:MM:SS')  # Format as "YYYY-MM-DD HH:MM:SS"
        
                # Prepare the data
                article_data = {
                    "language": lang_code,
                    "text_id": str(idx),
                    "content": [newspaper_article.text],
                }
                
                # Define the file path for the JSON file
                file_name = f"{lang_code}_{idx}.json"  # e.g., "fr_0.json"
                file_path = os.path.join(output_dir, file_name)
                
                # Save the article data to a JSON file
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(article_data, f, ensure_ascii=False, indent=4)
                
                # Print the formatted article data
                print(f"Article saved as {file_name}")
                print(article_data)
                print("\n")
            
            except Exception as e:
                print(f"Failed to process article at {url}. Error: {e}")
                continue