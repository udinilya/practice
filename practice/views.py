from django.shortcuts import render


def index(request):
    plans = [
        {
            "name": "Бесплатно",
            "price": "0",
            "options": {"users": 10, "space": 10, "support": "Почтовая рассылка"},
        },
        {
            "name": "Профессиональный",
            "price": "49",
            "options": {"users": 50, "space": 100, "support": "Телефон и email"},
        },
        {
            "name": "Корпоративный",
            "price": "99",
            "options": {"users": 100, "space": 500, "support": "Персональный менеджер"},
        },
    ]

    return render(request, 'index.html', {'plans': plans})


def plans(request):
    plans = [
        {
            "name": "Бесплатно",
            "price": "0",
            "options": {"users": 10, "space": 10, "support": "Почтовая рассылка"},
        },
        {
            "name": "Профессиональный",
            "price": "49",
            "options": {"users": 50, "space": 100, "support": "Телефон и email"},
        },
        {
            "name": "Корпоративный",
            "price": "99",
            "options": {"users": 100, "space": 500, "support": "Персональный менеджер"},
        },
    ]

    return render(request, 'plans.html', {'plans': plans})
