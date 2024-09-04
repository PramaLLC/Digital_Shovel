from flask import Flask, request, jsonify
import sys
import os
from .scraper import generating_urls_for_image_processor
import requests
from PIL import Image
from io import BytesIO



app = Flask(__name__)


import uuid 

@app.route('/', methods=['GET'])
def hello_world():
    start_str = request.args.get('start')
    product_name = request.args.get('product_name')

    try:

        start = int(start_str)
     

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    urls = generating_urls_for_image_processor(product_name, start)


    final_urls = []



    for url in urls:
        try:
            response = requests.get(url,timeout=10)  # Disable SSL certificate verification
            if str(response.status_code)[0] == "2":
                image_bytes = response.content
                # Open the image using PIL
                image = Image.open(BytesIO(image_bytes))


                width, height = image.size
                print("width")
                if width > 300 or height > 300:
                    
                    final_urls.append(url)

            else:
                print("stuck in side stuck")

        except Exception as e:
            print("stuck") 

    print(final_urls, file=sys.stderr)
    return  jsonify({"urls": final_urls})





@app.route('/ping', methods=['POST'])
def ping():
    return jsonify({"helloo":"hello"})






port = int(os.getenv('PORT'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)



