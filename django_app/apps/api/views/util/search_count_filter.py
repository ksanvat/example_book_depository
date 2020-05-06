from rest_framework import filters


class SearchCountFilter(filters.SearchFilter):
    search_param = 'count'
