FROM python:3

ADD api.py /
ADD classify.py /

RUN pip3 install flask
RUN pip3 install flask_restful
RUN pip3 install tensorflow

CMD [ "python", "./api.py" ]
