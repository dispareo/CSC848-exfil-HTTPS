from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'exfil-data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#There is no authentication with this, but I wanted to name the API upload anyway 
@app.route('/login', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename == '':
        return 'Ah, dont think there is a file attached', 400

    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)

    print(f"File exfil'd to: {save_path}")
    return 'Success', 200

if __name__ == '__main__':
#    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True)
#    app.run(debug=True)
     app.run(ssl_context=("cert.pem", "key.pem"), debug=True, port=443)
