# Purchase Register to Tally Converter

## 📘 Overview

The **Purchase Register to Tally Converter** is a Python-based tool designed to convert purchase register Excel files into Tally-compatible formats. It simplifies the accounting process by generating structured voucher entries based on CGST, SGST, IGST, and taxable values for each invoice (voucher).

---

## ⚙️ Features

- 🧾 **Voucher Grouping**: Automatically groups data by voucher numbers.
- 📆 **Date Formatting**: Cleans and standardizes the invoice date field.
- 📑 **Ledger Entries**: Generates Cr/Dr entries for purchase, CGST, SGST, and IGST.
- 📤 **Excel Export**: Outputs a clean `.xlsx` file ready for import into Tally.

---

## 🚀 How to Use

### 1. 📁 Prepare Your Input File

Ensure your input Excel file (`.xlsx`) has the following required columns:

| Column Name | Description |
|-------------|-------------|
| Date        | Invoice date (e.g., 25-04-2025) |
| Vch No.     | Voucher or invoice number |
| Particulars | Ledger name (e.g., Vendor name) |
| Taxable     | Taxable amount for the purchase |
| CGST        | Central GST amount |
| SGST        | State GST amount |
| IGST        | Integrated GST amount |

### 2. ▶️ Run the Script

```bash
pip install pandas openpyxl
python script_name.py  # Replace with actual file name or use in function form
```

Or use it as a function inside a Python script:

```python
from converter import process_csv_to_excel

process_purchase_to_tally("input_file.xlsx", "output_file.xlsx")
```

---

## 📂 Output Excel Format

The generated Excel file contains the following columns:

| Column | Description |
|--------|-------------|
| Voucher Date | Date of the invoice |
| Voucher Type Name | Always set to "Inward Register" for Cr entry |
| Reference No. | Invoice or voucher number |
| Ledger Name | Ledger affected by the entry |
| Ledger Amount | Total value for the ledger |
| Ledger Amount Dr/Cr | "Dr" or "Cr" depending on type |
| Change Mode | Set to "Accounting Invoice" for Cr entry |

---

## 📦 File Structure

```
purchase-register-to-tally/
├── converter.py           # Script containing the conversion function
├── README.md              # This file
├── input_file.xlsx        # Sample input file (user-provided)
├── output_file.xlsx       # Generated output
```

---

## 📋 Dependencies

Install all required packages using pip:

```bash
pip install pandas openpyxl
```

---

## 🛠️ Future Improvements

- Add GUI using Streamlit or Tkinter
- Support `.xlsx` format input
- Add validations and error handling for missing columns

---

## 🙌 Acknowledgments

Thanks to the accounting and automation communities for inspiration.

---

## 📬 Contact

For suggestions or support, feel free to reach out via GitHub Issues or pull requests.
