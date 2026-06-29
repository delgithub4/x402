class PaginationValidator:

    @staticmethod
    def validate(
        page,
        size,
    ):

        if page < 1:

            raise ValueError(
                "Invalid page."
            )

        if size < 1:

            raise ValueError(
                "Invalid page size."
            )

        return True
