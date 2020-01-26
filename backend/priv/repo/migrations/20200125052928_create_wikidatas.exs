defmodule Wikiglobe.Repo.Migrations.CreateWikidatas do
  use Ecto.Migration

  def change do
    create table(:wikidatas) do

      timestamps()
    end

  end
end
