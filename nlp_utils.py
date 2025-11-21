import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

# Load spaCy model
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Downloading spaCy model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load('en_core_web_sm')

def summarize_text(text: str, ratio: float = 0.3) -> str:
    """
    Summarizes the given text using extractive summarization.
    :param text: The input text to summarize.
    :param ratio: The ratio of sentences to keep (default 0.3).
    :return: The summarized text.
    """
    if not text:
        return ""
    
    doc = nlp(text)
    
    # Calculate word frequencies
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in STOP_WORDS and word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

    if not word_frequencies:
        return text

    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency

    # Calculate sentence scores
    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    # Select top sentences
    select_length = int(len(sentence_tokens) * ratio)
    if select_length < 1:
        select_length = 1
        
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    
    return summary
