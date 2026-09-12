import os
import time
from google import genai
from dotenv import load_dotenv

# .env faylindaki GEMINI_API_KEY-i mühit dəyişəninə yükləyir.
load_dotenv()


# === 1. DEKORATOR (API LOG SİSTEMİ) ===
def log_api_call(func):
    """API çağırışının müddətini ölçür və loqlaşdırır."""

    def wrapper(*args, **kwargs):
        print("\n⚡ [SYSTEM LOG] Gemini API ilə əlaqə qurulur... Zəhmət olmasa gözləyin...")
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        duration = end_time - start_time
        print(f"✅ [SYSTEM LOG] Cavab alındı! API Cavab Müddəti: {duration:.2f} saniyə.")
        return result

    return wrapper


# === 2. LLM API FUNKSİYASI ===
@log_api_call
def generate_travel_plan(city, days, budget, style, tags):
    # NOT: "YOUR_GEMINI_API_KEY" yazılan yerə öz real API açarını qoymalısan
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY", ""))

    prompt = f"""
    Sən professional bir AI Səyahət Bələdçisisən. Aşağıdakı parametrlərə uyğun olaraq səyahət planı hazırlamalısan:
    - Şəhər: {city}
    - Müddət: {days} gün
    - Ümumi Büdcə: {budget} USD
    - Səyahət Tərzi: {style}
    - Üstünlük verilən kateqoriyalar: {', '.join(tags)}

    MÜTLƏQ TƏLƏBLƏR:
    1. Cavab tamamilə Azərbaycan dilində və Markdown formatında olmalıdır.
    2. GÜNBƏGÜN MARŞRUT: Hər gün üçün ayrıca başlıq aç (məs: **Gün 1: ...**) və səhər, günorta, axşam gəziləcək yerləri, yeməkləri yaz.
    3. OTEL TÖVSİYƏLƏRİ: Həmin şəhərdə, gəziləcək yerlərin mərkəzinə yaxın yerləşən real və populyar 3 otel tövsiyəsi ver:
       - 1 dənə Ekonom otel/hostel (Təxmini gecəlik qiyməti ilə)
       - 1 dənə Orta səviyyəli otel (Təxmini gecəlik qiyməti ilə)
       - 1 dənə Lüks otel (Təxmini gecəlik qiyməti ilə)
       (Qeyd: Otellərin Booking-də tapıla bilən real adlar olmasına diqqət et).
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"❌ API ilə əlaqə zamanı xəta baş verdi: {e}"


# === MAIN PROQRAM ===
def main():
    print("==================================================")
    print("🌍 RoamPulse: Advanced AI Səyahət Planlayıcısı 🌍")
    print("==================================================\n")

    # Validation (Yoxlama)
    city = input("Gedəcəyiniz şəhəri daxil edin (məs: Paris): ").strip()
    if not city:
        print("❌ Xəta: Şəhər adı boş ola bilməz!")
        return

    days_input = input("Səyahət neçə gün çəkəcək?: ").strip()
    budget_input = input("Ümumi büdcənizi daxil edin (USD): ").strip()

    if not days_input.isdigit() or not budget_input.isdigit():
        print("❌ Xəta: Gün və büdcə yalnız müsbət ədəd olmalıdır!")
        return

    days = int(days_input)
    budget = float(budget_input)

    if days <= 0 or budget <= 0:
        print("❌ Xəta: Gün və büdcə 0-dan böyük olmalıdır!")
        return

    travel_style = input("Səyahət tərzi (Ekonom / Orta / Lüks): ").strip().capitalize()

    # 3. MƏLUMAT STRUKTURLARI VƏ SEÇİMLƏR
    print("\n--- Səyahət Maraqları ---")
    available_activities = {
        1: "Tarixi məkanlar və Muzeylər",
        2: "Təbiət yürüşləri və Parklar",
        3: "Yerli mətbəx (Qastro-turizm)",
        4: "Gecə həyatı və Əyləncə",
        5: "Alış-veriş (Shopping)"
    }

    for key, val in available_activities.items():
        print(f"{key}. {val}")

    user_choices = input("\nMaraqlandığınız sahələrin nömrələrini vergüllə daxil edin (məs: 1,3): ")
    selected_indices = [int(x.strip()) for x in user_choices.split(",") if x.strip().isdigit()]

    chosen_labels = []
    for index in selected_indices:
        if index in available_activities:
            chosen_labels.append(available_activities[index])

    # SET ilə Filtirləmə
    all_tags = {"history", "nature", "gastronomy", "nightlife", "shopping"}
    blacklist = set()
    no_thanks = input(
        "\nSəyahətdə QƏTİYYƏN olmasını İSTƏMƏDİYİNİZ mövzu (history/nature/nightlife/shopping və ya yox): ").strip().lower()
    if no_thanks != "yox" and no_thanks in all_tags:
        blacklist.add(no_thanks)

    final_tags = all_tags.difference(blacklist)

    # REZULTAT ANALİTİKASI (BÜDCƏ BÖLGÜSÜ)
    daily_budget = budget / days
    print("\n📊 TƏXMİNİ BÜDCƏ ANALİZİ:")
    print(f"|-- Günlük xərcləmə limiti: $ {daily_budget:.2f}")
    print(f"|-- 🏠 Otel və Qalmaq üçün (40%): $ {budget * 0.40:.2f}")
    print(f"|-- 🍔 Yemək və Restoranlar üçün (30%): $ {budget * 0.30:.2f}")
    print(f"|-- 🎟️ Muzeylər və Nəqliyyat üçün (30%): $ {budget * 0.30:.2f}")

    # API ÇAĞIRIŞI
    ai_plan = generate_travel_plan(city, days, budget, travel_style, final_tags)

    print("\n" + "=" * 50)
    print("✨ SÜNİ İNTELLEKTİN REALLAŞDIRDIĞI SƏYAHƏT PLANI VƏ OTƏLLƏR ✨")
    print("=" * 50)
    print(ai_plan)
    print("=" * 50)

    # FAYLA YAZMA (EXPORT SYSTEM)
    file_name = f"{city.replace(' ', '_')}_{days}_gunluk_plan.txt"
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(ai_plan)
        print(f"\n💾 Səyahət planınız fayla uğurla qeyd olundu: {file_name}")
    except Exception as e:
        print(f"❌ Fayla yazarkən xəta: {e}")


if __name__ == "__main__":
    main()

    import requests


    def send_to_n8n(city, plan_text):
        # n8n-dən kopyaladığın Webhook URL-ini bura yapışdır
        n8n_url = "http://localhost:5678/webhook-test/http://localhost:5678/webhook-test/trip-planner"

        payload = {
            "city": city,
            "travel_plan": plan_text
        }

        try:
            response = requests.post(n8n_url, json=payload)
            if response.status_code == 200:
                print("🚀 Data uğurla n8n workflow-una göndərildi!")
            else:
                print(f"⚠️ n8n cavab vermədi, Status kod: {response.status_code}")
        except Exception as e:
            print(f"❌ n8n ilə bağlantı xətası: {e}")

    # Bunu main() funksiyasının ən sonuna əlavə et:
    # send_to_n8n(city, ai_plan)
