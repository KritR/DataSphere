defmodule Wikiglobe.Database do
  @moduledoc """
  The Database context.
  """

  import Ecto.Query, warn: false
  alias Wikiglobe.Repo

  alias Wikiglobe.Database.WikiData

  @doc """
  Returns the list of wikidatas.

  ## Examples

      iex> list_wikidatas()
      [%WikiData{}, ...]

  """
  def list_wikidatas do
    Repo.all(WikiData)
  end

  @doc """
  Gets a single wiki_data.

  Raises `Ecto.NoResultsError` if the Wiki data does not exist.

  ## Examples

      iex> get_wiki_data!(123)
      %WikiData{}

      iex> get_wiki_data!(456)
      ** (Ecto.NoResultsError)

  """
  def get_wiki_data!(id), do: Repo.get!(WikiData, id)

  @doc """
  Creates a wiki_data.

  ## Examples

      iex> create_wiki_data(%{field: value})
      {:ok, %WikiData{}}

      iex> create_wiki_data(%{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def create_wiki_data(attrs \\ %{}) do
    %WikiData{}
    |> WikiData.changeset(attrs)
    |> Repo.insert()
  end

  @doc """
  Updates a wiki_data.

  ## Examples

      iex> update_wiki_data(wiki_data, %{field: new_value})
      {:ok, %WikiData{}}

      iex> update_wiki_data(wiki_data, %{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def update_wiki_data(%WikiData{} = wiki_data, attrs) do
    wiki_data
    |> WikiData.changeset(attrs)
    |> Repo.update()
  end

  @doc """
  Deletes a wiki_data.

  ## Examples

      iex> delete_wiki_data(wiki_data)
      {:ok, %WikiData{}}

      iex> delete_wiki_data(wiki_data)
      {:error, %Ecto.Changeset{}}

  """
  def delete_wiki_data(%WikiData{} = wiki_data) do
    Repo.delete(wiki_data)
  end

  @doc """
  Returns an `%Ecto.Changeset{}` for tracking wiki_data changes.

  ## Examples

      iex> change_wiki_data(wiki_data)
      %Ecto.Changeset{source: %WikiData{}}

  """
  def change_wiki_data(%WikiData{} = wiki_data) do
    WikiData.changeset(wiki_data, %{})
  end
end
