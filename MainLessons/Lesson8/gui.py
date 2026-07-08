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
    """
    AÃ§arÄ± É™vvÉ™lcÉ™ .env-dÉ™n (lokal inkiÅŸaf Ã¼Ã§Ã¼n), tapÄ±lmasa
    Streamlit Cloud-un Ã¶z Secrets sistemindÉ™n (st.secrets) oxuyur.
    BelÉ™liklÉ™ eyni kod hÉ™m PyCharm-da, hÉ™m dÉ™ deploy edilmiÅŸ saytda iÅŸlÉ™yir.
    """
    value = os.getenv(key, "")
    if value:
        return value
    try:
        return st.secrets.get(key, default)
    except Exception:
        return default


st.set_page_config(page_title="RoamPulse Pro", page_icon="âœˆï¸", layout="wide")

DEFAULT_API_KEY = get_secret("GEMINI_API_KEY")

LANG_DICT = {
    "AZ": {
        "title": "âœˆï¸ RoamPulse SÉ™yahÉ™t PortalÄ±",
        "subtitle": "SÉ™yahÉ™t planÄ±nÄ±zÄ± yaradÄ±n, canlÄ± hava durumunu vÉ™ otellÉ™ri anÄ±nda saytda gÃ¶rÃ¼n!",
        "settings": "âš™ï¸ TÉ™nzimlÉ™mÉ™lÉ™r",
        "options": "ðŸ“‹ SÉ™yahÉ™t ParametrlÉ™ri",
        "multi_city_title": "ðŸ—ºï¸ MarÅŸrut (ÅžÉ™hÉ™rlÉ™r)",
        "leg_city": "ÅžÉ™hÉ™r",
        "leg_days": "GÃ¼n",
        "add_city": "âž• ÅžÉ™hÉ™r É™lavÉ™ et",
        "remove_leg": "ðŸ—‘ï¸",
        "total_days_label": "ðŸ§® Ãœmumi MÃ¼ddÉ™t",
        "days_word": "gÃ¼n",
        "city_placeholder": "MÉ™s: Paris, Tokyo, Roma",
        "date": "ðŸ“… SÉ™yahÉ™tin BaÅŸlama Tarixi",
        "budget": "ðŸ’° Ãœmumi BÃ¼dcÉ™ (USD)",
        "style": "ðŸŽ­ SÉ™yahÉ™t TÉ™rzi",
        "style_opt": ["Ekonom", "Orta", "LÃ¼ks"],
        "interests": "ðŸŽ¯ Maraq DairÉ™si",
        "int_museums": "Tarix vÉ™ MuzeylÉ™r",
        "int_nature": "TÉ™biÉ™t vÉ™ Parklar",
        "int_food": "Yerli MÉ™tbÉ™x",
        "int_night": "GecÉ™ HÉ™yatÄ±",
        "format": "ðŸ“‹ Hesabat NÃ¶vÃ¼",
        "format_opt": ["DetallÄ± Plan", "QÄ±sa XÃ¼lasÉ™"],
        "security": "ðŸ”‘ TÉ™hlÃ¼kÉ™sizlik",
        "api_placeholder": "AÃ§arÄ±nÄ±zÄ± bura daxil edin",
        "api_saved_msg": "âœ… AÃ§ar .env-dÉ™n avtomatik yÃ¼klÉ™ndi",
        "btn_start": "ðŸš€ SÉ™yahÉ™t PlanÄ±nÄ± HazÄ±rla",
        "err_missing": "âŒ ZÉ™hmÉ™t olmasa bÃ¼tÃ¼n ÅŸÉ™hÉ™rlÉ™ri vÉ™ Gemini API aÃ§arÄ±nÄ± daxil edin!",
        "photo_cap": "ðŸ“¸ MÃ¶htÉ™ÅŸÉ™m MÉ™kan",
        "weather_title": "â˜€ï¸ CanlÄ± Hava VÉ™ziyyÉ™ti",
        "weather_high": "GÃ¶zlÉ™nilÉ™n Æn YÃ¼ksÉ™k",
        "weather_low": "GÃ¶zlÉ™nilÉ™n Æn AÅŸaÄŸÄ±",
        "weather_no_forecast": "â„¹ï¸ Bu tarix Ã¼Ã§Ã¼n anlÄ±q proqnoz yoxdur, mÃ¶vsÃ¼mi rejim aktivdir.",
        "geo_not_found": "âš ï¸ Bu ÅŸÉ™hÉ™r tapÄ±lmadÄ±, adÄ± yoxlayÄ±b yenidÉ™n cÉ™hd edin.",
        "expert_advice": "ðŸ’¡ Ekspert MÃ¶vsÃ¼m TÃ¶vsiyÉ™si",
        "budget_title": "ðŸ“Š GÃ¼nlÃ¼k TÉ™xmini BÃ¼dcÉ™ BÃ¶lgÃ¼sÃ¼ (Ãœmumi)",
        "hotel": "ðŸ¨ Otel vÉ™ Qalmaq",
        "food": "ðŸ” YemÉ™k vÉ™ Restoran",
        "transport": "ðŸš— NÉ™qliyyat vÉ™ ÆylÉ™ncÉ™",
        "ai_title": "âœ¨ Sizin XÃ¼susi Ã‡oxÅŸÉ™hÉ™rli SÉ™yahÉ™t PlanÄ±nÄ±z",
        "btn_download": "ðŸ“¥ PlanÄ± YÃ¼klÉ™",
        "ai_error": "ðŸ’¥ SÃ¼ni Ä°ntellekt xÉ™tti mÉ™ÅŸÄŸuldur",
        "weather_delay": "âš ï¸ Hava mÉ™lumatlarÄ±nda fasilÉ™ yarandÄ±",
        "status_low": "ðŸ£ BÃ¼dcÉ™ EKONOMDUR! QÉ™naÉ™tli sÉ™yahÉ™t.",
        "status_mid": "ðŸŽˆ BÃ¼dcÉ™ ORTADIR! BalanslÄ± vÉ™ rahat.",
        "status_high": "ðŸŽ‰ BÃ¼dcÉ™ YAXÅžIDIR! Rahat vÉ™ lÃ¼ks sÉ™yahÉ™t edÉ™ bilÉ™rsiniz.",
        "ai_role": "SÉ™n enerjili vÉ™ ÅŸÉ™n AI SÉ™yahÉ™t BÉ™lÉ™dÃ§isisÉ™n. AzÉ™rbaycan dilindÉ™ emojilÉ™rlÉ™ bol cavab ver.",
        "spinner_weather": "ðŸŒ¦ï¸ Hava mÉ™lumatlarÄ± yÃ¼klÉ™nir...",
        "spinner_ai": "ðŸ¤– AI planÄ±nÄ±zÄ± hazÄ±rlayÄ±r...",
        "leg_of_trip": "MarÅŸrut hissÉ™si",
        "api_key_not_found": "Gemini API key was not found on the server. Add GEMINI_API_KEY in Streamlit Cloud > App settings > Secrets.",
        "currency_label": "ðŸ’± Valyuta",
        "azn_equivalent": "AZN-É™ Ã§evrilmiÅŸ",
        "rate_caption": "MÉ™zÉ™nnÉ™",
        "rate_error": "âš ï¸ MÉ™zÉ™nnÉ™ tapÄ±lmadÄ±, AZN Ã§evrilmÉ™si gÃ¶stÉ™rilmir."
    },
    "EN": {
        "title": "âœˆï¸ RoamPulse Travel Portal",
        "subtitle": "Create your travel plan, see live weather and hotels instantly on the site!",
        "settings": "âš™ï¸ Settings",
        "options": "ðŸ“‹ Travel Parameters",
        "multi_city_title": "ðŸ—ºï¸ Route (Cities)",
        "leg_city": "City",
        "leg_days": "Days",
        "add_city": "âž• Add city",
        "remove_leg": "ðŸ—‘ï¸",
        "total_days_label": "ðŸ§® Total Duration",
        "days_word": "days",
        "city_placeholder": "E.g.: Paris, Tokyo, Rome",
        "date": "ðŸ“… Trip Start Date",
        "budget": "ðŸ’° Total Budget (USD)",
        "style": "ðŸŽ­ Travel Style",
        "style_opt": ["Budget", "Mid-range", "Luxury"],
        "interests": "ðŸŽ¯ Interests",
        "int_museums": "History & Museums",
        "int_nature": "Nature & Parks",
        "int_food": "Local Cuisine",
        "int_night": "Nightlife",
        "format": "ðŸ“‹ Report Type",
        "format_opt": ["Detailed Plan", "Short Summary"],
        "security": "ðŸ”‘ Security",
        "api_placeholder": "Enter your key here",
        "api_saved_msg": "âœ… Key auto-loaded from .env",
        "btn_start": "ðŸš€ Prepare Travel Plan",
        "err_missing": "âŒ Please fill in all cities and the Gemini API key!",
        "photo_cap": "ðŸ“¸ Amazing Destination",
        "weather_title": "â˜€ï¸ Live Weather Conditions",
        "weather_high": "Expected Max",
        "weather_low": "Expected Min",
        "weather_no_forecast": "â„¹ï¸ No live forecast for this date, seasonal mode is active.",
        "geo_not_found": "âš ï¸ City not found, please check the spelling and try again.",
        "expert_advice": "ðŸ’¡ Expert Seasonal Advice",
        "budget_title": "ðŸ“Š Estimated Daily Budget Allocation (Overall)",
        "hotel": "ðŸ¨ Hotel & Stay",
        "food": "ðŸ” Food & Dining",
        "transport": "ðŸš— Transport & Leisure",
        "ai_title": "âœ¨ Your Custom Multi-City Travel Plan",
        "btn_download": "ðŸ“¥ Download Plan",
        "ai_error": "ðŸ’¥ AI Line is busy",
        "weather_delay": "âš ï¸ Temporary delay in weather data",
        "status_low": "ðŸ£ Budget is BUDGET-FRIENDLY!",
        "status_mid": "ðŸŽˆ Budget is MID-RANGE!",
        "status_high": "ðŸŽ‰ Budget is GREAT! Enjoy luxury.",
        "ai_role": "You are an energetic and cheerful AI Travel Guide. Provide your response in English with plenty of emojis.",
        "spinner_weather": "ðŸŒ¦ï¸ Loading weather data...",
        "spinner_ai": "ðŸ¤– AI is preparing your plan...",
        "leg_of_trip": "Trip leg",
        "api_key_not_found": "Gemini API key was not found on the server. Add GEMINI_API_KEY in Streamlit Cloud > App settings > Secrets.",
        "currency_label": "ðŸ’± Currency",
        "azn_equivalent": "Converted to AZN",
        "rate_caption": "Exchange rate",
        "rate_error": "âš ï¸ Exchange rate not found, AZN conversion unavailable."
    }
}

