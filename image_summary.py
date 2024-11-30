import keras
import keras_nlp
import numpy as np
import PIL
import requests
import io
from PIL import Image


class ImageSummary():
    def __init__(self):
        keras.config.set_floatx("bfloat16")
        self.paligemma = keras_nlp.models.PaliGemmaCausalLM.from_preset("pali_gemma_3b_mix_224")
        self.paligemma.summary()

    def __call__(self, url, target_size=(224, 224)):
        image = self.read_image(url, target_size)
        output = self.paligemma.generate(
            inputs={
                "images": image,
                "prompts": "Summarise image in one short sentence. Summary:",
            }
        )
        return output

    def crop_and_resize(self, image, target_size):
        width, height = image.size
        source_size = min(image.size)
        left = width // 2 - source_size // 2
        top = height // 2 - source_size // 2
        right, bottom = left + source_size, top + source_size
        return image.resize(target_size, box=(left, top, right, bottom))


    def read_image(self, url, target_size):
        contents = io.BytesIO(requests.get(url).content)
        image = PIL.Image.open(contents)
        image = self.crop_and_resize(image, target_size)
        image = np.array(image)
        # Remove alpha channel if neccessary.
        if image.shape[2] == 4:
            image = image[:, :, :3]
        return image



if __name__ == "__main__":
    urls = ["https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/cd43/live/0dfaae30-ae6f-11ef-93a6-9fd2d3586a96.jpg",
            "https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/a003/live/dc55dd90-ae56-11ef-a4be-fb03c4435021.jpg"
            "https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/25b4/live/4237aa80-aeb6-11ef-9026-3f684a99c959.jpg",
            "https://ichef.bbci.co.uk/news/1024/branded_news/fec4/live/79733480-ae73-11ef-8ab9-9192db313061.jpg",
            "https://ichef.bbci.co.uk/images/ic/240x135/p0jpdjgy.jpg",
            "https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/cd43/live/0dfaae30-ae6f-11ef-93a6-9fd2d3586a96.jpg",
            "https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/f876/live/00907960-aefa-11ef-bdf5-b7cb2fa86e10.jpg",
            "https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/8090/live/cb3f89c0-ae6a-11ef-bdf5-b7cb2fa86e10.jpg",
            "https://sb.scorecardresearch.com/p?c1=2&c2=17986528&cs_ucfr=0&cv=2.0&cj=1",
            ]
    image_summary = ImageSummary()
    from speak_gtts import speak
    for i, url in enumerate(urls):
        summary = image_summary(url)
        speak(f"Image {i+1}")
        speak(summary)