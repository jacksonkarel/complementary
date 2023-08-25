from PIL import Image
from clip_interrogator import Config, Interrogator

def clip_interrogator_local(image_path):
    image = Image.open(image_path).convert('RGB')
    ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))
    img_description = ci.interrogate(image)

    return img_description