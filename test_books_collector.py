import pytest


class TestBooksCollector:
    def test_add_new_book_add_book(self, collector, new_book):
        collector.add_new_book(new_book)

        assert collector.get_book_genre(new_book) == ""

    @pytest.mark.parametrize(
        "book_name, expected_result",
        [
            ["1234567890123456789012345678901234567890", ""],
            ["12345678901234567890123456789012345678901", None],
            ["", None],
            [" ", ""],
        ],
    )
    def test_add_new_book_boundary_values(self, collector, book_name, expected_result):
        collector.add_new_book(book_name)

        assert collector.get_book_genre(book_name) == expected_result

    def test_set_book_genre_correct_set_genre(self, collector, new_book):

        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, "Ужасы")

        assert collector.get_book_genre(new_book) == "Ужасы"

    @pytest.mark.parametrize("genre", ["Тестовый жанр", " ", "", "Ужас"])
    def test_set_book_genre_set_incorrect_genre_values(
        self, collector, new_book, genre
    ):

        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, genre)

        assert collector.get_book_genre(new_book) == ""

    def test_get_book_genre_no_such_book_none(self, collector, new_book):

        assert collector.get_book_genre(new_book) is None

    @pytest.mark.parametrize(
        "book_genre,expected_books",
        [
            ("Фантастика", ["Гарри Поттер"]),
            ("Ужасы", ["Звонок", "Челюсти"]),
            ("Мультфильмы", ["Смешарики"]),
            ("Детективы", ["Коломбо"]),
            ("Комедии", ["Бетховен"]),
        ],
    )
    def test_get_books_with_specific_genre_check_all_genres(
        self, few_books, book_genre, expected_books
    ):

        assert few_books.get_books_with_specific_genre(book_genre) == expected_books

    def test_get_books_genre_check_all_genres_correct(self, few_books):

        books_genre = {
            "Гарри Поттер": "Фантастика",
            "Звонок": "Ужасы",
            "Челюсти": "Ужасы",
            "Смешарики": "Мультфильмы",
            "Коломбо": "Детективы",
            "Бетховен": "Комедии",
        }

        assert few_books.get_books_genre() == books_genre

    def test_get_books_for_children_only_right_genres_in_res(self, few_books):

        assert few_books.get_books_for_children() == [
            "Гарри Поттер",
            "Смешарики",
            "Бетховен",
        ]

    def test_add_book_in_favorites_add_correct_book(self, collector, new_book):

        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)

        assert collector.get_list_of_favorites_books() == ["Оно"]

    def test_add_book_in_favorites_add_incorrect_book(self, collector, new_book):

        collector.add_book_in_favorites(new_book)

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_correct_book(self, few_books):

        few_books.add_book_in_favorites("Коломбо")
        few_books.add_book_in_favorites("Гарри Поттер")

        few_books.delete_book_from_favorites("Коломбо")

        assert few_books.get_list_of_favorites_books() == ["Гарри Поттер"]

    def test_get_list_of_favorites_books_full_list(self, few_books):
        few_books.add_book_in_favorites("Звонок")
        few_books.add_book_in_favorites("Гарри Поттер")

        assert few_books.get_list_of_favorites_books() == ["Звонок", "Гарри Поттер"]

    def test_get_list_of_favorites_books_empty_list(self, few_books):

        assert few_books.get_list_of_favorites_books() == []
