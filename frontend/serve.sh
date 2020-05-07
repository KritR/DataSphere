#!/bin/sh

docker run -p 80:80 -p 443:443 \
  -v $(PWD):/usr/share/caddy \
  -v caddy_data:/data \
  caddy
echo $(docker ps)
