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
    %{name: wiki_data.name, year: wiki_data.year}
  end
end
