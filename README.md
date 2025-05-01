# Purchase to Tally Converter

## Overview

The **Purchase to Tally Converter** is a Streamlit-based web application that allows users to upload purchase register Excel files and convert them into Tally-compatible voucher entries. The app processes each voucher, calculates tax components (CGST, SGST, IGST), and generates a structured Excel sheet ready for import into accounting systems like Tally.

---

## Features

- 📤 Upload Excel purchase register
- 📅 Automatic date parsing
- 🧾 Group by voucher number
- 🧮 Tax calculation for CGST, SGST, IGST
- 📥 Download Tally-ready Excel output

---

## Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/purchase-to-tally-converter.git
cd purchase-to-tally-converter
```

2. **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit App**

```bash
streamlit run app.py
```

---

## Usage

1. Open the app in your browser (usually at `http://localhost:8501`)
2. Upload your Excel purchase register file
3. Click **Convert to Tally Format**
4. Download the processed Excel file

---

## Input Excel Format

Your Excel sheet must contain the following columns:

| Column Name | Description |
|-------------|-------------|
| Date | Invoice date (any format) |
| Vch No. | Voucher number |
| Particulars | Vendor or ledger name |
| Taxable | Taxable amount |
| CGST | Central GST |
| SGST | State GST |
| IGST | Integrated GST |

---

## Output Excel Format

The output file will contain:

| Column | Description |
|--------|-------------|
| Voucher Date | Parsed from the original `Date` column |
| Voucher Type Name | Always "Inward Register" |
| Reference No. | From the original voucher |
| Ledger Name | Vendor or tax-related entries |
| Ledger Amount | Calculated per entry |
| Ledger Amount Dr/Cr | "Cr" for vendor, "Dr" for others |
| Change Mode | "Accounting Invoice" for first row |

---

## File Structure

```
purchase-to-tally-converter/
├── app.py                  # Streamlit app
├── processor.py            # purchase_to_tally function
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Dependencies

- `streamlit`
- `pandas`
- `openpyxl`
- `xlsxwriter`

Install using:

```bash
pip install -r requirements.txt
```

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## License

This project is open-source and available under the MIT License.
