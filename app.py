import streamlit as st

st.set_page_config(
    page_title="Sayari Diesel Trade Investigation",
    page_icon="🔎",
    layout="wide"
)

st.title("Could Diesel Be Tracked from Iran to Russia?")

st.write(
    "A first-iteration investigation using Sayari Graph trade data "
    "to examine petroleum-product shipments and possible routes."
)

st.header("Research question")

st.write(
    "Can Sayari Graph identify diesel or petroleum-product trade "
    "relationships connecting Iran and Russia?"
)

st.header("Search method")

st.markdown("""
- Product category: Diesel and petroleum products
- HS code: 2710.19
- Shipper country: Iran
- Receiver country: Russia
""")

st.header("Finding")

st.warning(
    "One reviewed shipment involved an Iranian shipper and Diesel fuel K-4, "
    "but the listed arrival country was Uzbekistan. Therefore, it is not "
    "direct evidence of an Iran-to-Russia shipment."
)

st.header("Conclusion")

st.write(
    "The results support an Iran-linked regional petroleum-trade network, "
    "but additional records would be needed to confirm a direct "
    "Iran-to-Russia diesel route."
)