def measure_time(func):
    """
    Ã–z yazdÄ±ÄŸÄ±mÄ±z dekorator: funksiyanÄ±n icra mÃ¼ddÉ™tini Ã¶lÃ§Ã¼b sidebar-Ä±n
    altÄ±nda kiÃ§ik bir caption kimi gÃ¶stÉ™rir. SillabusdakÄ± 'Dekoratorlar'
    mÃ¶vzusunu gÃ¶stÉ™rmÉ™k Ã¼Ã§Ã¼n É™lavÉ™ edilib - @st.cache_data ilÉ™ birlikdÉ™
    stack olunaraq iÅŸlÉ™yir (É™vvÉ™lcÉ™ functools.wraps ilÉ™ orijinal funksiyanÄ±n
    adÄ±/metadatasÄ± qorunur, sonra É™sl funksiya Ã§aÄŸÄ±rÄ±lÄ±r vÉ™ vaxt Ã¶lÃ§Ã¼lÃ¼r).
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        # YalnÄ±z 10ms-dÉ™n Ã§ox Ã§É™kÉ™ndÉ™ gÃ¶stÉ™ririk (keÅŸlÉ™nmiÅŸ Ã§aÄŸÄ±rÄ±ÅŸlar demÉ™k olar 0ms-dir)
        if elapsed > 0.01:
            st.caption(f"â±ï¸ `{func.__name__}` â†’ {elapsed:.2f}s")
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
CURRENCY_SYMBOLS = {"USD": "$", "EUR": "â‚¬", "GBP": "Â£", "AZN": "â‚¼", "TRY": "â‚º", "RUB": "â‚½"}


@measure_time
@st.cache_data(ttl=3600, show_spinner=False)
def get_exchange_rate_to_azn(base_currency: str):
    """SeÃ§ilmiÅŸ valyutadan 1 vahidin bugÃ¼nkÃ¼ AZN qarÅŸÄ±lÄ±ÄŸÄ±nÄ± qaytarÄ±r. AZN seÃ§ilibsÉ™ 1.0 qaytarÄ±r."""
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
            return True, ("ðŸ”¥ Roma yay aylarÄ±nda (Ä°yul-Avqust) hÉ™ddindÉ™n artÄ±q isti vÉ™ boÄŸucu olur. "
                           "GÉ™zinti Ã¼Ã§Ã¼n É™lveriÅŸli deyil. Alternativ olaraq Aprel-May vÉ™ ya "
                           "Sentyabr-Oktyabr aylarÄ±nÄ± tÃ¶vsiyÉ™ edirik.")
        return False, "âœˆï¸ MÃ¶vsÃ¼m Roma kÉ™ÅŸfi Ã¼Ã§Ã¼n idealdÄ±r!"
    if "tokyo" in city_lower and travel_month in [3, 4]:
        return False, "ðŸŒ¸ Sakura dÃ¶vrÃ¼dÃ¼r! MÃ¶htÉ™ÅŸÉ™m vaxt seÃ§imi."
    return False, "âœˆï¸ SeÃ§diyiniz dÃ¶vr sÉ™yahÉ™t Ã¼Ã§Ã¼n uyÄŸundur!"


with st.sidebar:
    st.markdown("<h2 style='color:#FF4B2B; margin-bottom:0;'>âš™ï¸ TÉ™nzimlÉ™mÉ™lÉ™r</h2>", unsafe_allow_html=True)
    lang = st.selectbox("ðŸŒ Language / Dil", ["AZ", "EN"])
    T = LANG_DICT[lang]

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    .main-title {
        background: linear-gradient(45deg, #FF416C, #FF4B2B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px; font-weight: 700; text-align: center; margin-bottom: 5px;
    }
    .subtitle-text { text-align: center; color: #a4b0be; font-size: 16px; margin-bottom: 10px; }
    .animated-card {
        background-color: #1e1e24; padding: 25px; border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.35); margin-bottom: 25px;
        border: 1px solid rgba(255,255,255,0.05);
    }
    .leg-badge {
        display: inline-block; background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
        color: #0b0b0d; font-weight: 700; padding: 4px 14px; border-radius: 999px;
        font-size: 13px; margin-bottom: 10px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%); color: white;
        border-radius: 8px; padding: 12px 28px; font-size: 16px; font-weight: 600;
        border: none; transition: transform 0.15s ease;
    }
    .stButton>button:hover { transform: scale(1.02); }
    .status-box { padding: 15px; border-radius: 10px; font-weight: 600; text-align: center; margin-bottom: 15px; }
    .bounce-card {
        display: flex; align-items: center; gap: 14px; padding: 18px 22px;
        border-radius: 14px; font-weight: 700; font-size: 17px; height: 100%;
    }
    .bounce-emoji { font-size: 42px; display: inline-block; animation: bounce 1.4s ease-in-out infinite; }
    @keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
    .mobile-form-card {
        background-color: #1e1e24; padding: 22px; border-radius: 14px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.28); margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.06);
    }
    @media (max-width: 640px) {
        .block-container { padding: 1rem 0.8rem 2rem; }
        .main-title { font-size: 32px; line-height: 1.15; }
        .subtitle-text { font-size: 14px; }
        .mobile-form-card { padding: 16px; border-radius: 10px; }
        .animated-card { padding: 16px; border-radius: 10px; }
        .stButton>button { min-height: 48px; padding: 10px 14px; font-size: 15px; }
        [data-testid="stMetric"] { overflow-wrap: anywhere; }
    }
    </style>
""", unsafe_allow_html=True)

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

