#Generating text using a pre-trained model
# as a prerequisite, you need to install the transformers library
# pip install transformers
#pip install torch

from transformers import pipeline
# Load the text generation pipeline
import torch
# Check if GPU is available and set the device accordingly
# at beginning of the script
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = pipeline("text-generation", model="gpt2",device = 0)
# # Generate text based on a prompt

sentence = model("Once upon a time in a land far, far away", 
                 do_sample=True, top_k=50, 
                 temperature=0.9, max_length=100, 
                 num_return_sequences=2  )

for i in sentence:
  print(i["generated_text"])