defmodule Wikiglobe.DatabaseTest do
  use Wikiglobe.DataCase

  alias Wikiglobe.Database

  describe "wikidatas" do
    alias Wikiglobe.Database.WikiData

    @valid_attrs %{}
    @update_attrs %{}
    @invalid_attrs %{}

    def wiki_data_fixture(attrs \\ %{}) do
      {:ok, wiki_data} =
        attrs
        |> Enum.into(@valid_attrs)
        |> Database.create_wiki_data()

      wiki_data
    end

    test "list_wikidatas/0 returns all wikidatas" do
      wiki_data = wiki_data_fixture()
      assert Database.list_wikidatas() == [wiki_data]
    end

    test "get_wiki_data!/1 returns the wiki_data with given id" do
      wiki_data = wiki_data_fixture()
      assert Database.get_wiki_data!(wiki_data.id) == wiki_data
    end

    test "create_wiki_data/1 with valid data creates a wiki_data" do
      assert {:ok, %WikiData{} = wiki_data} = Database.create_wiki_data(@valid_attrs)
    end

    test "create_wiki_data/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = Database.create_wiki_data(@invalid_attrs)
    end

    test "update_wiki_data/2 with valid data updates the wiki_data" do
      wiki_data = wiki_data_fixture()
      assert {:ok, %WikiData{} = wiki_data} = Database.update_wiki_data(wiki_data, @update_attrs)
    end

    test "update_wiki_data/2 with invalid data returns error changeset" do
      wiki_data = wiki_data_fixture()
      assert {:error, %Ecto.Changeset{}} = Database.update_wiki_data(wiki_data, @invalid_attrs)
      assert wiki_data == Database.get_wiki_data!(wiki_data.id)
    end

    test "delete_wiki_data/1 deletes the wiki_data" do
      wiki_data = wiki_data_fixture()
      assert {:ok, %WikiData{}} = Database.delete_wiki_data(wiki_data)
      assert_raise Ecto.NoResultsError, fn -> Database.get_wiki_data!(wiki_data.id) end
    end

    test "change_wiki_data/1 returns a wiki_data changeset" do
      wiki_data = wiki_data_fixture()
      assert %Ecto.Changeset{} = Database.change_wiki_data(wiki_data)
    end
  end
end
