# main.py

from menu_data import menus
from recommender import recommend_top_n

def get_valid_input(prompt, valid_options):
    while True:
        value = input(prompt).strip().lower()
        if value in valid_options:
            return value
        print(f"Input tidak valid. Pilihan: {', '.join(valid_options)}")
def main():
    user_pref = get_user_input()
    try:
        top_menus = recommend_top_n(menus, user_pref, n=3)
    except Exception as e:
        import traceback
        print("Terjadi error saat merekomendasikan menu:")
        traceback.print_exc()
        return

    print("\n=== TOP 3 REKOMENDASI MENU ===")

    for idx, item in enumerate(top_menus, start=1):
        menu = item["menu"]
        score = item["score"]
        reasons = item["reasons"]

        print(f"\n#{idx}")
        print(f"Menu   : {menu['name']}")
        print(f"Harga  : Rp{menu['price']}")
        print(f"Skor   : {score}")
        print("Alasan :")
        for reason in reasons:
            print(f" - {reason}")

def get_user_input():
    print("=== MENU RECOMMENDATION SYSTEM ===")

    time = get_valid_input(
        "Waktu makan (siang/malam): ",
        ["siang", "malam"]
    )

    spice = get_valid_input(
        "Preferensi rasa (tidak_pedas/sedang/pedas): ",
        ["tidak_pedas", "sedang", "pedas"]
    )

    budget = get_valid_input(
        "Budget (low/medium/high): ",
        ["low", "medium", "high"]
    )

    return {
        "time": time,
        "spice": spice,
        "budget": budget
    }
if __name__ == "__main__":
    main()