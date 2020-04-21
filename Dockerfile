FROM python:3.8-buster
EXPOSE 5000
RUN pip install flask pycurl
ADD webhook.py /
ENV FLASK_APP=/webhook.py
CMD [ "flask", "run", "--host=0.0.0.0" ]
