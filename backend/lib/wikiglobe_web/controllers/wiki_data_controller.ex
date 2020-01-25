defmodule WikiglobeWeb.WikiDataController do
  use WikiglobeWeb, :controller

  alias Wikiglobe.Database
  alias Wikiglobe.Database.WikiData

  action_fallback WikiglobeWeb.FallbackController

  def index(conn, %{"year" => year} = params) do
    
    wikidatas = [%{
      :name => "param was provided",
      :year => year
      }] #Database.list_wikidatas()
    render(conn, "index.json", wikidatas: wikidatas)
  end

  def index(conn, _params) do
    wikidatas = [%{
      :name => "no params provided",
      :year => "none"
      }] #Database.list_wikidatas()
    render(conn, "index.json", wikidatas: wikidatas)
  end

  def create(conn, %{"wiki_data" => wiki_data_params}) do
    with {:ok, %WikiData{} = wiki_data} <- Database.create_wiki_data(wiki_data_params) do
      conn
      |> put_status(:created)
      |> put_resp_header("location", Routes.wiki_data_path(conn, :show, wiki_data))
      |> render("show.json", wiki_data: wiki_data)
    end
  end

  def show(conn, %{"id" => id}) do
    wiki_data = Database.get_wiki_data!(id)
    render(conn, "show.json", wiki_data: wiki_data)
  end

  def update(conn, %{"id" => id, "wiki_data" => wiki_data_params}) do
    wiki_data = Database.get_wiki_data!(id)

    with {:ok, %WikiData{} = wiki_data} <- Database.update_wiki_data(wiki_data, wiki_data_params) do
      render(conn, "show.json", wiki_data: wiki_data)
    end
  end

  def delete(conn, %{"id" => id}) do
    wiki_data = Database.get_wiki_data!(id)

    with {:ok, %WikiData{}} <- Database.delete_wiki_data(wiki_data) do
      send_resp(conn, :no_content, "")
    end
  end
end
