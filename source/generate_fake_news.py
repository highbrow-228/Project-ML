import os
import random
import time

import pandas as pd
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_google_genai import ChatGoogleGenerativeAI


# Завантажуємо .env файл
load_dotenv()

# Ініціалізація змінних:
api_key = os.getenv("GEMINI_API_KEY_YURII_2")
n = 5_500
delay = 15

tones = ["Нейтральна", "Тривожна", "Заспокійлива"]
styles = ["Суха подача", "Драматична", "Аналітична", "Іронічна", "Популістська", "Фактологічна"]
type_of_news = ["Маніпуляція", "Дезінформація", "Пропаганда", "Вплив через емоції",]
topics = ["Політика", "Економіка", "Суспільство", "Військові події", "Освіта", "Місцеве самоврядування", "Зовнішня політика", "Енергетика", "Інфраструктура", "Охорона здоров'я", "Культура", "Довкілля"]

# System message
system_message = """Ви — досвідчений журналіст із понад 10 роками роботи в провідних українських та міжнародних медіа.
Ваші тексти вирізняються глибиною аналізу, структурованістю та дотриманням високих стандартів журналістики.
Ви володієте майстерністю фактчекінгу, балансу думок і доступного викладу складних тем.\
"""

# Human message
human_message_template = """Згенеруй **фейкову, але правдоподібну** новину у стилі провідних українських медіа 2022–2025 років. \

### **Контекст подачі:**
- Тональність: {tone}
- Стиль: {style}
- Тип: {type_of_news}
- Тематика: {topics}

---

### Вимоги до тексту:
- **Почни з головного** — подія, її суть, причетні особи або інституції.
- Пиши **доступною, живою мовою** — без офіціозу, штампів чи технократичного жаргону.
- Стиль має бути **максимально реалістичним**, у форматі репортажу або аналітичної замітки.
- Включай **реальні імена посадовців, державних установ і фактів** (у межах 2022–2025 рр.).
- Додай **коментарі експертів або посадових осіб** — вигадані, але переконливі.
- **Не вигадуй географічних назв**, не використовуй очевидні кліше чи фантастичні події.
- Орієнтуйся на стиль **«Української правди», «bihus.info», «ТСН»** — стриманий, динамічний, фактологічний.

---

# ВИВІД МАЄ БУТИ У ФОРМАТІ:
{format_of_output}
"""

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=api_key,
    temperature=0.8,
    max_retries=2,
    top_p=0.9,
    top_k=40,
)


# Ініціалізація моделі виводу
class OutputModel(BaseModel):
    title: str = Field(description="Заголовок новини")
    text: str = Field(description="Текст новини (300-500 слів)")


parser = JsonOutputParser(pydantic_object=OutputModel)

# Генерація новини
def generate_one_news():
    prompt = ChatPromptTemplate(
        [
            ("system", system_message),
            ("human", human_message_template)
        ]
    )

    chain = prompt | llm | parser

    # Рандомно вибираємо тон, стиль, тип новин
    tone = random.choice(tones)
    style = random.choice(styles)
    type = random.choice(type_of_news)
    topic = random.choice(topics)

    input_data = {
        "tone": tone,
        "style": style,
        "type_of_news": type,
        "topics": topic,
        "format_of_output": parser.get_format_instructions()
    }

    # Запускаємо модель
    if isinstance(llm, OllamaLLM):
        return chain.invoke(input_data)['properties']
    else:
        return chain.invoke(input_data)

# додавання до датасету
def append_to_csv(news, path= "..//data//fake_news_template.csv"):
    df = pd.DataFrame(
        [
            {
                "title": news['title'],
                "text": news['text'],
            }
        ]
    )

    if not os.path.exists(path):
        df.to_csv(path, index=False, encoding="utf-8")
    else:
        df.to_csv(path, mode="a", index=False, header=False, encoding="utf-8")


for i in range(n):
    current_time = time.strftime("%H:%M:%S")

    try:
        news = generate_one_news()
        print(f"[{current_time}][{i+1}/{n}] {news['title']}")
    except OutputParserException as e:
        print(f"[{current_time}][{i+1}/{n}] ❌ ПОМИЛКА ПАРСИНГУ: {e}")
    except Exception as e:
        if "429" in str(e):
            print(f"[{current_time}][{i+1}/{n}] ❌ Ліміт запитів. Очікування 15 хвилин...")
            time.sleep(900)  # 15 хвилин очікування
            n += 1
            continue  # повторимо ітерацію
        else:
            print(f"[{current_time}][{i+1}/{n}] ❌ Інша помилка: {e}")


    append_to_csv(news)
    time.sleep(delay)

print(f"\n Згенеровано {n} новин. Результати збережено.")