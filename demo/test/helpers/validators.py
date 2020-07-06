import re
import iso639


class Validators:
    @staticmethod
    def is_valid_gender(item: str) -> bool:
        return item in ['Male', 'Female']

    @staticmethod
    def is_valid_name(item: str) -> bool:
        matches = re.match(r"([A-Za-z]+|\s+|-+)", item)
        return matches is not None

    @staticmethod
    def is_valid_date(item: str) -> bool:
        matches = re.match(r"(\w+)", item)
        return matches is not None

    @staticmethod
    def is_valid_mail(item: str) -> bool:
        matches = re.search(r"[\w]+\@[\w]+\.[a-z]{2,3}", item)
        return matches is not None

    @staticmethod
    def is_valid_id(item: str) -> bool:
        return item.isdigit()

    @staticmethod
    def is_valid_ip(item: str) -> bool:
        matches = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", item)
        return matches is not None

    @staticmethod
    def is_valid_language(item: str) -> bool:
        return iso639.find(whatever=item) is not None
