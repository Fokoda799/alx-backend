#!/usr/bin/env python3
""" Simple pagination """
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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()  # Ensure the dataset is loaded
        start, end = index_range(page, page_size)
        if start >= len(self.__dataset):
            return []
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Get a page with hypermedia pagination """
        n = self.get_page(page + 1, page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if n else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": math.ceil(len(self.__dataset) / page_size)
        }
