# Проект FitLife - MVP версия 1.0
import sys

sys.stdout.reconfigure(encoding="utf-8")
# исправление проблемы с тестом 6(output был NoneType)

WATER_PER_KG = 30  # рекомендуемый объём воды на килограмм веса
ML_PER_LITER = 1000
# 1. Знакомство
user_name = input("Приветствую! Как я могу к вам обращаться? ")
user_age = int(input("Сколько вам лет? "))


# 2. Сбор данных
user_weight = float(input("Укажите пожалуйста свой вес(в килограммах) "))
user_height = float(input("Укажите ваш рост в метрах(например 1.75) "))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
# расчёт количества воды
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_LITER


# 4. Вывод красивого результата
print("-" * 40)
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {round(bmi, 1)}")
print(f"Рекомендуемая норма воды: {water_l:.2f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
