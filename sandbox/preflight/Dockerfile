FROM python:3.12-slim@sha256:09f7da3bc104798d0afb40bc08d23ab2da20a76130cec1f2ef170848f5d85217
COPY requirements-dev.txt /opt/planning/requirements-dev.txt
RUN python -m pip install --no-cache-dir -r /opt/planning/requirements-dev.txt
USER 65532:65532
WORKDIR /workspace
ENTRYPOINT ["python"]
