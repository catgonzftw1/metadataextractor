FROM python:3
ADD *.py /
ADD requirements.txt /
ADD MetadataExtractor /
RUN apt-get update && apt-get install -y python3-opencv openjdk-11-jdk tesseract-ocr
RUN pip install -r ./requirements.txt
RUN python -c "import nltk; nltk.download('punkt')"
CMD [ "python", "./server.py" ]
