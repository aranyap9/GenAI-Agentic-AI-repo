from transformers import pipeline

# Load a text2text generation pipeline
generator = pipeline("text2text-generation", model="t5-small")

def modern_to_shakespeare(text):
    prompt = f"translate English to Shakespearean English: {text}"
    result = generator(prompt, max_length=100, do_sample=True)
    return result[0]['generated_text']