from enum import Enum


class Intent(str, Enum):
    RANDOM = "random"
    ADD = "add"
    DELETE = "delete"
    READ = "read"
    STATISTICS = "statistics"