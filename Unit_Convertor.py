import streamlit as st

# Stylish CSS for modern look
st.markdown(
    """
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stApp {
        background: linear-gradient(120deg, #10131a 0%, #1f1f2e 100%);
        color: white;
    }
    .main-container {
        background: rgba(255, 255, 255, 0.06);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(8px);
        margin: 25px;
    }
    h1 {
        text-align: center;
        font-size: 38px;
        color: #ffffff;
        text-shadow: 1px 2px 6px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    h2 {
        color: #4dd0e1;
        font-size: 24px;
        margin-top: 20px;
    }
    .stButton>button {
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px;
        border-radius: 10px;
        border: none;
        width: 100%;
        box-shadow: 0px 5px 15px rgba(0, 242, 254, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 8px 20px rgba(0, 242, 254, 0.6);
    }
    .result-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(to right, #43cea2, #185a9d);
        padding: 20px;
        border-radius: 15px;
        margin-top: 30px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        color: white;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        font-size: 16px;
        color: rgba(255, 255, 255, 0.7);
        border-top: 1px solid rgba(255, 255, 255, 0.2);
    }
    .description {
        font-size: 18px;
        line-height: 1.7;
        margin-bottom: 25px;
        color: rgba(255, 255, 255, 0.85);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# UI Layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown("<h1>🌟 Smart Unit Converter 🌡️📐⚖️</h1>", unsafe_allow_html=True)

st.markdown(
    '<p class="description">Convert any value instantly. Choose the type, input your number, and see the result right away. Fast, easy and for everyone!</p>',
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.markdown("## ⚙️ Choose Conversion")
conversion_type = st.sidebar.selectbox(
    "Pick Conversion Type", ["📏 Length", "⚖️ Weight", "🌡️ Temperature"]
)

conversion_type_clean = conversion_type.split(" ")[1]
st.markdown(f"<h2>{conversion_type}</h2>", unsafe_allow_html=True)

value = st.number_input("Enter value to convert:", value=0.0, min_value=0.0, step=0.1, format="%.4f")

col1, col2 = st.columns(2)

# Dropdowns
if conversion_type_clean == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Miles", "Yards", "Feet", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Miles", "Yards", "Feet", "Inches"])
elif conversion_type_clean == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Gram", "Milligram", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Gram", "Milligram", "Pounds", "Ounces"])
elif conversion_type_clean == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Logic
def length_converter(val, f, t):
    base = {'Meter': 1, 'Kilometer': 0.001, 'Centimeter': 100, 'Millimeter': 1000, 'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701}
    return (val / base[f]) * base[t]

def weight_converter(val, f, t):
    base = {'Kilogram': 1, 'Gram': 1000, 'Milligram': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274}
    return (val / base[f]) * base[t]

def temp_converter(val, f, t):
    if f == t:
        return val
    if f == "Celsius":
        return (val * 9/5 + 32) if t == "Fahrenheit" else val + 273.15
    elif f == "Fahrenheit":
        return (val - 32) * 5/9 if t == "Celsius" else (val - 32) * 5/9 + 273.15
    elif f == "Kelvin":
        return val - 273.15 if t == "Celsius" else (val - 273.15) * 9/5 + 32
    return val

# Result
result = None
if st.button("🔁 Convert Now"):
    with st.spinner("Calculating..."):
        if conversion_type_clean == "Length":
            result = length_converter(value, from_unit, to_unit)
        elif conversion_type_clean == "Weight":
            result = weight_converter(value, from_unit, to_unit)
        elif conversion_type_clean == "Temperature":
            result = temp_converter(value, from_unit, to_unit)

if result is not None:
    formatted = f"{result:.6f}" if abs(result) < 0.01 else f"{result:.2f}".rstrip('0').rstrip('.')
    emoji = "📏" if conversion_type_clean == "Length" else "⚖️" if conversion_type_clean == "Weight" else "🌡️"
    st.markdown(f"<div class='result-box'>{emoji} {value} {from_unit} = {formatted} {to_unit} {emoji}</div>", unsafe_allow_html=True)
    
# useful information based on conversion type
if conversion_type_clean == "Length":
    st.markdown("### 📝 Length Conversion Facts")
    st.markdown("- 1 Mile = 1.60934 Kilometers")
    st.markdown("- 1 Meter = 3.28084 Feet")
    st.markdown("- 1 Inch = 2.54 Centimeters")
elif conversion_type_clean == "Weight":
    st.markdown("### 📝 Weight Conversion Facts")
    st.markdown("- 1 Kilogram = 2.20462 Pounds")
    st.markdown("- 1 Pound = 16 Ounces")
    st.markdown("- 1 Kilogram = 1000 Grams")
elif conversion_type_clean == "Temperature":
    st.markdown("### 📝 Temperature Conversion Facts")
    st.markdown("- Water freezes at 0°C = 32°F = 273.15K")
    st.markdown("- Water boils at 100°C = 212°F = 373.15K")
    st.markdown("- Room temperature is about 20-25°C = 68-77°F = 293-298K")

# Footer 
st.markdown(
    "<div class='footer'>✨ Made with love by Shoaib Tahir — Thanks for using this tool! ❤️</div>", 
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
