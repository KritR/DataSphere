defmodule WikiglobeWeb.WikiDataView do
  use WikiglobeWeb, :view
  alias WikiglobeWeb.WikiDataView

  def render("index.json", %{events: events}) do
    %{data: render_many(events, WikiDataView, "event.json")}
  end

  def render("show.json", %{events: event}) do
    %{data: render_one(event, WikiDataView, "event.json")}
  end


  def render("event.json", %{wiki_data: event}) do
    %{
      title: event["title"], 
      year: event["date"], 
      location: event["location"],
      description: event["description"],
      url: event["url"],
      image: event["image"]
    }
  end

  def render("index.json", %{earthquakes: earthquakes}) do
    %{data: render_many(earthquakes, WikiDataView, "earthquake.json")}
  end

  def render("show.json", %{earthquakes: earthquake}) do
    %{data: render_one(earthquake, WikiDataView, "earthquake.json")}
  end

  def render("earthquake.json", %{wiki_data: earthquakes}) do
    %{
      location_name: earthquakes["location_name"], 
      year: earthquakes["year"], 
      location: earthquakes["location"],
      eq_primary: earthquakes["eq_primary"],
    }
  end
end
