from apiWeb.models.book import Book


class UtilBook:
    @staticmethod
    def get_book(book: Book):
        try:
            book_obj = {"id": int(book.id),
                        "name": str(book.name),
                        "author": str(book.author),
                        "Publishers": str(book.Publishers),
                        "image": str(book.image_link),
                        "link": str(book.link),
                        "is_ad": str(book.is_ad)}
            return book_obj
        except Exception as e:
            print("Error book :", str(e))
            return str(e)

    @staticmethod
    def get_latest_book():
        try:
            latest_book = Book.objects.order_by('-id')[:6]
            result_book = map(lambda podcast: UtilBook.get_book(podcast),
                              latest_book) if latest_book else []
            return result_book

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_book():
        try:
            all_book = Book.objects.order_by('-id')
            result_book = map(lambda podcast: UtiBook.get_book(podcast), all_book) if all_book else []
            return result_book

        except Exception as e:
            return [str(e)]
