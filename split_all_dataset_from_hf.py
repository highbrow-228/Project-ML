from datasets import load_dataset
import pandas as pd
from itertools import islice
import gc  # Для очищення пам'яті

# Завантажуємо датасет
dataset = load_dataset("zeusfsx/ukrainian-news")
train_data = dataset["train"]

total_rows = len(train_data)
print("Total rows is", total_rows)

batch_size = 1_000_000  # Кількість записів які повинні бути в 1 файлі
file_index = 1  # Індекс файлу
processed_rows = 0

# train_data -> ітератор
train_data_iter = iter(train_data)

# Проходимо по датасету і зберігаємо по batch_size рядків у csv
while processed_rows < total_rows:
    # Витягуємо партію даних
    batch = list(
        islice(
            train_data_iter,
            batch_size
        )
    )

    # Якщо партія пуста, ліваємо
    if not batch:
        break

    df = pd.DataFrame(batch)

    filename = f"data/news_part_{file_index}.csv"
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Збережено {filename}")

    # Оновлюємо кількість оброблених рядків
    processed_rows += len(batch)

    # Виводимо скільки ще рядків потрібно зберегти
    remaining_rows = total_rows - processed_rows
    print(f"Залишилось зберегти {remaining_rows} рядків.")

    # Оновлюємо індекс файлу
    file_index += 1

    # Очищення пам'яті
    del df
    del batch
    gc.collect()

print("Процес завершено. Всі дані збережено.")