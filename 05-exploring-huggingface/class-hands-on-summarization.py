from transformers import pipeline

MODEL = "facebook/bart-large-cnn"

model = pipeline("summarization", model=MODEL)

text = """
The answer was within her reach. It was hidden in a box and now that box sat directly 
in front of her. She'd spent years searching for it and could hardly believe she'd 
finally managed to find it. She turned the key to unlock the box and then gently lifted 
the top. She held her breath in anticipation of finally knowing the answer she had spent 
so much of her time in search of. As the lid came off she could see that the box was empty.
Sarah watched the whirlpool mesmerized. She couldn't take her eyes off the water swirling 
around and around. She stuck in small twigs and leaves to watch the whirlpool catch them 
and then suck them down. It bothered her more than a little bit that this could also be 
used as a metaphor for her life.
"Explain to me again why I shouldn't cheat?" he asked. "All the others do and nobody ever 
gets punished for doing so. I should go about being happy losing to cheaters because I 
know that I don't? That's what you're telling me?"
"""
result = model(text)

print("Summary: ")
print(result[0]["summary_text"])