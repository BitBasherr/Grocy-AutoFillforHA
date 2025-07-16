FROM ghcr.io/hassio-addons/base-python:14.2.3

ENV LANG C.UTF-8

COPY grocy_autofill.py /grocy_autofill.py

RUN pip install requests

CMD [ "python3", "/grocy_autofill.py" ]
