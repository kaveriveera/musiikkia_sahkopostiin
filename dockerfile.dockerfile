FROM python
WORKDIR /sahkoposti
COPY . /sahkoposti
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]