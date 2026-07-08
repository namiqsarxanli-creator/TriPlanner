import os
import time
from google import genai


# === 1. DEKORATOR (API LOG SÄ°STEMÄ°) ===
def log_api_call(func):
    """API Ã§aÄŸÄ±rÄ±ÅŸÄ±nÄ±n mÃ¼ddÉ™tini Ã¶lÃ§Ã¼r vÉ™ loqlaÅŸdÄ±rÄ±r."""

    def wrapper(*args, **kwargs):
        print("\nâš¡ [SYSTEM LOG] Gemini API ilÉ™ É™laqÉ™ qurulur... ZÉ™hmÉ™t olmasa gÃ¶zlÉ™yin...")
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        duration = end_time - start_time
        print(f"âœ… [SYSTEM LOG] Cavab alÄ±ndÄ±! API Cavab MÃ¼ddÉ™ti: {duration:.2f} saniyÉ™.")
        return result

    return wrapper


# === 2. LLM API FUNKSÄ°YASI ===
@log_api_call
def generate_travel_plan(city, days, budget, style, tags):
    # NOT: "YOUR_GEMINI_API_KEY" yazÄ±lan yerÉ™ Ã¶z real API aÃ§arÄ±nÄ± qoymalÄ±san
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY", ""))

    prompt = f"""
    SÉ™n professional bir AI SÉ™yahÉ™t BÉ™lÉ™dÃ§isisÉ™n. AÅŸaÄŸÄ±dakÄ± parametrlÉ™rÉ™ uyÄŸun olaraq sÉ™yahÉ™t planÄ± hazÄ±rlamalÄ±san:
    - ÅžÉ™hÉ™r: {city}
    - MÃ¼ddÉ™t: {days} gÃ¼n
    - Ãœmumi BÃ¼dcÉ™: {budget} USD
    - SÉ™yahÉ™t TÉ™rzi: {style}
    - ÃœstÃ¼nlÃ¼k verilÉ™n kateqoriyalar: {', '.join(tags)}

    MÃœTLÆQ TÆLÆBLÆR:
    1. Cavab tamamilÉ™ AzÉ™rbaycan dilindÉ™ vÉ™ Markdown formatÄ±nda olmalÄ±dÄ±r.
    2. GÃœNBÆGÃœN MARÅžRUT: HÉ™r gÃ¼n Ã¼Ã§Ã¼n ayrÄ±ca baÅŸlÄ±q aÃ§ (mÉ™s: **GÃ¼n 1: ...**) vÉ™ sÉ™hÉ™r, gÃ¼norta, axÅŸam gÉ™zilÉ™cÉ™k yerlÉ™ri, yemÉ™klÉ™ri yaz.
    3. OTEL TÃ–VSÄ°YÆLÆRÄ°: HÉ™min ÅŸÉ™hÉ™rdÉ™, gÉ™zilÉ™cÉ™k yerlÉ™rin mÉ™rkÉ™zinÉ™ yaxÄ±n yerlÉ™ÅŸÉ™n real vÉ™ populyar 3 otel tÃ¶vsiyÉ™si ver:
       - 1 dÉ™nÉ™ Ekonom otel/hostel (TÉ™xmini gecÉ™lik qiymÉ™ti ilÉ™)
       - 1 dÉ™nÉ™ Orta sÉ™viyyÉ™li otel (TÉ™xmini gecÉ™lik qiymÉ™ti ilÉ™)
       - 1 dÉ™nÉ™ LÃ¼ks otel (TÉ™xmini gecÉ™lik qiymÉ™ti ilÉ™)
       (Qeyd: OtellÉ™rin Booking-dÉ™ tapÄ±la bilÉ™n real adlar olmasÄ±na diqqÉ™t et).
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"âŒ API ilÉ™ É™laqÉ™ zamanÄ± xÉ™ta baÅŸ verdi: {e}"


# === MAIN PROQRAM ===
def main():
    print("==================================================")
    print("ðŸŒ RoamPulse: Advanced AI SÉ™yahÉ™t PlanlayÄ±cÄ±sÄ± ðŸŒ")
    print("==================================================\n")

    # Validation (Yoxlama)
    city = input("GedÉ™cÉ™yiniz ÅŸÉ™hÉ™ri daxil edin (mÉ™s: Paris): ").strip()
    if not city:
        print("âŒ XÉ™ta: ÅžÉ™hÉ™r adÄ± boÅŸ ola bilmÉ™z!")
        return

    days_input = input("SÉ™yahÉ™t neÃ§É™ gÃ¼n Ã§É™kÉ™cÉ™k?: ").strip()
    budget_input = input("Ãœmumi bÃ¼dcÉ™nizi daxil edin (USD): ").strip()

    if not days_input.isdigit() or not budget_input.isdigit():
        print("âŒ XÉ™ta: GÃ¼n vÉ™ bÃ¼dcÉ™ yalnÄ±z mÃ¼sbÉ™t É™dÉ™d olmalÄ±dÄ±r!")
        return

    days = int(days_input)
    budget = float(budget_input)

    if days <= 0 or budget <= 0:
        print("âŒ XÉ™ta: GÃ¼n vÉ™ bÃ¼dcÉ™ 0-dan bÃ¶yÃ¼k olmalÄ±dÄ±r!")
        return

    travel_style = input("SÉ™yahÉ™t tÉ™rzi (Ekonom / Orta / LÃ¼ks): ").strip().capitalize()

    # 3. MÆLUMAT STRUKTURLARI VÆ SEÃ‡Ä°MLÆR
    print("\n--- SÉ™yahÉ™t MaraqlarÄ± ---")
    available_activities = {
        1: "Tarixi mÉ™kanlar vÉ™ MuzeylÉ™r",
        2: "TÉ™biÉ™t yÃ¼rÃ¼ÅŸlÉ™ri vÉ™ Parklar",
        3: "Yerli mÉ™tbÉ™x (Qastro-turizm)",
        4: "GecÉ™ hÉ™yatÄ± vÉ™ ÆylÉ™ncÉ™",
        5: "AlÄ±ÅŸ-veriÅŸ (Shopping)"
    }

    for key, val in available_activities.items():
        print(f"{key}. {val}")

    user_choices = input("\nMaraqlandÄ±ÄŸÄ±nÄ±z sahÉ™lÉ™rin nÃ¶mrÉ™lÉ™rini vergÃ¼llÉ™ daxil edin (mÉ™s: 1,3): ")
    selected_indices = [int(x.strip()) for x in user_choices.split(",") if x.strip().isdigit()]

    chosen_labels = []
    for index in selected_indices:
        if index in available_activities:
            chosen_labels.append(available_activities[index])

    # SET ilÉ™ FiltirlÉ™mÉ™
    all_tags = {"history", "nature", "gastronomy", "nightlife", "shopping"}
    blacklist = set()
    no_thanks = input(
        "\nSÉ™yahÉ™tdÉ™ QÆTÄ°YYÆN olmasÄ±nÄ± Ä°STÆMÆDÄ°YÄ°NÄ°Z mÃ¶vzu (history/nature/nightlife/shopping vÉ™ ya yox): ").strip().lower()
    if no_thanks != "yox" and no_thanks in all_tags:
        blacklist.add(no_thanks)

    final_tags = all_tags.difference(blacklist)

    # REZULTAT ANALÄ°TÄ°KASI (BÃœDCÆ BÃ–LGÃœSÃœ)
    daily_budget = budget / days
    print("\nðŸ“Š TÆXMÄ°NÄ° BÃœDCÆ ANALÄ°ZÄ°:")
    print(f"|-- GÃ¼nlÃ¼k xÉ™rclÉ™mÉ™ limiti: $ {daily_budget:.2f}")
    print(f"|-- ðŸ  Otel vÉ™ Qalmaq Ã¼Ã§Ã¼n (40%): $ {budget * 0.40:.2f}")
    print(f"|-- ðŸ” YemÉ™k vÉ™ Restoranlar Ã¼Ã§Ã¼n (30%): $ {budget * 0.30:.2f}")
    print(f"|-- ðŸŽŸï¸ MuzeylÉ™r vÉ™ NÉ™qliyyat Ã¼Ã§Ã¼n (30%): $ {budget * 0.30:.2f}")

    # API Ã‡AÄžIRIÅžI
    ai_plan = generate_travel_plan(city, days, budget, travel_style, final_tags)

    print("\n" + "=" * 50)
    print("âœ¨ SÃœNÄ° Ä°NTELLEKTÄ°N REALLAÅžDIRDIÄžI SÆYAHÆT PLANI VÆ OTÆLLÆR âœ¨")
    print("=" * 50)
    print(ai_plan)
    print("=" * 50)

    # FAYLA YAZMA (EXPORT SYSTEM)
    file_name = f"{city.replace(' ', '_')}_{days}_gunluk_plan.txt"
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(ai_plan)
        print(f"\nðŸ’¾ SÉ™yahÉ™t planÄ±nÄ±z fayla uÄŸurla qeyd olundu: {file_name}")
    except Exception as e:
        print(f"âŒ Fayla yazarkÉ™n xÉ™ta: {e}")


if __name__ == "__main__":
    main()

    import requests


    def send_to_n8n(city, plan_text):
        # n8n-dÉ™n kopyaladÄ±ÄŸÄ±n Webhook URL-ini bura yapÄ±ÅŸdÄ±r
        n8n_url = "http://localhost:5678/webhook-test/http://localhost:5678/webhook-test/trip-planner"

        payload = {
            "city": city,
            "travel_plan": plan_text
        }

        try:
            response = requests.post(n8n_url, json=payload)
            if response.status_code == 200:
                print("ðŸš€ Data uÄŸurla n8n workflow-una gÃ¶ndÉ™rildi!")
            else:
                print(f"âš ï¸ n8n cavab vermÉ™di, Status kod: {response.status_code}")
        except Exception as e:
            print(f"âŒ n8n ilÉ™ baÄŸlantÄ± xÉ™tasÄ±: {e}")

    # Bunu main() funksiyasÄ±nÄ±n É™n sonuna É™lavÉ™ et:
    # send_to_n8n(city, ai_plan)
