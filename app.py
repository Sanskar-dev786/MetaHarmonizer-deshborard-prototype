import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="MetaHarmonizer Demo", layout="wide")

st.title("MetaHarmonizer Curator Dashboard (Prototype)")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Upload", "Mapping Review", "Ontology", "Quality", "Export"]
)

# ---------------- UPLOAD ---------------- #

with tab1:

    st.header("Upload Metadata")

    file = st.file_uploader("Upload CSV file", type=["csv"])

    if file:
        df = pd.read_csv(file)

        st.session_state["df"] = df

        st.success("File loaded")

        st.write(df.head())


# ---------------- MAPPING ---------------- #

with tab2:

    st.header("Mapping Review")

    if "df" in st.session_state:

        df = st.session_state["df"]

        columns = df.columns

        mapping = []

        for c in columns:

            conf = round(random.uniform(0.4, 0.95), 2)

            if conf > 0.8:
                status = "accepted"
            elif conf > 0.6:
                status = "pending"
            else:
                status = "low"

            stage = random.choice(["S1", "S2", "S3"])

            mapping.append({
                "raw_column": c,
                "matched_field": c.lower(),
                "confidence": conf,
                "stage": stage,
                "status": status
            })

        map_df = pd.DataFrame(mapping)

        show_low = st.checkbox("Show only low confidence")

        if show_low:
            map_df = map_df[map_df["confidence"] < 0.7]

        st.write("Edit mappings")

        edited = st.data_editor(
            map_df,
            num_rows="dynamic",
            use_container_width=True
        )

        st.session_state["mapping"] = edited

    else:
        st.info("Upload file first")


# ---------------- ONTOLOGY ---------------- #

with tab3:

    st.header("Ontology Mapping")

    if "mapping" in st.session_state:

        m = st.session_state["mapping"]

        data = []

        for v in m["raw_column"]:

            data.append({
                "value": v,
                "ontology_term": v.upper(),
                "score": round(random.uniform(0.5, 0.95), 2)
            })

        onto = pd.DataFrame(data)

        st.data_editor(onto, use_container_width=True)

    else:
        st.info("No mapping available")


# ---------------- QUALITY ---------------- #

with tab4:

    st.header("Quality Dashboard")

    if "mapping" in st.session_state:

        m = st.session_state["mapping"]

        total = len(m)

        accepted = (m["status"] == "accepted").sum()
        pending = (m["status"] == "pending").sum()
        low = (m["status"] == "low").sum()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total", total)
        col2.metric("Accepted", accepted)
        col3.metric("Pending", pending)
        col4.metric("Low", low)

        st.subheader("Confidence")

        st.bar_chart(m["confidence"])

    else:
        st.info("No data")


# ---------------- EXPORT ---------------- #

with tab5:

    st.header("Export")

    if "mapping" in st.session_state:

        m = st.session_state["mapping"]

        st.write(m)

        csv = m.to_csv(index=False)

        st.download_button(
            "Download CSV",
            csv,
            file_name="harmonized.csv",
            mime="text/csv"
        )

    else:
        st.info("Nothing to export")