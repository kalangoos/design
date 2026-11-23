# figcraft-server from the official Linux release (faster than building Rust on Fly).
# Build context: this directory (deploy/fly/).
#
#   docker build -t kalangoos-figcraft .
#
# Override version: docker build --build-arg VERSION=0.18.1 .

FROM debian:bookworm-slim AS fetch
ARG VERSION=0.18.1
ARG TARGETARCH
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates curl \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /tmp
RUN arch="$TARGETARCH"; \
    case "$arch" in \
      amd64) arch=x86_64 ;; \
      arm64) arch=aarch64 ;; \
      *) echo "unsupported arch: $arch" >&2; exit 1 ;; \
    esac; \
    name="figcraft-server-${VERSION}-linux-${arch}"; \
    curl -fsSL -o server.tgz \
      "https://github.com/storytold/figcraft/releases/download/v${VERSION}/${name}.tar.gz"; \
    tar -xzf server.tgz; \
    install -m 755 "${name}/figcraft-server" /tmp/figcraft-server

FROM gcr.io/distroless/cc-debian12:nonroot
COPY --from=fetch /tmp/figcraft-server /usr/local/bin/figcraft-server
COPY server.toml /etc/figcraft-server/server.toml
USER nonroot
VOLUME /data
EXPOSE 47900
STOPSIGNAL SIGTERM
ENTRYPOINT ["/usr/local/bin/figcraft-server", "--config", "/etc/figcraft-server/server.toml"]
