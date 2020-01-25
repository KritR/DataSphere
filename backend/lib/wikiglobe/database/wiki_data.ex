defmodule Wikiglobe.Database.WikiData do
  use Ecto.Schema
  import Ecto.Changeset

  schema "wikidatas" do

    timestamps()
  end

  @doc false
  def changeset(wiki_data, attrs) do
    wiki_data
    |> cast(attrs, [])
    |> validate_required([])
  end
end
