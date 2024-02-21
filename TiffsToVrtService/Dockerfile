FROM osgeo/gdal:ubuntu-small-3.6.3

RUN apt-get update && \
    apt-get install -y \
    python3-pip\
    --no-install-recommends

WORKDIR /app

RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install -r /tmp/requirements.txt

COPY . /app

CMD ["python", "main.py"]
