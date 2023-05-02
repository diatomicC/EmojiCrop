# Auto Emoji Converter with Flask

This is a simple Flask application that divides two input images into 16 pieces each and saves them as individual PNG files. It also resizes the pieces and creates new images with the resized pieces.

## Installation

1. Clone the repository using the command `git clone https://github.com/username/repo.git`.
2. Navigate into the project directory using the command `cd Auto-Emoji-Converter`.
3. Install the required dependencies using the command `pip install -r requirements.txt`.

## Usage

1. Start the Flask application by running the command `python app.py`.
2. Navigate to `http://localhost:5000/` in your web browser.
3. Upload two images by clicking on the `Choose File` buttons and selecting the desired images.
4. Click on the `Upload` button to divide the images into 16 pieces and save them.

The resulting images will be saved in the `./카카오톡` and `./네이버OGQ` directories.

## Dependencies

- Flask
- Pillow (PIL)

---

# Flask를 이용한 자동 이모티콘 변환기

이 프로젝트는 두 개의 입력 이미지를 16개 조각으로 나누고 각각을 PNG 파일로 저장하는 간단한 Flask 어플리케이션입니다. 또한 이미지를 리사이즈하고 리사이즈된 이미지로 새로운 이미지를 만듭니다.

## 설치

1. `git clone https://github.com/username/repo.git` 명령어를 사용하여 레포지토리를 클론합니다.
2. `cd Auto-Emoji-Converter` 명령어를 사용하여 프로젝트 디렉토리로 이동합니다.
3. `pip install -r requirements.txt` 명령어를 사용하여 필요한 종속성을 설치합니다.

## 사용법

1. `python app.py` 명령어를 실행하여 Flask 어플리케이션을 시작합니다.
2. 웹 브라우저에서 `http://localhost:5000/`로 이동합니다.
3. `Choose File` 버튼을 클릭하여 두 개의 이미지를 업로드합니다.
4. `Upload` 버튼을 클릭하여 이미지를 16개 조각으로 나누고 저장합니다.

결과 이미지는 `./카카오톡`과 `./네이버OGQ` 디렉토리에 저장됩니다.

## 종속성

- Flask
- Pillow (PIL)

