import timeit
# Алгоритм Кнута-Морріса-Пратта

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern
    indexes = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            indexes.append(i - len(pattern)) 
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    print(f"Пошук Алгоритмом Кнута-Морріса-Пратта: {indexes}") if indexes else  print(f"За запитом '{pattern}' нічого не знайдено")


# Алгоритм Боєра-Мура

def build_shift_table(pattern):
  """Створити таблицю зсувів для алгоритму Боєра-Мура."""
  table = {}
  length = len(pattern)

  # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
  for index, char in enumerate(pattern[:-1]):
    table[char] = length - index - 1
  # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
  table.setdefault(pattern[-1], length)
  return table

def boyer_moore_search(text, pattern):
  indexes = []
  # Створюємо таблицю зсувів для патерну (підрядка)
  shift_table = build_shift_table(pattern)
  i = 0 # Ініціалізуємо початковий індекс для основного тексту

  # Проходимо по основному тексту, порівнюючи з підрядком
  while i <= len(text) - len(pattern):
    j = len(pattern) - 1 # Починаємо з кінця підрядка

    # Порівнюємо символи від кінця підрядка до його початку
    while j >= 0 and text[i + j] == pattern[j]:
      j -= 1 # Зсуваємось до початку підрядка

    # Якщо весь підрядок збігається, повертаємо його позицію в тексті
    if j < 0:
      indexes.append(i) 

    i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

  print(f"Пошук Алгоритмом Боєра-Мура: {indexes}") if indexes else  print(f"За запитом '{pattern}' нічого не знайдено")



# Алгоритм Рабіна-Карпа
def polynomial_hash(s, base=256, modulus=101):
  """
  Повертає поліноміальний хеш рядка s.
  """
  n = len(s)
  hash_value = 0
  for i, char in enumerate(s):
      power_of_base = pow(base, n - i - 1) % modulus
      hash_value = (hash_value + ord(char) * power_of_base) % modulus
  return hash_value

def rabin_karp_search(main_string, substring):
  # Довжини основного рядка та підрядка пошуку
  substring_length = len(substring)
  main_string_length = len(main_string)
  indexes = []
  
  # Базове число для хешування та модуль
  base = 256 
  modulus = 101  
  
  # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
  substring_hash = polynomial_hash(substring, base, modulus)
  current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
  
  # Попереднє значення для перерахунку хешу
  h_multiplier = pow(base, substring_length - 1) % modulus
  
  # Проходимо крізь основний рядок
  for i in range(main_string_length - substring_length + 1):
      if substring_hash == current_slice_hash:
          if main_string[i:i+substring_length] == substring:
              indexes.append(i) 

      if i < main_string_length - substring_length:
          current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
          current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
          if current_slice_hash < 0:
              current_slice_hash += modulus

  print(f"Пошук Алгоритмом Рабіна-Карпа: {indexes}") if indexes else  print(f"За запитом '{substring}' нічого не знайдено")





article1 = "./task_3/test_data/test_data1.txt"
article2 = "./task_3/test_data/test_data2.txt"
pattern = "алгоритмів"

with open(article1, "r", encoding="utf-8") as file:
    text_1 = file.read()

with open(article2, "r", encoding="utf-8") as file:
    text_2 = file.read()

def compare_algorithms(string, pattern):
  times = []

  times.append(("Алгоритм Кнута-Морріса-Пратта", timeit.timeit(lambda: kmp_search(string, pattern), number=1)))

  times.append(("Алгоритм Боєра-Мура", timeit.timeit(lambda: boyer_moore_search(string, pattern), number=1)))

  times.append(("Алгоритм Рабіна-Карпа", timeit.timeit(lambda: rabin_karp_search(string, pattern), number=1)))

  print("Searching algorithms ranked by time:")
  for algo, time_taken in times:
      print(f"{algo}: {time_taken:.6f} seconds")


if __name__ == "__main__":
  print('------------------test data 1-----------------------')
  compare_algorithms(text_1, pattern)
  print('------------------test data 2-----------------------')
  compare_algorithms(text_2, pattern)
