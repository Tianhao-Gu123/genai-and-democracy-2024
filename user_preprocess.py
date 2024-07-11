import os
import warnings
print("🔧 Setting up environment for uese_preprocess...")
# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # This must be set before TensorFlow is imported
# Suppress FutureWarnings
warnings.filterwarnings('ignore', category=FutureWarning)

import json
from glob import glob
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
print("📚 Transformers libraries imported successfully.")

# Function to translate German to English
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from nltk.tokenize import sent_tokenize

def translate_de_to_en(text):
    print("🇩🇪 Translating from German to English...")
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("google/bert2bert_L-24_wmt_de_en", pad_token="<pad>", eos_token="</s>", bos_token="<s>")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/bert2bert_L-24_wmt_de_en")

    # Split the text into sentences to ensure each block is within the size limit
    sentences = sent_tokenize(text, language='german')
    translated_text = ""

    for sentence in sentences:
        # Tokenize sentence to check if it needs further splitting
        input_ids = tokenizer(sentence, return_tensors="pt", add_special_tokens=True).input_ids
        # If the sentence is too long, further splitting logic should be implemented here
        if len(input_ids[0]) > 512:
            print("⚠️ This sentence too long, further splitting required.")
            # Implement further splitting if necessary
            pass
        else:
            # Translate the sentence/block
            print(f"Translating: {sentence}")
            output_ids = model.generate(input_ids)[0]
            translated_sentence = tokenizer.decode(output_ids, skip_special_tokens=True)
            translated_text += translated_sentence + " "

    return translated_text.strip()

# Function to translate French to English
from transformers import pipeline
from nltk.tokenize import sent_tokenize

def translate_fr_to_en(text):
    print("🇫🇷 Translating from French to English...")
    # Initialize the translation pipeline
    pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-fr-en")
    
    # Split the text into sentences
    sentences = sent_tokenize(text, language='french')
    translated_text = ""
    
    for sentence in sentences:
        # Translate each sentence and concatenate
        print(f"Translating: {sentence}")
        result = pipe(sentence)
        translated_text += result[0]['translation_text'] + " "
    
    return translated_text.strip()

# Function to handle each input file
def handle_input_file(file_location, output_path):
    print(f"📄 Processing file: {os.path.basename(file_location)}")
    with open(file_location, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translated_content = []
    for paragraph in data['content']:
        if data['language'] == 'de':
            translated_paragraph = translate_de_to_en(paragraph)  
        elif data['language'] == 'fr':
            translated_paragraph = translate_fr_to_en(paragraph)
        else:
            translated_paragraph = paragraph
        translated_content.append(translated_paragraph)

    transformed_data = {
        "text_id": data['text_id'],
        "content": translated_content,
        "url": data['url']  # Assuming article_url contains the URL string

    }
    
    filename = os.path.basename(file_location)
    output_file_path = os.path.join(output_path, filename)
    with open(output_file_path, "w", encoding='utf-8') as f:
        json.dump(transformed_data, f, ensure_ascii=False, indent=4)
    print(f"✅ File processed and saved: {filename}")

# Main function to process all files in a directory
def process_files():
    print("🚀 Starting file processing...")
    input_dir = "./Cache/search_result"
    output_dir = "./Cache/preprocessed_search_result"
    input_files = glob(os.path.join(input_dir, '*.json'))
    for file_location in input_files:
        handle_input_file(file_location, output_dir)
    print("🎉 All files processed successfully.")

if __name__ == "__main__":
    # Ensure output directory exists
    os.makedirs("./Cache/preprocessed_search_result", exist_ok=True)
    print("📁 Output directory ready.")
    process_files()