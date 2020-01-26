# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.

# General application configuration
use Mix.Config

config :wikiglobe,
  ecto_repos: [Wikiglobe.Repo]

config :cors_plug,
  origin: ["http://datasphere.space"],
  max_age: 86400,
  methods: ["GET", "POST"]

# Configures the endpoint
config :wikiglobe, WikiglobeWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "6AsTcjPY6pxXlm77+sBo8+3RLdo+lGYqtgXeZkJflhBflA6icc54IoLq6c36iUNl",
  render_errors: [view: WikiglobeWeb.ErrorView, accepts: ~w(json)],
  pubsub: [name: Wikiglobe.PubSub, adapter: Phoenix.PubSub.PG2]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Use Jason for JSON parsing in Phoenix
config :phoenix, :json_library, Jason

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env()}.exs"
