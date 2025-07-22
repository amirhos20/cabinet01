
# cabinet_ai_agent_app.py

import streamlit as st
from PIL import Image
import io
import base64

# -----------------------
# Header
# -----------------------
st.set_page_config(page_title="Cabinet AI Agent", layout="centered")
st.title("🧠 Cabinet AI Agent")
st.markdown("""
آپلود پلان یا تصویر اولیه کابینت‌سازی، سپس پاسخ به چند سؤال ساده برای دریافت پیشنهاد اولیه ساخت، سایزینگ، و تحلیل.
""")

# -----------------------
# فایل نقشه یا تصویر
# -----------------------
file = st.file_uploader("📤 تصویر پلان یا طراحی را آپلود کنید (JPEG یا PNG)", type=["jpg", "jpeg", "png"])

if file:
    image = Image.open(file)
    st.image(image, caption="پلان آپلود شده", use_column_width=True)
    st.success("تصویر با موفقیت بارگذاری شد ✅")

# -----------------------
# اطلاعات پروژه
# -----------------------
st.subheader("📋 اطلاعات پروژه")

width = st.number_input("عرض محیط (cm)", min_value=50, max_value=1000, value=300)
height = st.number_input("ارتفاع سقف (cm)", min_value=200, max_value=400, value=280)
depth = st.number_input("عمق پیشنهادی کابینت (cm)", min_value=30, max_value=100, value=60)
style = st.selectbox("سبک طراحی موردنظر", ["مدرن", "کلاسیک", "مینیمال", "ترکیبی"])
color = st.color_picker("🎨 رنگ غالب پیشنهادی", "#ffffff")

# -----------------------
# پردازش هوشمند (نمایشی)
# -----------------------
if st.button("🚀 دریافت پیشنهاد اولیه"):
    st.subheader("🤖 تحلیل و پیشنهاد اولیه")

    st.markdown(f"""
    ✅ **ابعاد محیط:** {width}cm x {depth}cm با ارتفاع {height}cm  
    ✅ **سبک طراحی:** {style}  
    ✅ **رنگ غالب:** <span style='background-color:{color}; padding:2px 10px;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>  
    ✅ **تعداد کابینت پیشنهادی:** حدود {int(width / 60)} عدد  
    ✅ **حداکثر ارتفاع مجاز یونیت‌ها:** {int(height * 0.9)}cm  
    ✅ **مناسب برای:** اجرای CNC، MDF دوبل، باکس‌های قابل جداسازی
    """, unsafe_allow_html=True)

    st.info("برای تحلیل دقیق‌تر نقشه و نقشه برش، نسخه پیشرفته را فعال کنید یا با تیم فنی تماس بگیرید.")

# -----------------------
# Footer
# -----------------------
st.markdown("""
---
📞 [تماس با ما](mailto:youremail@example.com) | 💡 توسعه یافته توسط تیم هوش‌مصنوعی برای کابینت‌سازی آینده‌نگر
""")
