from markupsafe import escape, Markup

CQ1_CHOICES = [(0, '0$'), (50, '0.50$'), (100, '1.00$'), (150, '1.50$')]
CQ2_CHOICES = [(0, '0$'), (50, '0.50$'), (100, '1.00$'), (150, '1.50$')]

REVEAL_CHOICES = [(True, Markup('Я  хочу узнать ответ участника Б')),
                  (False, 'Я не хочу узнать ответ участника Б')]
OPINION_CHOICES = [(True, 'Согласен/согласна'), (False, 'Не согласен/не согласна'), ]
AGE_CHOICES = ["Младше 18 лет",
               "18-24 года",
               "25-34 года",
               "35-44 года",
               "45-54 года",
               "55-64 года",
               "65 лет и старше",
               ]

EDUCATION_CHOICES = [
    'Средняя школа',
    'Среднее профессиональное образование',
    'Незаконченное высшее образование',
    'Высшее образование',
    'Два и более диплома / Ученая степень']

GENDER_CHOICES = [
    "Мужской",
    "Женский",

]

MARITAL_CHOICES = ['Не женаты/не замужем',
                   'Женаты/замужем',
                   'В отношениях, но официально не состоите в браке',
                   'Разведены',
                   'Живете отдельно от супруга/и',
                   'Вдовец/Вдова']
EMPLOYMENT_CHOICES = [
    "Трудоустроен (полный рабочий день)",
    "Трудоустроен (частичная занятость)",
    "Самозанятый",
    "Не работаю и ищу работу",
    "Не работаю (на пенсии)",
    "Не работаю (по состоянию здоровья)",
    'Не работаю (другое)',
    "Предпочитаю не отвечать",
]
INCOME_CHOICES = [
    'Не хватает денег даже на еду',
    'Хватает на еду, но не хватает на покупку одежды и обуви',
    'Хватает на одежду и обувь, но не хватает на покупку мелкой бытовой техники',

    'Хватает денег на небольшие покупки, но покупка дорогих вещей (компьютера, стиральной машины, холодильника) требует накоплений или кредита',

    'Хватает денег на покупки для дома, но на покупку машины, дачи, квартиры необходимо копить или брать кредит',
    'Можем позволить себе любые покупки без ограничений и кредитов']

RISK_CHOICES = range(0, 11)


agreement_choices_5DNK = [
    [1, 'Совершенно не согласен'],
    [2, 'Скорее не согласен'],
    [3, 'Ни согласен, ни не согласен'],
    [4, 'Скорее согласен'],
    [5, 'Полностью согласен'],
    HARD_TO_SAY_CHOICE
]
