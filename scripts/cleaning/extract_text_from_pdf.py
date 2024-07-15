import re
import PyPDF2

def extract_sentences_from_pdf(pdf_path, txt_path):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)

            # Initialize an empty list to store sentences
            sentences = []

            # Iterate through each page
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()

                # Split text into sentences (assuming sentences end with '.', '!', or '?')
                sentence_list = re.split(r'[.!?]', text)
                sentences.extend(sentence_list)

        # Write sentences to a text file
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for sentence in sentences:
                sentence: str = sentence.strip()  # Remove leading/trailing spaces
                sentence = sentence.replace('\n', '')
                if sentence:
                    txt_file.write(sentence + '.\n')

        print(f"Sentences extracted and saved to {txt_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
pdf_file_path = '../../datasets/books/pocso_kha.pdf'
txt_file_path = '../../datasets/books/pocso_kha.txt'
extract_sentences_from_pdf(pdf_file_path, txt_file_path)
