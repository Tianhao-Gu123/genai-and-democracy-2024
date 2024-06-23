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

# Initialize the model
model = SentenceTransformer("sentence-transformers/msmarco-distilbert-base-tas-b")
print("🧠 Model loaded successfully.")

# Load the JSON files from the specified directory
def load_and_process_json_files(directory_path):
    print("📂 Loading and processing JSON files...")
    docs = []
    text_ids = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = join(directory_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                for content in data['content']:
                    docs.append(content)
                    text_ids.append(data['text_id'])  # Store the text_id alongside the content
    print("✅ JSON files processed.")
    return docs, text_ids

# Implement the inference logic here
def handle_user_query(query, query_de):
    print("🔍 Handling user query...")
    # TODO by Ayoub: use some API to get some results for the query and store them in the search_result directory in JSON format
    # TODO: Call user_preprocessing.py to preprocess the search results
    process_files()
    docs, text_ids = load_and_process_json_files("./Cache/preprocessed_search_result")
    query_emb = model.encode(query)
    doc_emb = model.encode(docs)
    scores = util.dot_score(query_emb, doc_emb)[0].cpu().tolist()
    doc_info = list(zip(docs, scores, text_ids))
    sorted_doc_info = sorted(doc_info, key=lambda x: x[1], reverse=True)
    top_results = sorted_doc_info[:3]
    print(f"🎉 Great! We have found some results for you! And the higher the score, the more relevant the text is.")
    for doc, score, text_id in top_results:
        print(f"📄 Score: {score}, Doc: {doc}")
    # TODO: Store the results in a JSON file in the res_history directory
    # TODO: Clear the search_result directory after the query is processed
    # TODO: Add source for the results, for example, Wikipedia, StackOverflow, etc.

parser = argparse.ArgumentParser(description='Run the inference.')
parser.add_argument('--query', type=str, help='The user query.', required=True, action="append")
parser.add_argument('--query_de', type=str, help='query_de', required=True, action="append")

if __name__ == "__main__":
    args = parser.parse_args()
    query = args.query
    query_de = args.query_de
    handle_user_query(query, query_de)