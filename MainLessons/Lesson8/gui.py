import streamlit as st
from google import genai
import requests
import datetime
import os
import time
from functools import wraps
from urllib.parse import quote
from dotenv import load_dotenv
import io
from fpdf import FPDF
import urllib.request

ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path=ENV_PATH)


def get_secret(key: str, default: str = "") -> str:
    value = os.getenv(key, "")
    if value:
        return value
    try:
        return st.secrets.get(key, default)
    except Exception:
        return default


st.set_page_config(page_title="CompassAI", page_icon="✈️", layout="wide")


def inject_luxury_theme():
    """
    CompassAI EXPLORER — LÜKS DİZAYN MODULU (YENİLƏNMİŞ)
    Arxa fondakı naxışların brauzerdə dəqiq görünməsi üçün SVG kodu CSS-ə uyğun optimizasiya edildi.
    """
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght=500;700;900&family=Poppins:wght=300;400;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            letter-spacing: 0.5px;
        }

        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        .main {
            background-color: #0b1120 !important;
            background-image:
                linear-gradient(180deg, rgba(11,17,32,0.88) 0%, rgba(15,23,42,0.93) 100%),
                url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='700' height='420' viewBox='0 0 700 420'%3E%3Cg fill='none' stroke='%23c9a24a' stroke-width='1.7' opacity='0.32' stroke-linejoin='round' stroke-linecap='round'%3E%3C!-- Eyfel qulesi --%3E%3Cpath d='M60 380 L95 150 L105 150 L140 380 M68 300 L132 300 M75 240 L125 240 M95 150 L95 110 L105 110 L105 150 M100 110 L100 85'/%3E%3C!-- Misir piramidasi --%3E%3Cpath d='M195 380 L245 240 L295 380 Z M210 380 L280 380'/%3E%3C!-- Big Ben qullesi --%3E%3Cpath d='M355 380 L355 190 Q355 165 380 165 Q405 165 405 190 L405 380 M345 380 L415 380 M365 200 L395 200 M365 230 L395 230 M365 260 L395 260 M370 165 L370 145 L390 145 L390 165'/%3E%3C!-- Tac Mahal gunbezi --%3E%3Cpath d='M465 380 L465 280 Q465 225 505 210 Q545 225 545 280 L545 380 M450 380 L560 380 M505 210 L505 185 M495 185 L515 185 M475 300 L475 380 M535 300 L535 380'/%3E%3C!-- Pagoda --%3E%3Cpath d='M600 380 L600 320 M575 320 L625 320 M580 300 L620 300 L600 275 Z M585 270 L615 270 L600 250 Z M568 330 L632 330'/%3E%3C/g%3E%3C/svg%3E") !important;
            background-repeat: no-repeat, repeat !important;
            background-size: cover, 700px 420px !important;
            background-position: center top, 0 0 !important;
            background-attachment: fixed, fixed !important;
        }

        [data-testid="stHeader"] {
            background-color: transparent !important;
        }

        .main-title {
            background: linear-gradient(45deg, #c9a24a, #f4e4bc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 42px; font-weight: 700; text-align: center; margin-bottom: 5px;
            text-shadow: 0 0 18px rgba(201,162,74,0.25);
        }
        .subtitle-text { text-align: center; color: #b8b2a3; font-size: 16px; margin-bottom: 10px; }

        h2, h3, p, label, span, div { color: #e8e4da; }

        .animated-card, .mobile-form-card {
            background: rgba(255,255,255,0.04);
            padding: 25px; border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.4); margin-bottom: 25px;
            border: 1px solid rgba(201,162,74,0.3);
            backdrop-filter: blur(10px);
        }

        div[data-testid="stForm"] {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(201,162,74,0.35);
            border-radius: 16px;
            backdrop-filter: blur(10px);
        }

        .leg-badge {
            display: inline-block;
            background: linear-gradient(45deg, #c9a24a 0%, #e8c874 100%);
            color: #0b1120; font-weight: 700; padding: 4px 14px; border-radius: 999px;
            font-size: 13px; margin-bottom: 10px;
        }

        .stButton>button, .stFormSubmitButton > button, .stDownloadButton>button {
            background: linear-gradient(135deg, #c9a24a 0%, #e8c874 50%, #c9a24a 100%);
            color: #0b1120 !important; border: none; border-radius: 10px;
            padding: 12px 28px; font-size: 16px; font-weight: 600;
            letter-spacing: 0.5px; transition: all 0.2s ease;
            box-shadow: 0 4px 14px rgba(201,162,74,0.3);
        }
        .stButton>button:hover, .stFormSubmitButton > button:hover, .stDownloadButton>button:hover {
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 8px 22px rgba(201,162,74,0.5);
        }

        .status-box { padding: 15px; border-radius: 10px; font-weight: 600; text-align: center; margin-bottom: 15px; }

        .bounce-card {
            display: flex; align-items: center; gap: 14px; padding: 18px 22px;
            border-radius: 14px; font-weight: 700; font-size: 17px; height: 100%;
        }
        .bounce-emoji { font-size: 42px; display: inline-block; animation: bounce 1.4s ease-in-out infinite; }
        @keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }

        .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"],
        .stDateInput input, .stTextArea textarea {
            background-color: rgba(255,255,255,0.06) !important;
            color: #f4e4bc !important;
            border: 1px solid rgba(201,162,74,0.4) !important;
            border-radius: 8px !important;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f172a 0%, #0b1120 100%);
            border-right: 1px solid rgba(201,162,74,0.25);
        }

        div[data-testid="stMetric"] {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(201,162,74,0.25);
            border-radius: 12px; padding: 12px;
        }

        .chat-container {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(201,162,74,0.2);
            border-radius: 12px; padding: 10px; margin-top: 15px;
            max-height: 350px; overflow-y: auto;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_luxury_theme()

DEFAULT_API_KEY = get_secret("GEMINI_API_KEY")

LANG_DICT = {
    "AZ": {
        "title": "✈️ CompassAI",
        "subtitle": "Səyahət planınızı yaradın, canlı hava durumunu və otelləri anında saytda görün!",
        "settings": "⚙️ Tənzimləmələr",
        "options": "📋 Səyahət Parametrləri",
        "multi_city_title": "🗺️ Marşrut (Şəhərlər)",
        "leg_city": "Şəhər",
        "leg_days": "Gün",
        "add_city": "➕ Şəhər əlavə et",
        "remove_leg": "🗑️",
        "total_days_label": "🧮 Ümumi Müddət",
        "days_word": "gün",
        "city_placeholder": "Məs: Paris, Tokyo, Roma",
        "date": "📅 Səyahətin Başlama Tarixi",
        "budget": "💰 Ümumi Büdcə (USD)",
        "style": "🎭 Səyahət Tərzi",
        "style_opt": ["Ekonom", "Orta", "Lüks"],
        "interests": "🎯 Maraq Dairəsi",
        "int_museums": "Tarix və Muzeylər",
        "int_nature": "Təbiət və Parklar",
        "int_food": "Yerli Mətbəx",
        "int_night": "Gecə Həyatı",
        "format": "📋 Hesabat Növü",
        "format_opt": ["Detallı Plan", "Qısa Xülasə"],
        "btn_start": "🚀 Səyahət Planını Hazırla",
        "photo_cap": "📸 Möhtəşəm Məkan",
        "weather_title": "☀️ Canlı Hava Vəziyyəti",
        "weather_high": "Gözlənilən Ən Yüksək",
        "weather_low": "Gözlənilən Ən Aşağı",
        "weather_no_forecast": "ℹ️ Bu tarix üçün anlıq proqnoz yoxdur, mövsümi rejim aktivdir.",
        "geo_not_found": "🧭 Point Me uğursuz oldu! Bu şəhər tapılmadı, adı yoxlayıb yenidən cəhd edin.",
        "budget_title": "📊 Günlük Təxmini Büdcə Bölgüsü (Ümumi)",
        "hotel": "🏨 Otel və Qalmaq",
        "food": "🍔 Yemək və Restoran",
        "transport": "🚗 Nəqliyyat və Əyləncə",
        "ai_title": "✨ Sizin Xüsusi Çoxşəhərli Səyahət Planınız",
        "btn_download": "📥 Planı Yüklə",
        "ai_error": "💥 Süni İntellekt xətti məşğuldur",
        "weather_delay": "⚠️ Hava məlumatlarında fasilə yarandı",
        "status_low": "🐣 Reparo! Büdcə EKONOMDUR — qənaətli tərzdə bərpa edildi.",
        "status_mid": "🎈 Wingardium Leviosa! Büdcə ORTADIR — balanslı və rahat uçuş.",
        "status_high": "🎉 Expecto Patronum! Büdcə YAXŞIDIR — lüks qoruyucunuz aktivdir.",
        "ai_role": "Sən enerjili və şən AI Səyahət Bələdçisisən. Azərbaycan dilində emojilərlə bol cavab ver.",
        "spinner_weather": "🛡️ Protego! Hava ruhları araşdırılır...",
        "spinner_ai": "🪄 Accio Marşrut! Planınız çağırılır...",
        "leg_of_trip": "Marşrut hissəsi",
        "api_key_not_found": "Gemini API key tapılmadı.",
        "currency_label": "💱 Valyuta",
        "azn_equivalent": "AZN-ə çevrilmiş",
        "rate_caption": "Məzənnə",
        "rate_error": "⚠️ Məzənnə tapılmadı.",
        "chat_header": "💬 Canlı Səyahət Bələdçiniz",
        "chat_placeholder": "Səyahət haqqında sual verin..."
    },
    "EN": {
        "title": "✈️ CompassAI",
        "subtitle": "Create your travel plan, see live weather and hotels instantly on the site!",
        "settings": "⚙️ Settings",
        "options": "📋 Travel Parameters",
        "multi_city_title": "🗺️ Route (Cities)",
        "leg_city": "City",
        "leg_days": "Days",
        "add_city": "➕ Add city",
        "remove_leg": "🗑️",
        "total_days_label": "🧮 Total Duration",
        "days_word": "days",
        "city_placeholder": "E.g.: Paris, Tokyo, Rome",
        "date": "📅 Trip Start Date",
        "budget": "💰 Total Budget (USD)",
        "style": "🎭 Travel Style",
        "style_opt": ["Budget", "Mid-range", "Luxury"],
        "interests": "🎯 Interests",
        "int_museums": "History & Museums",
        "int_nature": "Nature & Parks",
        "int_food": "Local Cuisine",
        "int_night": "Nightlife",
        "format": "📋 Report Type",
        "format_opt": ["Detailed Plan", "Short Summary"],
        "btn_start": "🚀 Prepare Travel Plan",
        "photo_cap": "📸 Amazing Destination",
        "weather_title": "☀️ Live Weather Conditions",
        "weather_high": "Expected Max",
        "weather_low": "Expected Min",
        "weather_no_forecast": "ℹ️ No live forecast for this date, seasonal mode is active.",
        "geo_not_found": "🧭 Point Me failed! City not found.",
        "budget_title": "📊 Estimated Daily Budget Allocation",
        "hotel": "🏨 Hotel & Stay",
        "food": "🍔 Food & Dining",
        "transport": "🚗 Transport & Leisure",
        "ai_title": "✨ Your Custom Multi-City Travel Plan",
        "btn_download": "📥 Download Plan",
        "ai_error": "💥 AI Line is busy",
        "weather_delay": "⚠️ Temporary delay in weather data",
        "status_low": "🐣 Reparo! Budget is BUDGET-FRIENDLY — patched up and thrifty.",
        "status_mid": "🎈 Wingardium Leviosa! Budget is MID-RANGE — a balanced flight.",
        "status_high": "🎉 Expecto Patronum! Budget is GREAT — your luxury shield is up.",
        "ai_role": "You are an AI Travel Guide. Provide response in English with emojis.",
        "spinner_weather": "🛡️ Protego! Scouting the weather spirits...",
        "spinner_ai": "🪄 Accio Route! Summoning your plan...",
        "leg_of_trip": "Trip leg",
        "api_key_not_found": "Gemini API key not found.",
        "currency_label": "💱 Currency",
        "azn_equivalent": "Converted to AZN",
        "rate_caption": "Exchange rate",
        "rate_error": "⚠️ Exchange rate not found.",
        "chat_header": "💬 Live Travel Assistant",
        "chat_placeholder": "Ask something about your trip..."
    }
}


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        if elapsed > 0.01:
            st.caption(f"⏱️ `{func.__name__}` → {elapsed:.2f}s")
        return result

    return wrapper


@measure_time
@st.cache_data(ttl=3600, show_spinner=False)
def get_coordinates(city_name: str):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={quote(city_name)}&count=1&language=en&format=json"
    resp = requests.get(geo_url, timeout=10)
    resp.raise_for_status()
    return resp.json()


@measure_time
@st.cache_data(ttl=1800, show_spinner=False)
def get_weather(lat: float, lon: float, date_str: str):
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
        f"&start_date={date_str}&end_date={date_str}"
    )
    resp = requests.get(weather_url, timeout=10)
    resp.raise_for_status()
    return resp.json()


CURRENCY_OPTIONS = ["USD", "EUR", "GBP", "AZN", "TRY", "RUB"]
CURRENCY_SYMBOLS = {"USD": "$", "EUR": "€", "GBP": "£", "AZN": "₼", "TRY": "₺", "RUB": "₽"}


@measure_time
@st.cache_data(ttl=3600, show_spinner=False)
def get_exchange_rate_to_azn(base_currency: str):
    if base_currency == "AZN":
        return 1.0
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data["rates"]["AZN"]


def fun_status_card(emoji: str, text: str, color: str, text_color: str = "#ffffff"):
    st.markdown(f"""
        <div class="bounce-card" style="background:{color}; color:{text_color};">
            <span class="bounce-emoji">{emoji}</span>
            <span>{text}</span>
        </div>
    """, unsafe_allow_html=True)


def seasonal_note(city_lower: str, travel_month: int):
    if "roma" in city_lower or "rome" in city_lower:
        if travel_month in [7, 8]:
            return True, "🔥 Aguamenti belə kömək etməz — Roma yayda həddindən artıq isti olur."
        return False, "✈️ Mövsüm Roma kəşfi üçün idealdır!"
    if "tokyo" in city_lower and travel_month in [3, 4]:
        return False, "🌸 Sakura dövrüdür! Möhtəşəm vaxt seçimi."
    return False, "✈️ Seçdiyiniz dövr səyahət üçün uyğundur!"


def generate_luxury_pdf(plan_text, route, budget):
    pdf = FPDF()
    pdf.add_page()

    # Azərbaycan şriftini (Dejavu Sans) birbaşa vebdən yükləyirik ki, Linux-da kvadrat çıxmasın
    font_url = "https://raw.githubusercontent.com/reingart/pyfpdf/master/fpdf/font/DejaVuSans.ttf"
    font_path = "DejaVuSans.ttf"
    try:
        urllib.request.urlretrieve(font_url, font_path)
        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.set_font("DejaVu", size=12)
    except:
        # Əgər internetdə problem olarsa, standart şriftə keçsin
        pdf.set_font("Arial", size=12)

    # Başlıq hissəsi
    pdf.set_text_color(201, 162, 74)  # Lüks qızılı rəng
    pdf.cell(200, 10, txt="CompassAI — Eksklüziv Səyahət Planı", ln=True, align='C')
    pdf.ln(10)

    # Məlumat paneli
    pdf.set_text_color(34, 34, 34)
    pdf.cell(200, 8, txt=f"Marşrut: {route}", ln=True)
    pdf.cell(200, 8, txt=f"Ümumi Büdcə: {budget}", ln=True)
    pdf.cell(200, 8, txt=f"Yaradılma Tarixi: {datetime.date.today().strftime('%d.%m.%Y')}", ln=True)
    pdf.ln(10)

    # Səyahət planının mətni
    for line in plan_text.split('\n'):
        clean_line = line.replace("**", "")  # Ulduzları təmizləyirik
        if clean_line.strip().startswith('#'):
            pdf.set_text_color(201, 162, 74)
            pdf.cell(200, 10, txt=clean_line.lstrip('#').strip(), ln=True)
            pdf.set_text_color(34, 34, 34)
        else:
            pdf.multi_cell(0, 8, txt=clean_line)

    # PDF-i yaddaşa yazırıq
    output = io.BytesIO()
    pdf.output(output)
    output.seek(0)
    return output

with st.sidebar:
    st.markdown("<h2 style='color:#c9a24a; margin-bottom:0;'>⚙️ Tənzimləmələr</h2>", unsafe_allow_html=True)
    lang = st.selectbox("🌐 Language / Dil", ["AZ", "EN"])
    T = LANG_DICT[lang]

st.markdown(f"<h1 class='main-title'>{T['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle-text'>{T['subtitle']}</p>", unsafe_allow_html=True)
st.write("---")

if "legs" not in st.session_state:
    st.session_state.legs = [{"city": "", "days": 3}]

st.markdown("<div class='mobile-form-card'>", unsafe_allow_html=True)
st.markdown(f"### {T['options']}")

travel_date = st.date_input(T["date"], min_value=datetime.date.today())

col_budget, col_currency = st.columns([2, 1])
budget = col_budget.number_input(T["budget"], min_value=50, value=500)
currency = col_currency.selectbox(T["currency_label"], CURRENCY_OPTIONS, index=0)

style = st.selectbox(T["style"], T["style_opt"])

st.markdown("---")
st.markdown(f"#### {T['multi_city_title']}")

legs_to_remove = None
for i, leg in enumerate(st.session_state.legs):
    c1, c2, c3 = st.columns([3, 2, 1])
    leg["city"] = c1.text_input(
        T["leg_city"], value=leg["city"], key=f"leg_city_{i}",
        placeholder=T["city_placeholder"], label_visibility="collapsed" if i > 0 else "visible"
    )
    leg["days"] = c2.number_input(
        T["leg_days"], min_value=1, max_value=60, value=leg["days"], key=f"leg_days_{i}",
        label_visibility="collapsed" if i > 0 else "visible"
    )
    with c3:
        if i == 0:
            st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
        if len(st.session_state.legs) > 1 and st.button(T["remove_leg"], key=f"leg_remove_{i}"):
            legs_to_remove = i

if legs_to_remove is not None:
    st.session_state.legs.pop(legs_to_remove)
    st.rerun()

if st.button(T["add_city"], use_container_width=True):
    st.session_state.legs.append({"city": "", "days": 3})
    st.rerun()

total_days = sum(leg["days"] for leg in st.session_state.legs)
st.caption(f"{T['total_days_label']}: **{total_days} {T['days_word']}**")

st.markdown(f"### {T['interests']}")
int_m = st.checkbox(T["int_museums"], value=True)
int_n = st.checkbox(T["int_nature"])
int_f = st.checkbox(T["int_food"])
int_ny = st.checkbox(T["int_night"])

plan_format_idx = st.radio(T["format"], T["format_opt"], index=0)
is_detailed = plan_format_idx == T["format_opt"][0]

st.markdown("</div>", unsafe_allow_html=True)

st.session_state["api_key"] = DEFAULT_API_KEY

if "generated_plan_text" not in st.session_state:
    st.session_state["generated_plan_text"] = ""
if "route_summary_text" not in st.session_state:
    st.session_state["route_summary_text"] = ""

if st.button(T["btn_start"], use_container_width=True):
    legs = [{"city": leg["city"].strip().title(), "days": leg["days"]} for leg in st.session_state.legs]
    all_cities_filled = all(leg["city"] for leg in legs)

    if not all_cities_filled:
        st.error("Please enter a city / Seher daxil edin.")
    elif not st.session_state.get("api_key"):
        st.error(T["api_key_not_found"])
    else:
        total_days = sum(leg["days"] for leg in legs)
        any_bad_weather = False
        weather_notes = []

        current_date = travel_date
        for idx, leg in enumerate(legs):
            city = leg["city"]
            leg_days = leg["days"]
            leg_start = current_date
            leg_end = current_date + datetime.timedelta(days=leg_days - 1)

            st.markdown("<div class='animated-card'>", unsafe_allow_html=True)
            st.markdown(
                f"<span class='leg-badge'>{T['leg_of_trip']} {idx + 1}/{len(legs)}: "
                f"{leg_start.strftime('%d.%m')} → {leg_end.strftime('%d.%m')} ({leg_days} {T['days_word']})</span>",
                unsafe_allow_html=True
            )
            st.subheader(f"📍 {city}")

            img_url = f"https://loremflickr.com/1000/350/{quote(city)},travel,landmark/all"
            st.image(img_url, caption=f"{T['photo_cap']}: {city}", use_container_width=True)

            # ============ TƏCİLİ MƏLUMAT KARTI ============
            st.markdown("#### 🚨 Təcili Məlumat və Qaydalar")

            # Şəhərə görə statik baza məlumatları təyin edirik (Genişləndirilə bilər)
            city_upper = city.upper()
            emergency_no = "112"
            visa_info = "AI tərəfindən yoxlanılır..."
            timezone = "UTC+1"

            if "PARIS" in city_upper:
                emergency_no = "112 (Ümumi), 15 (Təcili Yardım)"
                visa_info = "Şengen vizası tələb olunur (Azərbaycan vətəndaşları üçün)."
                timezone = "Paris (GMT+2)"
            elif "TOKYO" in city_upper:
                emergency_no = "119 (Yanğın/Təcili), 110 (Polis)"
                visa_info = "Viza tələb olunur. Səfirlikdən öncədən alınmalıdır."
                timezone = "Tokyo (GMT+9)"
            elif "ROMA" in city_upper or "ROME" in city_upper:
                emergency_no = "112 (Ümumi Polis və Tibb)"
                visa_info = "Şengen vizası tələb olunur."
                timezone = "Roma (GMT+2)"
            else:
                visa_info = "Giriş qaydalarını yoxlamaq üçün AI bələdçinizə müraciət edin."
                timezone = "Yerli vaxt zolağı"

            # Vizual Kart Dizaynı
            st.markdown(f"""
                            <div style="background: rgba(201,162,74,0.08); border-left: 5px solid #c9a24a; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                                <p style="margin: 0 0 8px 0;"><b>📞 Təcili Nömrələr:</b> {emergency_no}</p>
                                <p style="margin: 0 0 8px 0;"><b>🌍 Vaxt Zolağı:</b> {timezone}</p>
                                <p style="margin: 0;"><b>🛂 Viza Tələbi:</b> {visa_info}</p>
                            </div>
                        """, unsafe_allow_html=True)

            with st.spinner(T["spinner_weather"]):
                try:
                    geo_res = get_coordinates(city)
                    if geo_res.get("results"):
                        lat = geo_res["results"][0]["latitude"]
                        lon = geo_res["results"][0]["longitude"]

                        today = datetime.date.today()
                        if (leg_start - today).days <= 14:
                            w_data = get_weather(lat, lon, str(leg_start))
                            max_t = w_data['daily']['temperature_2m_max'][0]
                            min_t = w_data['daily']['temperature_2m_min'][0]

                            col_w1, col_w2 = st.columns(2)
                            col_w1.metric(f"{T['weather_high']} ({city})", f"{max_t} °C")
                            col_w2.metric(f"{T['weather_low']} ({city})", f"{min_t} °C")

                            if max_t > 38 or max_t < 0:
                                any_bad_weather = True
                        else:
                            st.info(T["weather_no_forecast"])

                        is_bad, note = seasonal_note(city.lower(), leg_start.month)
                        if is_bad:
                            any_bad_weather = True
                            weather_notes.append(f"{city}: {note}")
                            st.warning(note)
                        else:
                            st.success(note)
                    else:
                        st.warning(f"{T['geo_not_found']} ({city})")
                except requests.exceptions.RequestException as e:
                    st.warning(f"{T['weather_delay']} ({city}: {e})")

            st.markdown("</div>", unsafe_allow_html=True)
            current_date = leg_end + datetime.timedelta(days=1)

        st.markdown("<div class='animated-card'>", unsafe_allow_html=True)
        st.subheader(T["budget_title"])

        symbol = CURRENCY_SYMBOLS.get(currency, currency)
        try:
            rate_to_azn = get_exchange_rate_to_azn(currency)
        except Exception:
            rate_to_azn = None
            st.warning(T["rate_error"])

        if rate_to_azn:
            st.caption(
                f"{T['rate_caption']}: 1 {currency} ≈ {rate_to_azn:.4f} AZN "
                f"→ {T['azn_equivalent']}: **{budget * rate_to_azn:,.2f} ₼**"
            )


        def fmt_amount(amount: float) -> str:
            text = f"{symbol}{amount:.2f}"
            if rate_to_azn:
                text += f"  (≈ {amount * rate_to_azn:.2f} ₼)"
            return text


        daily_budget = budget / total_days
        hotel_share = daily_budget * 0.40
        food_share = daily_budget * 0.30
        trans_share = daily_budget * 0.30

        col_b1, col_b2, col_b3 = st.columns(3)
        col_b1.metric(T["hotel"], fmt_amount(hotel_share))
        col_b2.metric(T["food"], fmt_amount(food_share))
        col_b3.metric(T["transport"], fmt_amount(trans_share))

        daily_budget_azn = daily_budget * rate_to_azn if rate_to_azn else daily_budget

        col_g1, col_g2 = st.columns([1, 2])
        if daily_budget_azn < 120:
            with col_g1:
                fun_status_card("🐣", "Econo-mode!", "#8B3A2A")
            with col_g2:
                st.markdown(f'<div class="status-box" style="background:#8B3A2A;">{T["status_low"]}</div>',
                            unsafe_allow_html=True)
        elif 120 <= daily_budget_azn <= 300:
            with col_g1:
                fun_status_card("🎈", "Balanced!", "#c9a24a", text_color="#0b1120")
            with col_g2:
                st.markdown(
                    f'<div class="status-box" style="background:#c9a24a; color:#0b1120;">{T["status_mid"]}</div>',
                    unsafe_allow_html=True)
        else:
            with col_g1:
                fun_status_card("🎉", "Luxury mode!", "#2E7D5B")
            with col_g2:
                st.markdown(f'<div class="status-box" style="background:#2E7D5B;">{T["status_high"]}</div>',
                            unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        selected_interests = []
        if int_m: selected_interests.append(T["int_museums"])
        if int_n: selected_interests.append(T["int_nature"])
        if int_f: selected_interests.append(T["int_food"])
        if int_ny: selected_interests.append(T["int_night"])
        interests_str = ", ".join(selected_interests) if selected_interests else "-"

        format_instruction = (
            "günbəgün DETALLI, otel məsləhətləri daxil olmaqla geniş marşrut yaz"
            if is_detailed else "çox qısa xülasə yaz"
        )

        route_lines = []
        cd = travel_date
        for leg in legs:
            leg_end = cd + datetime.timedelta(days=leg["days"] - 1)
            route_lines.append(
                f"- {leg['city']}: {cd.strftime('%d.%m.%Y')} - {leg_end.strftime('%d.%m.%Y')} ({leg['days']} gün)")
            cd = leg_end + datetime.timedelta(days=1)
        route_description = "\n".join(route_lines)
        st.session_state["route_summary_text"] = route_description

        alt_date_prompt = ""
        if any_bad_weather and weather_notes:
            alt_date_prompt = " Hava məsələlərinə diqqət et."

        budget_azn_note = f" (≈ {budget * rate_to_azn:,.2f} AZN)" if rate_to_azn else ""
        ai_plan = None

        with st.spinner(T["spinner_ai"]):
            try:
                client = genai.Client(api_key=st.session_state.api_key)

                prompt = f"""
                {T['ai_role']}
                Müştəri marşrutu:
                {route_description}
                Büdcə: {symbol}{budget} {currency}{budget_azn_note} (Tərz: {style}).
                Maraqlar: {interests_str}.
                {format_instruction}.{alt_date_prompt}
                Markdown formatında yaz.
                """

                response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                ai_plan = response.text
                st.session_state["generated_plan_text"] = ai_plan
            except Exception as e:
                st.error(f"{T['ai_error']}: {e}")

if st.session_state.get("generated_plan_text"):
    st.markdown("<div class='animated-card'>", unsafe_allow_html=True)
    st.subheader(T["ai_title"])
    st.markdown(st.session_state["generated_plan_text"])
    st.markdown("</div>", unsafe_allow_html=True)

    cities_joined = "-".join(leg["city"] for leg in st.session_state.legs)
    cities_joined = "-".join(leg["city"] for leg in st.session_state.legs)

    # PDF generation
    pdf_data = generate_luxury_pdf(
        st.session_state["generated_plan_text"],
        st.session_state.get("route_summary_text", ""),
        f"{budget} {currency}"
    )

    st.download_button(
        label="📥 Eksklüziv PDF Planı Yüklə",
        data=pdf_data,
        file_name=f"{cities_joined}_luxury_plan.pdf",
        mime="application/pdf",
        use_container_width=True
    )


with st.sidebar:
    st.markdown("---")
    st.markdown(f"### {T['chat_header']}")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if st.session_state.chat_history:
        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
        for msg in st.session_state.chat_history:
            role_emoji = "👤" if msg["role"] == "user" else "🤖"
            st.markdown(f"**{role_emoji}**: {msg['content']}")
        st.markdown("</div>", unsafe_allow_html=True)

    if user_in := st.chat_input(T["chat_placeholder"], key="sidebar_chat_input"):
        st.session_state.chat_history.append({"role": "user", "content": user_in})

        if not st.session_state.get("api_key"):
            st.warning(T["api_key_not_found"])
        else:
            try:
                client = genai.Client(api_key=st.session_state.api_key)
                context_route = st.session_state.get("route_summary_text", "Hələ plan qurulmayıb")
                system_instruction = (
                    f"{T['ai_role']} Sən hazırda bu marşrut üzrə kömək edirsən:\n{context_route}\n"
                    "İstifadəçinin sualına qısa, şən və emojilərlə cavab ver."
                )
                chat_prompt = f"{system_instruction}\nİstifadəçi: {user_in}"
                response = client.models.generate_content(model='gemini-2.5-flash', contents=chat_prompt)
                st.session_state.chat_history.append({"role": "assistant", "content": response.text})
                st.rerun()
            except Exception as e:
                st.sidebar.error(f"Chat Error: {e}")