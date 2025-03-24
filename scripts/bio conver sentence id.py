import pandas as pd
import os
import re

# ✅ Load the extracted SDOH dataset
csv_path = r"C:\Users\subha\OneDrive\Desktop\sdoh_aria_results.csv"
df = pd.read_csv(csv_path)

# ✅ Token Cleaning Function
def clean_token(token):
    """Removes unnecessary symbols and keeps only meaningful words."""
    return re.sub(r"[^a-zA-Z0-9,.!?-]", "", token)  # Keeps only letters, numbers, and punctuation

# ✅ Function to Convert Dataset into BIO Format with Correct Sentence_ID
def convert_to_bio_csv(df, output_csv_path):
    bio_data = []
    sentence_id = 0  # Start Sentence_ID from 0
    last_text = None  # Track last sentence to prevent incorrect ID increments

    for _, row in df.iterrows():
        text = str(row["Extracted_Text"]).strip()  # Ensure text is a string
        category = str(row["SDOH_Category"]).strip()

        if pd.isna(text) or pd.isna(category) or text == "":
            continue  # Skip empty text

        # ✅ Check if this is a new sentence (different from last sentence)
        if text != last_text:
            sentence_id += 1  # Increment Sentence_ID only when text changes
            last_text = text

        tokens = text.split()  # Simple whitespace-based tokenization
        tokens = [clean_token(token) for token in tokens if token.strip()]  # Clean tokens

        if len(tokens) == 0:
            continue  # Skip if no valid tokens remain

        bio_tags = ["O"] * len(tokens)  # Default to "O" (Outside) tags

        # ✅ Assign BIO tags properly
        bio_tags[0] = f"B-{category}"  # First token gets "B-Category"
        for i in range(1, len(tokens)):
            bio_tags[i] = f"I-{category}"  # Remaining tokens get "I-Category"

        # ✅ Store each token, corresponding BIO tag, and Sentence_ID
        for token, tag in zip(tokens, bio_tags):
            bio_data.append([sentence_id, token, tag])

    # ✅ Convert to DataFrame
    bio_df = pd.DataFrame(bio_data, columns=["Sentence_ID", "Token", "BIO_Tag"])

    # ✅ Save as CSV
    bio_df.to_csv(output_csv_path, index=False, encoding="utf-8")

# ✅ Define output CSV path
output_folder = r"C:\Users\subha\OneDrive\Desktop"
bio_csv_path = os.path.join(output_folder, "sdoh_bio_dataset_corrected.csv")

# ✅ Convert dataset to BIO format and save as CSV
convert_to_bio_csv(df, bio_csv_path)

print(f"✅ BIO dataset saved as CSV at: {bio_csv_path}")

# ✅ Load and Verify Dataset
df_bio = pd.read_csv(bio_csv_path)
print(df_bio.head())  # Display first few rows to verify correctness

# ✅ Quick Check: Ensure Correct Label Distribution
print("\n🔍 BIO Label Distribution:")
print(df_bio["BIO_Tag"].value_counts())
