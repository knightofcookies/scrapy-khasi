import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Read sentences from files
with open('training_data/valid_text.txt', 'r', encoding="utf-8") as valid_file:
    valid_sentences = valid_file.read().splitlines()

with open('training_data/invalid_text.txt', 'r', encoding="utf-8") as invalid_file:
    invalid_sentences = invalid_file.read().splitlines()

# Create DataFrame
valid_df = pd.DataFrame({'sentence': valid_sentences, 'label': 1})
invalid_df = pd.DataFrame({'sentence': invalid_sentences, 'label': 0})

# Combine valid and invalid dataframes
df = pd.concat([valid_df, invalid_df], ignore_index=True)

# Print a sample of the combined DataFrame
print(df.head())

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df['sentence'], df['label'], test_size=0.2, random_state=42
)

# Create a bag-of-words representation
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Predictions
y_pred = model.predict(X_test_vec)

# Evaluate the model
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred))
