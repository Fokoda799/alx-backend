#!/usr/bin/env python3
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return a
    tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.


    Returns:
        Tuple[int, int]: Tuple containing start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get a page from the dataset """
        assert isinstance(page, int) and page > 0, "page should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size should be a positive integer"

        self.dataset()  # Ensure the dataset is loaded

        start, end = index_range(page, page_size)

        if start >= len(self.__dataset):
            return []

        return self.__dataset[start:end]

