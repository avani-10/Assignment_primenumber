from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_rera_projects():
    options = Options()
    # Uncomment if you want to see browser working
    # options.add_argument("--headless")

    # If Chrome is not installed in standard location, specify the path like this:
    # options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 20)

    driver.get("https://rera.odisha.gov.in/projects/project-list")

    # Wait for project table to appear
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table#projectsListTable")))

    projects = []
    rows = driver.find_elements(By.CSS_SELECTOR, "table#projectsListTable tbody tr")[:6]

    for idx, row in enumerate(rows, 1):
        try:
            # Scroll and click "View Details"
            view_btn = row.find_element(By.LINK_TEXT, "View Details")
            driver.execute_script("arguments[0].scrollIntoView();", view_btn)
            view_btn.click()

            # Wait for details page to load
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".detail-section")))

            # Extract required fields
            rera_no = driver.find_element(By.XPATH, "//td[contains(text(),'Rera Regd. No')]/following-sibling::td").text.strip()
            project_name = driver.find_element(By.XPATH, "//td[contains(text(),'Project Name')]/following-sibling::td").text.strip()

            # Switch to Promoter Details tab
            promoter_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Promoter Details')]")
            promoter_tab.click()
            time.sleep(1)  # small wait for tab content to load

            promoter_name = driver.find_element(By.XPATH, "//td[contains(text(),'Company Name')]/following-sibling::td").text.strip()
            promoter_address = driver.find_element(By.XPATH, "//td[contains(text(),'Registered Office Address')]/following-sibling::td").text.strip()
            gst_no = driver.find_element(By.XPATH, "//td[contains(text(),'GST No')]/following-sibling::td").text.strip()

            projects.append({
                "Rera Regd. No": rera_no,
                "Project Name": project_name,
                "Promoter Name": promoter_name,
                "Promoter Address": promoter_address,
                "GST No": gst_no,
            })

            # Go back to project list page
            driver.back()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table#projectsListTable")))

        except Exception as e:
            print(f"Error scraping project {idx}: {e}")
            driver.back()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table#projectsListTable")))

    driver.quit()
    return projects

if __name__ == "__main__":
    data = scrape_rera_projects()
    for i, proj in enumerate(data, 1):
        print(f"\nProject {i}:")
        for key, value in proj.items():
            print(f"  {key}: {value}")
