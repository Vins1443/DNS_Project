# 📘 Labour Act Viewer & Document Extractor

This full-stack project extracts structured text from the **Labour Act PDF**, converts it to an indented `.txt` file maintaining hierarchy, and displays it using a React frontend powered by a FastAPI backend.

---

## 🚀 Features

- ✅ Extracts structured text from `Labour Act.pdf`
- ✅ Maintains section hierarchy and indentation
- ✅ Handles bullet point cleanup and formatting
- ✅ FastAPI backend to serve content
- ✅ React UI to render the structured output
- ✅ AWS DMS low-level design (DMS LLD) included

---

## 🗂️ Folder Structure

```
DMS_Project/
├── backend/
│   ├── main.py               # FastAPI backend server
│   └── pdf_parser.py         # PDF parser and formatter
├── documents/
│   └── Labour Act.pdf        # Input PDF
├── frontend/                 # React frontend project
├── output.txt                # Extracted text output
├── requirements.txt          # Python backend dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ Backend Setup (FastAPI + PyMuPDF)

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```

2. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install required packages:
   ```bash
   pip install -r ../requirements.txt
   ```

4. Run the parser to generate `output.txt`:
   ```bash
   python pdf_parser.py
   ```

5. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

6. Open in browser:
   ```
   http://127.0.0.1:8000/file
   ```

---

## 🖥️ Frontend Setup (React)

1. Open a new terminal:
   ```bash
   cd frontend
   npm install
   npm start
   ```

2. View the UI:
   ```
   http://localhost:3000
   ```

---

## ☁️ AWS Document Management System (DMS) – LLD

| Component              | AWS Service               | Purpose                                   |
|-----------------------|---------------------------|-------------------------------------------|
| Document Storage       | Amazon S3                 | Store uploaded documents                  |
| API Backend            | API Gateway + Lambda      | Upload, parse, and manage docs            |
| OCR/Parsing            | Amazon Textract           | Extract structured content from PDFs      |
| User Auth              | Amazon Cognito            | Secure user access                        |
| Metadata DB            | DynamoDB or RDS           | Store file details and search metadata    |
| Search                 | OpenSearch                | Full-text document search                 |
| UI Hosting             | AWS Amplify / S3 + CloudFront | Serve React frontend                    |
| Notification           | SNS / SES                 | Notify users about updates/workflows      |

---

## ✅ Deliverables Summary

- [x] Extract structured text from Labour Act PDF
- [x] Save to output.txt with proper hierarchy
- [x] Display formatted data in browser
- [x] FastAPI + React integration
- [x] AWS DMS architecture plan

---

## 👨‍💻 Author

**Vineet Bothra**  
📧 vineetbothra1443@gmail.com  
🌐 [vineetbothra.com](https://vineetbothra.com)  
💻 [github.com/Vins1443](https://github.com/Vins1443)