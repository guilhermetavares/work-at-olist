FROM python:3.5  
ENV PYTHONUNBUFFERED 1
ENV APP_USER workatolist
ENV APP_ROOT /work-at-olist
RUN mkdir /work-at-olist;

RUN groupadd -r ${APP_USER} \
    && useradd -r -m \
    --home-dir ${APP_ROOT} \
    -s /usr/sbin/nologin \
    -g ${APP_USER} ${APP_USER}
WORKDIR ${APP_ROOT}

ADD requirements.txt /work-at-olist/
RUN mkdir /requirements;
ADD /requirements /work-at-olist/requirements/
RUN pip install -r /work-at-olist/requirements.txt

USER ${APP_USER}
ADD . ${APP_ROOT}