import os
from PIL import Image
from clip_interrogator import Config, Interrogator
import openai

def jpg_to_dynamic(image_path):
    image = Image.open(image_path).convert('RGB')
    ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))
    img_description = ci.interrogate(image)
    
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    
    messages = [{"role": "user", "content": ""}]
    response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
