# DataSphere Monorepo

### Running Development Mode

> docker-compose -f ./docker-compose.dev.yml up

If you want the local page to actually query data from the local server.
Run the following in the javascript console

> enableDebug()

Should live reload files and whatnot

Website is at https://localhost

API is at localhost/api/v1

Make sure you accept the ssl certificate override (recommend Safari / Firefox)
Safari doesn't like external certificates from non localhost
(aka use localhost instead of 127.0.0.1)

### Running Production Mode

> docker-compose -f ./docker-compose.prod.yml up

For deployment. Make sure you have SECRET_KEY_BASE assigned in ./.secrets.env
