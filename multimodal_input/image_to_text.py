import requests

def ocr_image_to_text(image_path):
    with open(image_path, 'rb') as image_file:
        response = requests.post(
            'https://api.ocr.space/parse/image',
            files={'filename': image_file},
            data={'apikey': 'your_api_key_here', 'language': 'eng'},
        )
    result = response.json()
    return result['ParsedResults'][0]['ParsedText'] if result['IsErroredOnProcessing'] is False else "OCR failed"
