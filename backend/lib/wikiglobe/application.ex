defmodule Wikiglobe.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  def start(_type, _args) do
    # List all child processes to be supervised
    children = [
      # Start the Ecto repository
      # Wikiglobe.Repo,
      # Start the endpoint when the application starts
      WikiglobeWeb.Endpoint,
      {Mongo, [name: :mongo, url: "mongodb+srv://backend:skarpassword@skarcluster-zb6ru.gcp.mongodb.net/test?retryWrites=true&w=majority", pool: DBConnection.Poolboy]},
      # Starts a worker by calling: Wikiglobe.Worker.start_link(arg)
      # {Wikiglobe.Worker, arg},
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: Wikiglobe.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  def config_change(changed, _new, removed) do
    WikiglobeWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
