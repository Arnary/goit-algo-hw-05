from timeit import timeit

from kmp_search import kmp_search
from boyer_moore_search import boyer_moore_search
from rabin_karp_search import rabin_karp_search


non_existent_pattern = "Колись давно у далекій-далекій галактиці..."

with open("03/article_1.txt", "r") as text:
    existing_pattern = "експоненціальні позиції"

    kmp_article_1 = timeit(lambda: kmp_search(text.read(), existing_pattern))
    boyer_moore_article_1 = timeit(lambda: boyer_moore_search(text.read(), existing_pattern))
    rabin_karp_article_1 = timeit(lambda: rabin_karp_search(text.read(), existing_pattern))

    n_kmp_article_1 = timeit(lambda: kmp_search(text.read(), non_existent_pattern))
    n_boyer_moore_article_1 = timeit(lambda: boyer_moore_search(text.read(), non_existent_pattern))
    n_rabin_karp_article_1 = timeit(lambda: rabin_karp_search(text.read(), non_existent_pattern))

with open("03/article_2.txt", "r") as text:
    existing_pattern = "булевих функцій у формі"

    kmp_article_2 = timeit(lambda: kmp_search(text.read(), existing_pattern))
    boyer_moore_article_2 = timeit(lambda: boyer_moore_search(text.read(), existing_pattern))
    rabin_karp_article_2 = timeit(lambda: rabin_karp_search(text.read(), existing_pattern))

    n_kmp_article_2 = timeit(lambda: kmp_search(text.read(), non_existent_pattern))
    n_boyer_moore_article_2 = timeit(lambda: boyer_moore_search(text.read(), non_existent_pattern))
    n_rabin_karp_article_2 = timeit(lambda: rabin_karp_search(text.read(), non_existent_pattern))


print(f"| {'Article 1':^102} |")
print(f"| {'-'*103}|")
print(f"{'| Algorithm': <14} | {'Processing time for existing substring': <42} | {'Processing time for non-existent substring': <42} |")
print(f"| {'-'*12} | {'-'*42} | {'-'*42} |")
print(f"| {'KMP':<12} | {kmp_article_1:^42f} | {n_kmp_article_1:^42f} |")
print(f"| {'Boyer-Moore':<12} | {boyer_moore_article_1:^42f} | {n_boyer_moore_article_1:^42f} |")
print(f"| {'Rabin-Karp':<12} | {rabin_karp_article_1:^42f} | {n_rabin_karp_article_1:^42f} |")

print("\n", ("*" * 105), "\n")

print(f"| {'Article 2':^102} |")
print(f"| {'-'*103}|")
print(f"{'| Algorithm': <14} | {'Processing time for existing substring': <42} | {'Processing time for non-existent substring': <42} |")
print(f"| {'-'*12} | {'-'*42} | {'-'*42} |")
print(f"| {'KMP':<12} | {kmp_article_2:^42f} | {n_kmp_article_2:^42f} |")
print(f"| {'Boyer-Moore':<12} | {boyer_moore_article_2:^42f} | {n_boyer_moore_article_2:^42f} |")
print(f"| {'Rabin-Karp':<12} | {rabin_karp_article_2:^42f} | {n_rabin_karp_article_2:^42f} |")