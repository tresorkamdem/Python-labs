# Week 7 – Files, Exceptions & Logging

This week focuses on:
- File handling
- Exception management
- Logging
- Basic security analysis

---

## Exercise 1 – Product Pricing Manager

### Description
Reads product data from `products.txt`, applies category and tier discounts,
and generates a formatted pricing report.

### Input File
products.txt format:
ProductName,BasePrice,Category,DiscountTier

Example:
Laptop Computer,999.99,Electronics,Premium

### Output
- pricing_report.txt
- Console summary (total products and average discount)

### Features
- Uses `with open()` for file handling
- Handles FileNotFoundError and ValueError
- Applies category and tier-based discounts
- Generates formatted report

### Run
```bash
python product_pricing.py
```

---

## Exercise 2 – Log Analyzer

### Description
Analyzes a server log file and detects:

- Forbidden access attempts
- SQL injection attempts
- Brute force login attempts
- Processing errors

### Input
server.log

### Output Files
- security_incidents.txt
- error_log.txt
- summary_report.txt
- analysis_audit.log

### Features
- Line-by-line log parsing
- Regex pattern matching
- Security detection logic
- Exception handling
- Logging with different levels (INFO, WARNING, ERROR)

### Run
```bash
python log_analyzer.py
```

---

## Exercise 3 – File Audit Tool

### Description
Scans a directory and generates an audit report including:

- Total files
- Total size
- Python files count
- Largest file
- Files modified in last 24h

### Output
- audit_report.txt

### Features
- Uses os and datetime modules
- Handles invalid directories
- Clean formatted output
- Proper exception handling

### Run
```bash
python file_audit.py
```

---

## Concepts Covered

- File operations
- Try/except blocks
- Logging module
- Regular expressions
- Basic security analysis
- Directory scanning with os
- Report generation

---

Author: [kamdem]  
Course: Python Programming  
Week: 7