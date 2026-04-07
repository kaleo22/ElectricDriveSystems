FROM antmicro/renode:latest

USER root

# Install GUI runtime dependencies so Renode can open its X11 UI.
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		libgtk-3-0 \
		libcanberra-gtk3-module \
		xauth \
	&& rm -rf /var/lib/apt/lists/*

USER ubuntu
