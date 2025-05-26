This Python project scrapes the first six real estate projects listed on the [Odisha RERA website](https://rera.odisha.gov.in/projects/project-list) and extracts important information including:

- Project Name  
-  RERA Registration Number  
-  Promoter Name  
-  Promoter Address  
-  GST Number  

##  Tools Used

- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/) for browser automation
- [fpdf](https://py-pdf.github.io/fpdf2/) for generating PDF report
- [csv](https://docs.python.org/3/library/csv.html) for saving data in CSV format

##  Output Files

- `rera_projects.csv` – Extracted project details in tabular format.
- `rera_projects_report.pdf` – Professionally formatted PDF report.

## 🚀 How to Run

1. Clone this repository:
    ```bash
    git clone https://github.com/your-avani-10/rera-project-scraper.git
    cd rera-project-scraper
    ```

2. Install the required packages:
    ```bash
    pip install selenium fpdf
    ```

3. Ensure you have ChromeDriver installed and accessible in your system's PATH.

4. Run the script:
    ```bash
    python rera_scraper.py
    ```

##  Notes

- This script opens each project detail in a new tab to avoid reloading the main list.
- Basic error handling is included to skip missing details.

##  Developed By

**Avani Aggarwal**  
B.Tech (EEE) | BMS Institute of Technology  
GitHub: [avani-10](https://github.com/your-avani-10)

---

✨ Feel free to fork and enhance the project for your own region’s RERA portal.
