# Wikiglobe

To start your Phoenix server:

  * Install dependencies with `mix deps.get`
  * Create and migrate your database with `mix ecto.setup`
  * Start Phoenix endpoint with `mix phx.server`

Now you can visit [`localhost:4000`](http://localhost:4000) from your browser.

Ready to run in production? Please [check our deployment guides](https://hexdocs.pm/phoenix/deployment.html).

# Docker Usage

This is to run the server
```
docker run --rm -it -p 4000:4000 -v $PWD:/opt/app bitwalker/alpine-elixir-phoenix mix phx.server
```

mix phx.server can be substituted for any command


