defmodule WikiglobeWeb.WikiDataView do
  use WikiglobeWeb, :view
  alias WikiglobeWeb.WikiDataView

  def render("index.json", %{wikidatas: wikidatas}) do
    %{data: render_many(wikidatas, WikiDataView, "wiki_data.json")}
  end

  def render("show.json", %{wiki_data: wiki_data}) do
    %{data: render_one(wiki_data, WikiDataView, "wiki_data.json")}
  end

  def render("wiki_data.json", %{wiki_data: wiki_data}) do
    %{
      title: wiki_data["title"], 
      year: wiki_data["date"], 
      location: wiki_data["location"],
      description: wiki_data["description"],
      url: wiki_data["url"],
      image: wiki_data["image"]
    }
  end
end
