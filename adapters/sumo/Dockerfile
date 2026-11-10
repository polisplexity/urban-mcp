FROM python:3.12-slim@sha256:09f7da3bc104798d0afb40bc08d23ab2da20a76130cec1f2ef170848f5d85217
WORKDIR /opt/urban-mcp
COPY adapters/sumo/runtime.lock.txt /opt/sumo-runtime.lock.txt
ADD --checksum=sha256:ec7042794e5ab1d806b90a5983aeda4a978dc4224141b94c0ff3affeeb4ec977 https://files.pythonhosted.org/packages/0d/12/b37bcb407bdfe811e1a38179b4abc3142290e589104a33a8f88a3e661eb0/eclipse_sumo-1.28.0-py3-none-manylinux_2_28_x86_64.whl /tmp/eclipse_sumo-1.28.0-py3-none-manylinux_2_28_x86_64.whl
RUN apt-get update && apt-get install -y --no-install-recommends libx11-6 libxext6 libxrender1 libgl1 libglu1-mesa libgomp1 libatomic1 && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --no-cache-dir -r /opt/sumo-runtime.lock.txt /tmp/eclipse_sumo-1.28.0-py3-none-manylinux_2_28_x86_64.whl && sumo --version
ADD --checksum=sha256:1f3238d7013f40381ef0d9a21fffae3190da0150782829fb69e920502b48a44c https://codeload.github.com/XRDS76354/SUMO-MCP-Server/tar.gz/6b62a25c1b13751d636309a03e4388594fcd7620 /tmp/sumo-mcp.tar.gz
RUN mkdir /opt/sumo-mcp && tar -xzf /tmp/sumo-mcp.tar.gz -C /opt/sumo-mcp --strip-components=1
ENV PYTHONPATH=/opt/urban-mcp:/opt/sumo-mcp/src PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 SUMO_HOME=/usr/local/lib/python3.12/site-packages/sumo MPLCONFIGDIR=/tmp/matplotlib PROJ_DATA=/usr/local/lib/python3.12/site-packages/sumo/data/proj PROJ_LIB=/usr/local/lib/python3.12/site-packages/sumo/data/proj
COPY urban_mcp_sumo /opt/urban-mcp/urban_mcp_sumo
COPY cases/two-city-sumo /opt/urban-mcp/cases/two-city-sumo
USER 65532:65532
WORKDIR /data
ENTRYPOINT ["python","-m","urban_mcp_sumo"]
CMD ["status"]
