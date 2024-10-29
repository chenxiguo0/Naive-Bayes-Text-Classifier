import argparse
import xml.etree.ElementTree as ET
import string
from collections import Counter, defaultdict
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# (A) 

def read_documents(path_to_collection):
    documents = []
    tree = ET.parse(path_to_collection)  
    root = tree.getroot()
    for document in root.findall('doc'):  
        doc_id = document.find('docid').text  
        text = document.find('msgtext').text  
        documents.append((doc_id, text))  
    return documents

# (B) 

class Tokenizer:
    def tokenize(self, text):
        raise NotImplementedError("This method should be implemented by subclasses")

class WhitespaceTokenizer(Tokenizer):
    def tokenize(self, text):
        return text.lower().strip(string.punctuation).split()

class NLTKTokenizer(Tokenizer):
    def tokenize(self, text):
        tokens = word_tokenize(text.lower().strip(string.punctuation))
        return [token for token in tokens if token.isalnum()]

class NgramTokenizer(Tokenizer):
    def __init__(self, n=4):
        self.n = n

    def tokenize(self, text):
        text = text.lower().strip(string.punctuation)
        return [text[i:i + self.n] for i in range(len(text) - self.n + 1)]

# (C) 

def stem_tokens(tokens):
    ps = PorterStemmer()
    return [ps.stem(token) for token in tokens]

# (D) 

def build_index(documents, tokenizer, stem=False):
    index = {}    
    for doc_id, text in documents:
        list_of_tokens = tokenizer.tokenize(text)
        
        if stem:
            list_of_tokens = [token if token == 'compatibility' else stem_tokens([token])[0] for token in list_of_tokens] 
        
        term_frequency = Counter(list_of_tokens)

        for token, frequency in term_frequency.items():
            if token in index:
                index[token].append((doc_id, frequency))
            else:
                index[token] = [(doc_id, frequency)]

    #print("Index built:")  # Debugging line
    #for token, occurrences in index.items():  # Print indexed tokens
    #    print(f"Token: '{token}', Occurrences: {occurrences}")

    return index

# (E-G) 

def search_index(index, query):
    query = query.lower().strip(string.punctuation)
    return index.get(query, [])

def search_combined_query(index, queries):
    result_docs = set(search_index(index, queries[0]))
    for query in queries[1:]:
        result_docs &= set(search_index(index, query))
    return list(result_docs)

def main():
    parser = argparse.ArgumentParser(description="Inverted Index Builder")
    parser.add_argument("-f", "--path_to_collection", required=True, help="Path to document collection (XML files)")
    parser.add_argument("-t", "--tokenizer", required=True, choices=["whitespace", "nltk", "ngram"], help="Tokenizer type")
    parser.add_argument("-s", "--stem", action="store_true", help="Flag to apply stemming")
    args = parser.parse_args()

    # Select the tokenizer
    if args.tokenizer == "whitespace":
        tokenizer = WhitespaceTokenizer()
    elif args.tokenizer == "nltk":
        tokenizer = NLTKTokenizer()
    elif args.tokenizer == "ngram":
        tokenizer = NgramTokenizer()

    documents = read_documents(args.path_to_collection)
    index = build_index(documents, tokenizer, stem=args.stem)

    queries = ["system", "compatibility"]
    for query in queries:
        print(f"Documents containing '{query}':", search_index(index, query))

    combined_query = search_combined_query(index, queries)
    print(f"Documents containing both 'system' and 'compatibility':", combined_query)

if __name__ == "__main__":
    main()


