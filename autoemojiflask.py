from flask import Flask, render_template, request
import os
from PIL import Image

app = Flask(__name__)

UPLOAD_DIRECTORY = "./카카오톡"
UPLOAD_DIRECTORY_2 = "./네이버OGQ"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

if not os.path.exists(UPLOAD_DIRECTORY_2):
    os.makedirs(UPLOAD_DIRECTORY_2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file1 = request.files['file1']
    file2 = request.files['file2']
    try:
        im1 = Image.open(file1)
        im2 = Image.open(file2)
    except IOError:
        return 'Cannot open image file'

    width1, height1 = im1.size
    width2, height2 = im2.size
    piece_width = width1 // 4
    piece_height = height1 // 4
    count = 1
    for j in range(4):
        for i in range(4):
            x = i * piece_width
            y = j * piece_height
            piece = im1.crop((x, y, x + piece_width, y + piece_height))
            filename = os.path.join(UPLOAD_DIRECTORY, '{}.png'.format(count))
            piece_360 = piece.resize((360, 360))
            piece_760 = piece.resize((640, 640))

            new_img = Image.new(piece_760.mode, (640, 760), (0, 0, 0, 0))
            new_img.paste(piece_760, (0, 60))

            piece_360.save(filename)
            filename = os.path.join(UPLOAD_DIRECTORY_2, '{}.png'.format(count))
            new_img.save(filename)
            count += 1

    piece_width2 = width2 // 4
    piece_height2 = height2 // 4

    count2 = 17
    for k in range(4):
        for p in range(4):
            x2 = p * piece_width2
            y2 = k * piece_height2
            piece2 = im2.crop((x2, y2, x2 + piece_width2, y2 + piece_height2))
            filename2 = os.path.join(UPLOAD_DIRECTORY, '{}.png'.format(count2))
            piece_3602 = piece2.resize((360, 360))
            piece_7602 = piece2.resize((640, 640))

            new_img2 = Image.new(piece_7602.mode, (640, 760), (0, 0, 0, 0))
            new_img2.paste(piece_7602, (0, 60))

            piece_3602.save(filename2)
            filename2 = os.path.join(UPLOAD_DIRECTORY_2, '{}.png'.format(count2))
            new_img2.save(filename2)
            count2 += 1

    im1.close()
    im2.close()

    return 'Images successfully divided into 16 pieces!'

if __name__ == '__main__':
    app.run(debug=True)
