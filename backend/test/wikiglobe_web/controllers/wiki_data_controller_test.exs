defmodule WikiglobeWeb.WikiDataControllerTest do
  use WikiglobeWeb.ConnCase

  alias Wikiglobe.Database
  alias Wikiglobe.Database.WikiData

  @create_attrs %{

  }
  @update_attrs %{

  }
  @invalid_attrs %{}

  def fixture(:wiki_data) do
    {:ok, wiki_data} = Database.create_wiki_data(@create_attrs)
    wiki_data
  end

  setup %{conn: conn} do
    {:ok, conn: put_req_header(conn, "accept", "application/json")}
  end

  describe "index" do
    test "lists all wikidatas", %{conn: conn} do
      conn = get(conn, Routes.wiki_data_path(conn, :index))
      assert json_response(conn, 200)["data"] == []
    end
  end

  describe "create wiki_data" do
    test "renders wiki_data when data is valid", %{conn: conn} do
      conn = post(conn, Routes.wiki_data_path(conn, :create), wiki_data: @create_attrs)
      assert %{"id" => id} = json_response(conn, 201)["data"]

      conn = get(conn, Routes.wiki_data_path(conn, :show, id))

      assert %{
               "id" => id
             } = json_response(conn, 200)["data"]
    end

    test "renders errors when data is invalid", %{conn: conn} do
      conn = post(conn, Routes.wiki_data_path(conn, :create), wiki_data: @invalid_attrs)
      assert json_response(conn, 422)["errors"] != %{}
    end
  end

  describe "update wiki_data" do
    setup [:create_wiki_data]

    test "renders wiki_data when data is valid", %{conn: conn, wiki_data: %WikiData{id: id} = wiki_data} do
      conn = put(conn, Routes.wiki_data_path(conn, :update, wiki_data), wiki_data: @update_attrs)
      assert %{"id" => ^id} = json_response(conn, 200)["data"]

      conn = get(conn, Routes.wiki_data_path(conn, :show, id))

      assert %{
               "id" => id
             } = json_response(conn, 200)["data"]
    end

    test "renders errors when data is invalid", %{conn: conn, wiki_data: wiki_data} do
      conn = put(conn, Routes.wiki_data_path(conn, :update, wiki_data), wiki_data: @invalid_attrs)
      assert json_response(conn, 422)["errors"] != %{}
    end
  end

  describe "delete wiki_data" do
    setup [:create_wiki_data]

    test "deletes chosen wiki_data", %{conn: conn, wiki_data: wiki_data} do
      conn = delete(conn, Routes.wiki_data_path(conn, :delete, wiki_data))
      assert response(conn, 204)

      assert_error_sent 404, fn ->
        get(conn, Routes.wiki_data_path(conn, :show, wiki_data))
      end
    end
  end

  defp create_wiki_data(_) do
    wiki_data = fixture(:wiki_data)
    {:ok, wiki_data: wiki_data}
  end
end
