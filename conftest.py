import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()

    return collector

@pytest.fixture
def few_books(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")

    collector.add_new_book("Звонок")
    collector.set_book_genre("Звонок", "Ужасы")

    collector.add_new_book("Челюсти")
    collector.set_book_genre("Челюсти", "Ужасы")

    collector.add_new_book("Смешарики")
    collector.set_book_genre("Смешарики", "Мультфильмы")

    collector.add_new_book("Коломбо")
    collector.set_book_genre("Коломбо", "Детективы")

    collector.add_new_book("Бетховен")
    collector.set_book_genre("Бетховен", "Комедии")

    return collector