# API key is loaded from local .env or Streamlit secrets without showing it in the UI.
# This keeps the key out of screenshots and browser history.
st.session_state["api_key"] = DEFAULT_API_KEY

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
                f"{leg_start.strftime('%d.%m')} â†’ {leg_end.strftime('%d.%m')} ({leg_days} {T['days_word']})</span>",
                unsafe_allow_html=True
            )
            st.subheader(f"ðŸ“ {city}")

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
                            col_w1.metric(f"{T['weather_high']} ({city})", f"{max_t} Â°C")
                            col_w2.metric(f"{T['weather_low']} ({city})", f"{min_t} Â°C")

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
                f"{T['rate_caption']}: 1 {currency} â‰ˆ {rate_to_azn:.4f} AZN "
                f"â†’ {T['azn_equivalent']}: **{budget * rate_to_azn:,.2f} â‚¼**"
            )

        def fmt_amount(amount: float) -> str:
            text = f"{symbol}{amount:.2f}"
            if rate_to_azn:
                text += f"  (â‰ˆ {amount * rate_to_azn:.2f} â‚¼)"
            return text

        daily_budget = budget / total_days
        hotel_share = daily_budget * 0.40
        food_share = daily_budget * 0.30
        trans_share = daily_budget * 0.30

        col_b1, col_b2, col_b3 = st.columns(3)
        col_b1.metric(T["hotel"], fmt_amount(hotel_share))
        col_b2.metric(T["food"], fmt_amount(food_share))
        col_b3.metric(T["transport"], fmt_amount(trans_share))

        # BÃ¼dcÉ™ statusu valyutadan asÄ±lÄ± olmayaraq dÃ¼zgÃ¼n iÅŸlÉ™sin deyÉ™, mÃ¼qayisÉ™ni AZN Ã¼zÉ™rindÉ™n aparÄ±rÄ±q
        daily_budget_azn = daily_budget * rate_to_azn if rate_to_azn else daily_budget

        col_g1, col_g2 = st.columns([1, 2])
        if daily_budget_azn < 120:
            with col_g1:
                fun_status_card("ðŸ£", "Econo-mode!", "#FF3B30")
            with col_g2:
                st.markdown(f'<div class="status-box" style="background:#FF3B30;">{T["status_low"]}</div>', unsafe_allow_html=True)
        elif 120 <= daily_budget_azn <= 300:
            with col_g1:
                fun_status_card("ðŸŽˆ", "Balanced!", "#FFCC00", text_color="#1C1C1E")
            with col_g2:
                st.markdown(f'<div class="status-box" style="background:#FFCC00; color:#1C1C1E;">{T["status_mid"]}</div>', unsafe_allow_html=True)
        else:
            with col_g1:
                fun_status_card("ðŸŽ‰", "Luxury mode!", "#34C759")
            with col_g2:
                st.markdown(f'<div class="status-box" style="background:#34C759;">{T["status_high"]}</div>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        selected_interests = []
        if int_m: selected_interests.append(T["int_museums"])
        if int_n: selected_interests.append(T["int_nature"])
        if int_f: selected_interests.append(T["int_food"])
        if int_ny: selected_interests.append(T["int_night"])
        interests_str = ", ".join(selected_interests) if selected_interests else "-"

        format_instruction = (
            "gÃ¼nbÉ™gÃ¼n DETALLI, otel mÉ™slÉ™hÉ™tlÉ™ri daxil olmaqla geniÅŸ marÅŸrut yaz"
            if is_detailed else "Ã§ox qÄ±sa xÃ¼lasÉ™ yaz"
        )

        route_lines = []
        cd = travel_date
        for leg in legs:
            leg_end = cd + datetime.timedelta(days=leg["days"] - 1)
            route_lines.append(f"- {leg['city']}: {cd.strftime('%d.%m.%Y')} - {leg_end.strftime('%d.%m.%Y')} ({leg['days']} gÃ¼n)")
            cd = leg_end + datetime.timedelta(days=1)
        route_description = "\n".join(route_lines)

        alt_date_prompt = ""
        if any_bad_weather and weather_notes:
            alt_date_prompt = (
                "HÉ™mÃ§inin bÉ™zi ÅŸÉ™hÉ™rlÉ™r Ã¼Ã§Ã¼n hava/mÃ¶vsÃ¼m baxÄ±mÄ±ndan qeydlÉ™r var: "
                + " | ".join(weather_notes)
                + " ZÉ™hmÉ™t olmasa bunlarÄ± nÉ™zÉ™rÉ™ alaraq ayrÄ±ca bir baÅŸlÄ±qda alternativ tÃ¶vsiyÉ™lÉ™r ver."
            )

        budget_azn_note = f" (â‰ˆ {budget * rate_to_azn:,.2f} AZN)" if rate_to_azn else ""
        cities_joined = "-".join(leg["city"] for leg in legs)
        ai_plan = None

        with st.spinner(T["spinner_ai"]):
            try:
                client = genai.Client(api_key=st.session_state.api_key)

                prompt = f"""
                {T['ai_role']}
                MÃ¼ÅŸtÉ™ri aÅŸaÄŸÄ±dakÄ± Ã‡OXÅžÆHÆRLÄ° marÅŸrutla sÉ™yahÉ™t edÉ™cÉ™k (Ã¼mumi {total_days} gÃ¼n):
                {route_description}

                Ãœmumi BÃ¼dcÉ™: {symbol}{budget} {currency}{budget_azn_note} (TÉ™rz: {style}).
                GÃ¼nlÃ¼k orta otel bÃ¼dcÉ™si: {fmt_amount(hotel_share)}.
                MÃ¼ÅŸtÉ™rinin XÃ¼susi Maraq DairÉ™lÉ™ri: {interests_str}.

                ZÉ™hmÉ™t olmasa TÆK bir bitiÅŸik plan yaz: ÅŸÉ™hÉ™rdÉ™n ÅŸÉ™hÉ™rÉ™ keÃ§id tÃ¶vsiyÉ™lÉ™ri
                (mÉ™sÉ™lÉ™n qatar/tÉ™yyarÉ™ variantlarÄ±) daxil olmaqla, hÉ™r ÅŸÉ™hÉ™r Ã¼Ã§Ã¼n ayrÄ±ca baÅŸlÄ±q aÃ§ vÉ™
                o ÅŸÉ™hÉ™rin gÃ¼nlÉ™rini ardÄ±cÄ±l olaraq planla (mÉ™s: "GÃ¼n 1-4: Tokio", "GÃ¼n 5-7: Osaka").
                HÉ™r ÅŸÉ™hÉ™rdÉ™ maraqlara uyÄŸun yerlÉ™r vÉ™ otel/qalacaq yer tÃ¶vsiyÉ™lÉ™ri olsun.
                {format_instruction}. {alt_date_prompt}
                Markdown formatÄ±nda, baÅŸlÄ±qlarla struktura salÄ±nmÄ±ÅŸ cavab ver.
                """

                response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                ai_plan = response.text
            except Exception as e:
                st.error(f"{T['ai_error']}: {e}")

        if ai_plan:
            st.markdown("<div class='animated-card'>", unsafe_allow_html=True)
            st.subheader(T["ai_title"])
            st.markdown(ai_plan)
            st.markdown("</div>", unsafe_allow_html=True)

            st.download_button(
                label=T["btn_download"],
                data=ai_plan,
                file_name=f"{cities_joined}_seyahat_plani.txt",
                mime="text/plain",
                use_container_width=True
            )

