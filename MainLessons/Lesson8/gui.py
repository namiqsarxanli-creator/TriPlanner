import streamlit as st
from google import genai
import requests
import datetime
import os
import time
from functools import wraps
from urllib.parse import quote
from dotenv import load_dotenv

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

        /* ============ ARXA PLAN YENİLƏNDİ ============ */
        .stApp {
            background-color: #0b1120;
            background-image: 
                linear-gradient(180deg, rgba(11,17,32,0.92) 0%, rgba(15,23,42,0.96) 100%),
                url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='500' viewBox='0 0 800 500'%3E%3Cg fill='none' stroke='%23c9a24a' stroke-width='1.5' opacity='0.15'%3E%3Cpath d='M80 400 L110 180 L120 180 L150 400 M90 310 L140 310 M95 260 L135 260 M115 180 L115 140 L115 120'/%3E%3Cpath d='M250 400 L270 160 L310 165 L290 405 Z M255 340 L295 345 M260 280 L300 285 M265 220 L305 225'/%3E%3Cpath d='M380 400 L440 280 L500 400 Z M410 400 L440 280'/%3E%3Cpath d='M580 320 L590 260 L600 320 M575 290 L605 290 M590 260 L570 240 M590 260 L590 230 M590 260 L610 240'/%3E%3Cpath d='M680 400 L680 200 L710 200 L710 400 M680 230 L710 230 M695 215 A 6 6 0 1 1 695 214 M685 170 L705 170 L695 140 Z'/%3E%3C/g%3E%3C/svg%3E");
            background-repeat: repeat;
            background-size: 800px 500px;
            background-position: center top;
            background-attachment: fixed;
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
        "geo_not_found": "⚠️ Bu şəhər tapılmadı, adı yoxlayıb yenidən cəhd edin.",
        "budget_title": "📊 Günlük Təxmini Büdcə Bölgüsü (Ümumi)",
        "hotel": "🏨 Otel və Qalmaq",
        "food": "🍔 Yemək və Restoran",
        "transport": "🚗 Nəqliyyat və Əyləncə",
        "ai_title": "✨ Sizin Xüsusi Çoxşəhərli Səyahət Planınız",
        "btn_download": "📥 Planı Yüklə",
        "ai_error": "💥 Süni İntellekt xətti məşğuldur",
        "weather_delay": "⚠️ Hava məlumatlarında fasilə yarandı",
        "status_low": "🐣 Büdcə EKONOMDUR! Qənaətli səyahət.",
        "status_mid": "🎈 Büdcə ORTADIR! Balanslı və rahat.",
        "status_high": "🎉 Büdcə YAXŞIDIR! Rahat və lüks səyahət edə bilərsiniz.",
        "ai_role": "Sən enerjili və şən AI Səyahət Bələdçisisən. Azərbaycan dilində emojilərlə bol cavab ver.",
        "spinner_weather": "🌦️ Hava məlumatları yüklənir...",
        "spinner_ai": "🤖 AI planınızı hazırlayır...",
        "leg_of_trip": "Marşrut hissəsi",
        "api_key_not_found": "Gemini API key tapılmadı.",
        "currency_label": "💱 Valyuta",
        "azn_equivalent": "AZN-ə çevrilmiş",
        "rate_caption": "Məzənnə",
        "rate_error": "⚠️ Məzənnə tapılmadı.",
        "chat_header": "💬 Canlı Səyahət Bələdçiniz",
        "chat_placeholder": "Səyahət haqqında sual verin...",
        "wa_button": "🟢 Planı WhatsApp-a Göndər (n8n)",
        "wa_success": "🚀 Planınız WhatsApp-a uğurla göndərildi!",
        "wa_error": "❌ WhatsApp-a göndərilərkən xəta baş verirdi.",
        "wa_phone_label": "📞 WhatsApp Nömrəniz (Məs: +99450XXXXXXX)"
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
        "geo_not_found": "⚠️ City not found.",
        "budget_title": "📊 Estimated Daily Budget Allocation",
        "hotel": "🏨 Hotel & Stay",
        "food": "🍔 Food & Dining",
        "transport": "🚗 Transport & Leisure",
        "ai_title": "✨ Your Custom Multi-City Travel Plan",
        "btn_download": "📥 Download Plan",
        "ai_error": "💥 AI Line is busy",
        "weather_delay": "⚠️ Temporary delay in weather data",
        "status_low": "🐣 Budget is BUDGET-FRIENDLY!",
        "status_mid": "🎈 Budget is MID-RANGE!",
        "status_high": "🎉 Budget is GREAT!",
        "ai_role": "You are an AI Travel Guide. Provide response in English with emojis.",
        "spinner_weather": "🌦️ Loading weather data...",
        "spinner_ai": "🤖 AI is preparing your plan...",
        "leg_of_trip": "Trip leg",
        "api_key_not_found": "Gemini API key not found.",
        "currency_label": "💱 Currency",
        "azn_equivalent": "Converted to AZN",
        "rate_caption": "Exchange rate",
        "rate_error": "⚠️ Exchange rate not found.",
        "chat_header": "💬 Live Travel Assistant",
        "chat_placeholder": "Ask something about your trip...",
        "wa_button": "🟢 Send Plan to WhatsApp (n8n)",
        "wa_success": "🚀 Plan successfully sent to WhatsApp!",
        "wa_error": "❌ Error sending to WhatsApp.",
        "wa_phone_label": "📞 Your WhatsApp Number (E.g.: +99450XXXXXXX)"
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
            return True, "🔥 Roma yayda həddindən artıq isti olur."
        return False, "✈️ Mövsüm Roma kəşfi üçün idealdır!"
    if "tokyo" in city_lower and travel_month in [3, 4]:
        return False, "🌸 Sakura dövrüdür! Möhtəşəm vaxt seçimi."
    return False, "✈️ Seçdiyiniz dövr səyahət üçün uyğundur!"


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
    st.download_button(
        label=T["btn_download"],
        data=st.session_state["generated_plan_text"],
        file_name=f"{cities_joined}_seyahat_plani.txt",
        mime="text/plain",
        use_container_width=True
    )

# ============ SIDEBAR - CANLI AI CHATBOT ============
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