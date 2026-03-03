# qa_python

add_new_book

1. test_add_new_book_add_book. Создание книги корректное
2. test_add_new_book_boundary_values Создание книги пограничные значения. Параметризованный тест

set_book_genre

3. test_set_book_genre_correct_set_genre. Позитивный тест, есть такая книга и такой жанр
4. test_set_book_genre_set_incorrect_genre_values. Некорректные значения жанра. Параметризованный тест

get_book_genre

5. test_get_book_genre_no_such_book_none. Нет такого имени - None

get_books_with_specific_genre

6. test_get_books_with_specific_genre_check_different_genres. Параметризованный тест, проверка вывода фильмов по жанру

get_books_genre

7. test_get_books_genre_check_few_genres_correct. Проверка вывода текущего словаря 4 элемента

get_books_for_children

8. test_get_books_for_children_only_right_genres_in_res Проверка что неподходящие жанры отсутствуют в списке

add_book_in_favorites

9. test_add_book_in_favorites_add_correct_book. Корректное добавление книги в избранное
10. test_add_book_in_favorites_add_incorrect_book. Книги нет в списке книг - не добавлена в избранное

delete_book_from_favorites

11. test_delete_book_from_favorites_correct_book. Корректное удаление книги из избранного

get_list_of_favorites_books

12. test_get_list_of_favorites_books_full_list. Проверка заполненного избранного

13. test_get_list_of_favorites_books_empty_list. Проверка пустого избранного


