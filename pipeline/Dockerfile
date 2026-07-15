FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
# RUN pip install pandas pyarrow
WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"
COPY pyproject.toml .python-version uv.lock ./

COPY pipeline.py  .
RUN uv sync --locked
ENTRYPOINT ["python", "pipeline.py"]

