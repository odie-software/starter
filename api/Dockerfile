FROM python:3.11-bookworm
USER ${UID}:${GID}

# Name it
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=True

WORKDIR /app
COPY . .

RUN apt update

# python
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
ENV VIRTUAL_ENV="/venv"

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000

ENTRYPOINT ["bash"]

CMD ["bin/entrypoint"]
