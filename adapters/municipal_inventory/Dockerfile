FROM python:3.12-slim@sha256:09f7da3bc104798d0afb40bc08d23ab2da20a76130cec1f2ef170848f5d85217
WORKDIR /opt/urban-mcp
COPY adapters/municipal_inventory/upstream-constraints.txt /opt/upstream-constraints.txt
ADD --checksum=sha256:46a97d684816f5614525554d6b080ad8c27fa568d30896c17fba160c1e0dee13 https://codeload.github.com/JordanGunn/gdal-mcp/tar.gz/418f401c7987e388eaaee6ad13289798a1ff69b6 /tmp/upstream.tar.gz
RUN mkdir /opt/gdal-mcp && tar -xzf /tmp/upstream.tar.gz -C /opt/gdal-mcp --strip-components=1 \
    && SETUPTOOLS_SCM_PRETEND_VERSION=0.0.0+418f401 python -m pip install --no-cache-dir -c /opt/upstream-constraints.txt /opt/gdal-mcp pytest pytest-asyncio \
    && python -m pip freeze > /opt/runtime.freeze.txt
RUN apt-get update && apt-get install -y --no-install-recommends libexpat1 \
    && rm -rf /var/lib/apt/lists/*
COPY adapters/municipal_inventory/apply_compat.py /opt/apply_compat.py
RUN python /opt/apply_compat.py /usr/local/lib/python3.12/site-packages/src \
    && python /opt/apply_compat.py /opt/gdal-mcp/src
ENV PYTHONPATH=/opt/urban-mcp PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 GDAL_MCP_WORKSPACES=/data VECTOR=true RASTER=true FASTMCP_LOG_LEVEL=CRITICAL
COPY urban_mcp_case /opt/urban-mcp/urban_mcp_case
COPY cases/helsinki-service-inventory /opt/urban-mcp/cases/helsinki-service-inventory
USER 65532:65532
WORKDIR /data
ENTRYPOINT ["python", "-m", "urban_mcp_case"]
CMD ["status"]
