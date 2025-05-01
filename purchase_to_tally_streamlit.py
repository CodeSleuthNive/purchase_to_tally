import streamlit as st
import pandas as pd
import io


def purchase_to_tally(input_file):
    df = pd.read_excel(input_file)

    # Fix the date column
    df['Date'] = pd.to_datetime(df['Date'].astype(str).str[:10])
    df = df.rename(columns={'Vch No.': 'voucher_no'})

    grouped = df.groupby('voucher_no')
    result = []

    for voucher_no, group in grouped:
        row = group.iloc[0]
        voucher_date = row['Date'].date()
        reference_no = row['voucher_no']
        ledger_name = row['Particulars']
        taxable = float(row['Taxable']) if pd.notna(row['Taxable']) else 0.0
        cgst = float(row['CGST']) if pd.notna(row['CGST']) else 0.0
        sgst = float(row['SGST']) if pd.notna(row['SGST']) else 0.0
        igst = float(row['IGST']) if pd.notna(row['IGST']) else 0.0
        total_amount = taxable + cgst + sgst + igst

        result.append({
            "Voucher Date": voucher_date,
            "Voucher Type Name": "Inward Register",
            "Reference No.": reference_no,
            "Ledger Name": ledger_name,
            "Ledger Amount": round(total_amount, 2),
            "Ledger Amount Dr/Cr": "Cr",
            "Change Mode": "Accounting Invoice"
        })

        result.append({"Voucher Date": "", "Voucher Type Name": "", "Reference No.": "", "Ledger Name": "PURCHASE", "Ledger Amount": round(taxable, 2), "Ledger Amount Dr/Cr": "Dr", "Change Mode": ""})
        result.append({"Voucher Date": "", "Voucher Type Name": "", "Reference No.": "", "Ledger Name": "INPUT CGST", "Ledger Amount": round(cgst, 2), "Ledger Amount Dr/Cr": "Dr", "Change Mode": ""})
        result.append({"Voucher Date": "", "Voucher Type Name": "", "Reference No.": "", "Ledger Name": "INPUT SGST", "Ledger Amount": round(sgst, 2), "Ledger Amount Dr/Cr": "Dr", "Change Mode": ""})
        result.append({"Voucher Date": "", "Voucher Type Name": "", "Reference No.": "", "Ledger Name": "INPUT IGST", "Ledger Amount": round(igst, 2), "Ledger Amount Dr/Cr": "Dr", "Change Mode": ""})

    return pd.DataFrame(result)


# Streamlit App
st.set_page_config(page_title="Purchase to Tally Converter", layout="centered")
st.title("📥 Purchase Register to Tally Converter")

uploaded_file = st.file_uploader("Upload Purchase Register Excel File", type=[".xlsx"])

if uploaded_file:
    st.success("File uploaded successfully!")
    processed_df = purchase_to_tally(uploaded_file)
    st.write("### Preview of Processed Data")
    st.dataframe(processed_df.head(50))

    output = io.BytesIO()
    processed_df.to_excel(output, index=False)
    output.seek(0)

    st.download_button(
        label="📤 Download Tally Format Excel",
        data=output,
        file_name="tally_purchase_register.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
