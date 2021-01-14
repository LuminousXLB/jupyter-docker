FROM python:3.8-slim

COPY server.py /workdir/server.py
WORKDIR /workdir

RUN pip3 config set global.index-url https://mirrors.sjtug.sjtu.edu.cn/pypi/web/simple && \
    pip3 install psycopg2-binary

CMD ["python3", "server.py"]
