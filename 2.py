
import streamlit as st
import pandas as pd
from PIL import Image
import pytesseract

st.set_page_config(page_title="ایجنت هوشمند کابینت‌سازی", layout="centered")
st.title("🧠 ایجنت هوشمند کابینت‌سازی - نسخه پیشرفته با نقشه‌خوانی")

st.markdown("""
### 🎯 محاسبه قیمت، متریال و طراحی پروژه کابینت
ایجنت با سوالات هوشمند، پروژه را تحلیل می‌کند و سود، قیمت و اطلاعات فنی ارائه می‌دهد. همچنین امکان آپلود نقشه و خواندن آن فراهم شده است.
""")

# آپلود فایل نقشه
st.subheader("📤 آپلود نقشه طراحی (تصویر یا PDF)")
uploaded_file = st.file_uploader("یک تصویر از نقشه یا طراحی کابینت را آپلود کنید", type=["png", "jpg", "jpeg"])
extracted_text = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="نقشه آپلودشده", use_column_width=True)
    st.write("در حال پردازش تصویر...")
    extracted_text = pytesseract.image_to_string(image, lang='eng+fas')
    st.write("🧾 متن استخراج‌شده از نقشه:")
    st.code(extracted_text)

    # تحلیل اولیه ابعاد بر اساس متن (نمونه ساده)
    possible_units = []
    for line in extracted_text.split('\n'):
        if any(unit in line.lower() for unit in ["base", "wall", "کابینت", "یونیت"]):
            possible_units.append(line)

    if possible_units:
        st.write("📌 واحدهای احتمالی تشخیص داده‌شده از نقشه:")
        for unit in possible_units:
            st.write(f"- {unit}")

        confirm = st.radio("آیا می‌خواهید این اطلاعات را ویرایش یا تأیید کنید؟", ("تأیید اطلاعات نقشه", "ویرایش دستی"))
        if confirm == "ویرایش دستی":
            st.info("فعلاً ویرایش دستی اطلاعات یونیت‌ها را به صورت فرم از شما دریافت خواهیم کرد. در نسخه‌های بعدی می‌توانیم جدول پویا یا ترسیم بصری هم اضافه کنیم.")

# فرم اصلی پروژه
with st.form("project_form"):
    st.subheader("🔍 مشخصات پروژه")
    project_name = st.text_input("نام پروژه")
    customer_name = st.text_input("نام مشتری")
    location = st.text_input("موقعیت جغرافیایی پروژه")

    st.subheader("📐 ابعاد کلی")
    total_length = st.number_input("طول کل کابینت‌ها (متر)", min_value=1.0, step=0.1)
    wall_height = st.selectbox("ارتفاع کابینت دیواری (سانتی‌متر)", [70, 80, 90])
    base_height = st.selectbox("ارتفاع کابینت زمینی (سانتی‌متر)", [85, 90])

    st.subheader("🧱 متریال و یراق‌آلات")
    material = st.selectbox("نوع ورق MDF", ["MDF ایرانی", "MDF خارجی", "هایگلاس", "PVC"])
    edge_band = st.selectbox("نوع نوار PVC لبه‌کاری", ["معمولی", "مات خارجی", "براق خارجی"])
    hardware = st.selectbox("نوع یراق‌آلات", ["معمولی", "متوسط", "لوکس"])

    st.subheader("🎨 رنگ و استایل")
    color_style = st.selectbox("ترکیب رنگ کلی پروژه", ["سفید و طوسی", "کرم و قهوه‌ای", "مشکی و چوبی", "سفارشی"])
    finish_type = st.selectbox("نوع فینیش", ["مات", "براق", "های‌گلاس"])

    submitted = st.form_submit_button("محاسبه کن")

if submitted:
    material_prices = {
        "MDF ایرانی": 1500000,
        "MDF خارجی": 2200000,
        "هایگلاس": 3000000,
        "PVC": 3500000
    }
    edge_factors = {
        "معمولی": 1.0,
        "مات خارجی": 1.1,
        "براق خارجی": 1.2
    }
    hardware_factors = {
        "معمولی": 1.0,
        "متوسط": 1.15,
        "لوکس": 1.35
    }

    # محاسبه‌ها
    base_price = total_length * material_prices[material]
    edge_price = base_price * edge_factors[edge_band] * 0.1
    hardware_price = base_price * hardware_factors[hardware] * 0.2

    total_cost = base_price + edge_price + hardware_price
    profit = total_cost * 0.25
    final_price = total_cost + profit

    st.success(f"نتایج پروژه برای {project_name} ({customer_name})")
    st.write(f"**مکان پروژه:** {location}")
    st.write(f"**قیمت متریال پایه:** {int(base_price):,} تومان")
    st.write(f"**هزینه نوار PVC:** {int(edge_price):,} تومان")
    st.write(f"**هزینه یراق‌آلات:** {int(hardware_price):,} تومان")
    st.write(f"**قیمت تمام‌شده:** {int(total_cost):,} تومان")
    st.write(f"**سود پیشنهادی:** {int(profit):,} تومان")
    st.write(f"**قیمت پیشنهادی نهایی به مشتری:** {int(final_price):,} تومان")
