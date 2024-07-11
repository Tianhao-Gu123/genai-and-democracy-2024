import os
import warnings

print("B🅱️e🇪s🇸t🇹 Seminar ever 🎉📚🎓🌟😊👍🔥💡🚀")
print("--------------------")
print("🔧 Setting up environment of user_inference...")
# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # This will hide the TensorFlow info and warning messages
warnings.filterwarnings('ignore', category=FutureWarning)  # This will ignore FutureWarnings
# Suppress specific warning from Hugging Face's transformers
def warn(*args, **kwargs):
    pass
warnings.warn = warn

import argparse
import json
from os.path import join
from sentence_transformers import SentenceTransformer, util
from user_preprocess import process_files
from retrieve_data import retrieve_data
import requests
import time


# Initialize the model
model = SentenceTransformer("sentence-transformers/msmarco-distilbert-base-tas-b")
print("🧠 Model loaded successfully.")

def load_and_process_json_files(directory_path):
    print("📂 Loading and processing JSON files...")
    docs = []
    text_ids = []
    urls = []  # Initialize a list to store URLs
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)  # Ensure os.path.join is used for file path
            with open(file_path, 'r') as file:
                data = json.load(file)
                for content in data['content']:
                    docs.append(content)
                    text_ids.append(data['text_id'])  # Store the text_id alongside the content
                    urls.append(data['url'])  # Assuming each JSON file contains a 'url' key
    print("✅ JSON files processed.")
    return docs, text_ids, urls  # Return the urls list along with docs and text_ids

def query_bias_detection(input_text, max_retries=5, wait_time=20):
    API_URL = "https://api-inference.huggingface.co/models/d4data/bias-detection-model"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    retries = 0
    while retries < max_retries:
        output = query({"inputs": input_text})
        # Check if the response contains an error indicating the model is loading
        if isinstance(output, dict) and output.get('error') == 'Model d4data/bias-detection-model is currently loading':
            print(f"Model is loading, retrying in {wait_time} seconds...")
            time.sleep(wait_time)  # Wait before retrying
            retries += 1
            continue
        return output  # Return the output if no loading error or other errors
    return {"error": "Max retries reached, could not process the input."}

def get_top_three_non_biased_docs(top_results):
    non_biased_scores = []
    for doc, sc, id, url in top_results:
        bias_detection_result = query_bias_detection(doc)
        if isinstance(bias_detection_result, dict) and 'error' in bias_detection_result:
            print("An error occurred while evaluating the bias.")
            print(bias_detection_result)
            continue
        elif not isinstance(bias_detection_result, list):
            continue
        else:
            first_result_list = bias_detection_result[0]
            non_biased_score = next((item for item in first_result_list if item['label'] == 'Non-biased'), None)['score']
            non_biased_scores.append((doc, non_biased_score, id, url))  # Include id and url in the tuple
    
    non_biased_scores.sort(key=lambda x: x[1], reverse=True)
    top_three_non_biased_docs = non_biased_scores[:3]
    
    for doc, score, id, url in top_three_non_biased_docs:  # Unpack id and url along with doc and score
        print(f"Document: {doc}\nNon-biased Score: {score}\nFor the full text, visit: {url}\n")

# Implement the inference logic here
def handle_user_query(query):
    print("🔍 Handling user query...")
    #transform the query to a string
    query = " ".join(query)
    retrieve_data(query)
    #call user_preprocessing.py to preprocess the search results
    process_files()

    docs, text_ids, urls = load_and_process_json_files("./Cache/preprocessed_search_result")
    query_emb = model.encode(query)
    doc_emb = model.encode(docs)
    scores = util.dot_score(query_emb, doc_emb)[0].cpu().tolist()
    doc_info = list(zip(docs, scores, text_ids, urls))
    sorted_doc_info = sorted(doc_info, key=lambda x: x[1], reverse=True)
    top_results = sorted_doc_info[:4]
    print(f"🎉 Great! We have found the best result for you!")
    get_top_three_non_biased_docs(top_results)

    #print(f"🎉 Great! We have found the best result for you!")
    #print(f"Most non-biased document: {most_non_biased_doc}")

    
parser = argparse.ArgumentParser(description='Run the inference.')
parser.add_argument('--query', type=str, help='The user query.', required=True, action="append")

if __name__ == "__main__":
    args = parser.parse_args()
    query = args.query
    handle_user_query(query)