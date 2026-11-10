FROM python:3.12-slim@sha256:09f7da3bc104798d0afb40bc08d23ab2da20a76130cec1f2ef170848f5d85217 AS native
RUN apt-get update && apt-get install -y --no-install-recommends cmake build-essential && rm -rf /var/lib/apt/lists/*
ADD --checksum=sha256:3111fb4b1f447e7b3d3aa7ab1595c6e0175d887dc4d3bcbf366768371f3d766a https://codeload.github.com/USEPA/Stormwater-Management-Model/tar.gz/07c371f8a0d477da1d9d4e7c0d75719664f62fec /tmp/epa.tar.gz
RUN mkdir /opt/epa && tar -xzf /tmp/epa.tar.gz -C /opt/epa --strip-components=1 && cmake -S /opt/epa -B /opt/build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/native -DCMAKE_INSTALL_RPATH=/opt/native/bin && cmake --build /opt/build -j 2 && cmake --install /opt/build

FROM python:3.12-slim@sha256:09f7da3bc104798d0afb40bc08d23ab2da20a76130cec1f2ef170848f5d85217
WORKDIR /opt/urban-mcp
COPY adapters/swmm/runtime.lock.txt /opt/swmm-runtime.lock.txt
RUN python -m pip install --no-cache-dir -r /opt/swmm-runtime.lock.txt
COPY --from=native /opt/native /opt/native
COPY --from=native /usr/lib/x86_64-linux-gnu/libgomp.so.1.0.0 /usr/lib/x86_64-linux-gnu/libgomp.so.1
COPY --from=native /usr/share/doc/libgomp1/copyright /opt/licenses/libgomp1-copyright
COPY --from=native /usr/share/common-licenses/GPL-3 /opt/licenses/GPL-3
COPY adapters/swmm/licenses /opt/licenses
COPY --from=native /opt/epa /opt/epa
ADD --checksum=sha256:e31265cb5d63cf7c3c760e66b0a42e09a7736053754f2cb933f0fe80dfcfc136 https://codeload.github.com/foundanotusedname/pyswmm-mcp/tar.gz/a4db37b45d3b30dcfbd80fc0162a8238e727a80f /tmp/pyswmm-mcp.tar.gz
RUN mkdir /opt/pyswmm-mcp && tar -xzf /tmp/pyswmm-mcp.tar.gz -C /opt/pyswmm-mcp --strip-components=1 && cp -a /opt/pyswmm-mcp /opt/pyswmm-runtime
COPY adapters/swmm/patch_linux_watchdog.py /opt/patch_linux_watchdog.py
COPY adapters/swmm/linux_watchdog.py /opt/swmm-linux-watchdog.py
RUN python /opt/patch_linux_watchdog.py /opt/pyswmm-runtime > /opt/linux-watchdog-receipt.json && python -m pip install --no-deps /opt/pyswmm-runtime
ADD --chmod=644 --checksum=sha256:ac1098a1573c59eac6d99216f86edd6ce9701ecbfb3440b0af8cc2c4f69302db https://raw.githubusercontent.com/pyswmm/pyswmm/80b9d558f3f235cc347ac8eb9f03d01fe9c55463/pyswmm/tests/data/model_full_features.inp /opt/fixture/model_full_features.inp
RUN chmod 755 /opt/fixture
ENV PYTHONPATH=/opt/urban-mcp PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PATH=/opt/native/bin:$PATH MPLCONFIGDIR=/tmp/matplotlib PYSWMM_MCP_MODEL_ROOT=/data/models PYSWMM_MCP_RUN_ROOT=/data/runs PYSWMM_MCP_MAX_WORKERS=2 PYSWMM_MCP_RETENTION_SECONDS=0 PYSWMM_MCP_MAX_RUNS=0 PYSWMM_MCP_RUN_QUOTA_BYTES=0
COPY urban_mcp_swmm /opt/urban-mcp/urban_mcp_swmm
COPY cases/two-city-swmm /opt/urban-mcp/cases/two-city-swmm
COPY tools/audit_swmm_upstream.py /opt/urban-mcp/tools/audit_swmm_upstream.py
USER 65532:65532
WORKDIR /data
ENTRYPOINT ["python","-m","urban_mcp_swmm"]
CMD ["status"]
