FROM python:3.8-buster
MAINTAINER MAB <mab@mab.net>
# Keep image updated
ENV REFRESHED_AT 2020-04-20-00-00Z

EXPOSE 5000
RUN pip install flask pycurl
ADD webhook.py /
ENV FLASK_APP=/webhook.py
CMD [ "flask", "run", "--host=0.0.0.0" ]
