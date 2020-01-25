defmodule WikiglobeWeb.Router do
  use WikiglobeWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/api", WikiglobeWeb do
    pipe_through :api
  end
end
