# Perplexity AI API csv

Ten projekt integruje się z API Perplexity AI, aby przetwarzać zapytania masowo z pliku csv i uzyskiwać odpowiedzi na podstawie podanych promptów.
Wybrany model `llama-3.1-sonar-small-128k-chat`, można zmienić w 21 linii w pliku: `get_perplexity.py`
Lista dostępnych modeli w api: `https://docs.perplexity.ai/guides/model-cards`

## Struktura projektu

- `config.py`: Zawiera funkcje do tworzenia i odczytywania pliku konfiguracyjnego z kluczem API.
- `file_operations.py`: Zawiera funkcje do odczytywania plików CSV i zapisywania wyników do plików tekstowych.
- `get_perplexity.py`: Zawiera funkcję do komunikacji z API Perplexity AI.
- `main.py`: Główny plik uruchamiający aplikację.

## Instalacja

1. Sklonuj repozytorium:
    ```sh
    git clone https://github.com/akowynia/csv_perplexity.git
    cd csv_perplexity
    ```

2. Zainstaluj wymagane biblioteki:
    ```sh
    pip install -r requirements.txt
    ```

## Użycie

1. Uruchom skrypt `main.py`:
    ```sh
    python main.py
    ```

2. Postępuj zgodnie z instrukcjami wyświetlanymi w konsoli:
    - Wprowadź klucz API, jeśli plik konfiguracyjny nie istnieje.
    - Podaj ścieżkę do pliku tekstowego, w którym mają być zapisywane wyniki.
    - Podaj prompt do użycia w zapytaniach do API.
    - Podaj ścieżkę do pliku CSV z pytaniami.

## Pliki

- [config.py](config.py)
  - [`create_config`](config.py) - Tworzy plik konfiguracyjny z kluczem API.
  - [`read_config`](config.py) - Odczytuje klucz API z pliku konfiguracyjnego.

- [file_operations.py](file_operations.py)
  - [`read_csv_file`](file_operations.py) - Odczytuje plik CSV i przetwarza każdą linię.
  - [`create_txt_file_if_not_exists`](file_operations.py) - Tworzy plik tekstowy, jeśli nie istnieje.

- [get_perplexity.py](get_perplexity.py)
  - [`get_perplexity`](get_perplexity.py) - Wysyła zapytanie do API Perplexity AI i zwraca odpowiedź.

- [main.py](main.py) - Główny plik uruchamiający aplikację.

## Wymagania

- Python 3.x
- Biblioteki wymienione w `requirements.txt`


## Licencja

Ten projekt jest licencjonowany na warunkach licencji MIT. 