from transformers import pipeline # type: ignore

# Load summarization model
summarizer = pipeline("summarization")

def summarize_text(discussion_text):
    # Generate summary from discussion
    summary = summarizer(discussion_text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
