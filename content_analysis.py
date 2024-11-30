from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from torch.nn.functional import softmax
from dotenv import load_dotenv
load_dotenv()

tokenizer = AutoTokenizer.from_pretrained("google/shieldgemma-2b")
model = AutoModelForSequenceClassification.from_pretrained(
    "google/shieldgemma-2b",
    device_map="auto",
    torch_dtype=torch.bfloat16,
)
def check_sensitive_content(text): 
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)  # Convert logits to probabilities
    
    offensive_probability = probabilities[0][1].item()
    print(f"Offensive probability: {offensive_probability}")
    return offensive_probability >= 0.5     # Return True if the probability of being offensive is greater than a threshold (e.g., 0.5)

text = "This is good news" 
result = check_sensitive_content(text)
print(f"Is the text offensive? {result}")

