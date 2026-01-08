# recommender.py

def budget_level(price):
    if price <= 18000:
        return "low"
    elif price <= 23000:
        return "medium"
    else:
        return "high"


def calculate_score(menu, user_pref):
    score = 0
    reasons = []

    # Waktu makan
    if user_pref["time"] in menu["available_time"]:
        score += 3
        reasons.append("Cocok untuk waktu makan")

    # Preferensi rasa
    if user_pref["spice"] == menu["spice"]:
        score += 3
        reasons.append("Sesuai preferensi rasa")

    # Budget
    if user_pref["budget"] == budget_level(menu["price"]):
        score += 4
        reasons.append("Sesuai budget")

    # Popularitas
    if menu["sold_count"] >= 150:
        score += 2
        reasons.append("Menu populer")
    elif menu["sold_count"] >= 100:
        score += 1
        reasons.append("Cukup populer")

    return score, reasons


def recommend_top_n(menus, user_pref, n=3):
    scored_menus = []

    for menu in menus:
        score, reasons = calculate_score(menu, user_pref)
        scored_menus.append({
            "menu": menu,
            "score": score,
            "reasons": reasons
        })

    # Urutkan dari skor tertinggi
    scored_menus.sort(key=lambda x: x["score"], reverse=True)

    return scored_menus[:n]
