# API Tester

## Opis
Skrypt `api_tester.py` automatycznie testuje różne endpointy API JSONPlaceholder za pomocą narzędzia `curl`. Skrypt wysyła żądania HTTP do wybranych endpointów, sprawdza status odpowiedzi HTTP, parsuje odpowiedzi JSON i sprawdza obecność kluczowych elementów. Możesz łatwo dostosować go do testowania innych endpointów lub API, zmieniając wartości w liście `tests`.

## Uruchomienie skryptu
1. Upewnij się, że masz zainstalowany Python oraz narzędzie curl.
2. Uruchom skrypt komendą:
    ```bash
    python api_tester.py
    ```
3. Skrypt wyświetli wyniki testów w formacie PASSED lub FAILED, w zależności od tego, czy odpowiedzi spełniają określone warunki.

## Przykładowe wyniki
```
Test https://jsonplaceholder.typicode.com/posts/1: PASSED
Test https://jsonplaceholder.typicode.com/comments/1: PASSED
Test https://jsonplaceholder.typicode.com/albums/1: PASSED
```
