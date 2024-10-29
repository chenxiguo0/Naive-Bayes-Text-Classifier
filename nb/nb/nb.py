import numpy as np

class NaiveBayes:
    def __init__(self, alpha=0.1):
        self.alpha = alpha
        self.vocabulary = {}
        self.priors = None
        self.likelihoods = None

    def train(self, df):
        v = set()
        for text in df["text"]:
            v.update(text.split())
        self.vocabulary = {t: idx for idx, t in enumerate(v)}
        n_docs = df.shape[0]
        n_classes = df['author'].nunique()
        self.priors = df['author'].value_counts(normalize=True).values

        training_matrix = np.zeros((n_docs, len(self.vocabulary)))
        for i, text in enumerate(df["text"]):
            for word in text.split():
                if word in self.vocabulary:
                    training_matrix[i, self.vocabulary[word]] += 1

        word_counts_per_class = {author: np.zeros(len(self.vocabulary)) for author in df['author'].unique()}
        for i, row in df.iterrows():
            author = row["author"]
            word_counts_per_class[author] += training_matrix[i]

        self.likelihoods = np.zeros((n_classes, len(self.vocabulary)))

        for i, author in enumerate(word_counts_per_class):
            total_count = word_counts_per_class[author].sum()
            #for j in range(len(self.vocabulary)):
                #self.likelihoods[i, j] = (word_counts_per_class[author][j] + self.alpha) / (total_count + self.alpha * len(self.vocabulary))
            for j, word in enumerate(self.vocabulary):
                word_count = word_counts_per_class[author][j]  # Get the count for the specific word in this class
                self.likelihoods[i, j] = (word_count + self.alpha) / (total_count + self.alpha * len(self.vocabulary))

    def test(self, df):
        class_predictions = []
        for text in df["text"]:
            test_vector = np.zeros(len(self.vocabulary))
            for word in text.split():
                if word in self.vocabulary:
                    test_vector[self.vocabulary[word]] += 1
            preds = np.log(self.priors) + np.dot(np.log(self.likelihoods), test_vector)
            yhat = np.argmax(preds)
            class_predictions.append(yhat)
        return class_predictions

