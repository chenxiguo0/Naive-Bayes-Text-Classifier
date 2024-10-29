import argparse
import pandas as pd
from nb.nb import NaiveBayes  
from utils.load_data import build_dataframe

def main():
    # (a) Set up argparse to get the input directory from the user
    parser = argparse.ArgumentParser(description="Naive Bayes Classifier")
    parser.add_argument("-f", "--indir", required=True, help="Input directory for text data")
    args = parser.parse_args()
    print(f"Input directory: {args.indir}")

    # (b) Build the DataFrame from the text within the data subfolders
    training_df, test_df = build_dataframe(args.indir)
    print(f"Training DataFrame shape: {training_df.shape}")
    print(f"Test DataFrame shape: {test_df.shape}")

    # Create an instance of your NaiveBayes class
    nb = NaiveBayes(alpha=1.0)

    # (c) Train the Naive Bayes model to estimate priors and likelihoods
    nb.train(training_df)
    print("Trained Naive Bayes model.")
    print(f"Priors: {nb.priors}")
    print(f"Likelihoods: {nb.likelihoods}")
    
    # (d) Run the test method to get predictions
    predictions = nb.test(test_df)

    # (e) Print out the predictions
    for text, pred in zip(test_df["text"], predictions):
        print(f"Text: {text}\nPredicted Author ID: {pred}\n")

if __name__ == "__main__":
    main()