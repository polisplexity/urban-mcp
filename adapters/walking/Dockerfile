FROM python:3.12-slim@sha256:09f7da3bc104798d0afb40bc08d23ab2da20a76130cec1f2ef170848f5d85217
WORKDIR /opt/urban-mcp
COPY adapters/walking/runtime.lock.txt /opt/requirements.txt
RUN python -m pip install --no-cache-dir -r /opt/requirements.txt && python -m pip freeze > /opt/runtime.freeze.txt
ENV PYTHONPATH=/opt/urban-mcp PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR=/tmp/matplotlib XDG_CACHE_HOME=/tmp
COPY urban_mcp_walking /opt/urban-mcp/urban_mcp_walking
COPY cases/two-city-walking /opt/urban-mcp/cases/two-city-walking
USER 65532:65532
WORKDIR /data
ENTRYPOINT ["python", "-m", "urban_mcp_walking"]
CMD ["status"]
