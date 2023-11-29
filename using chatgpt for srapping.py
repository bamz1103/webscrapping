from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open("Amazon.html", "r", encoding="utf8") as file:
    html_content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "lxml")

# Find all divs with the specified class
divs = soup.find_all("div", class_="puisg-col-inner")

# Create an Excel file
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write headers 
sheet["A1"] = "Product Name"
sheet["B1"] = "Product Price"

# Loop through the divs
for i, div in enumerate(divs, start=2):
    # Find the span tag for product name
    span_name = div.find("span", class_="a-size-medium a-color-base a-text-normal")
    product_name = span_name.text.strip() if span_name else ""

    # Find the span tag for product price
    span_price = div.find("span", class_="a-offscreen")
    product_price = span_price.text.strip() if span_price else ""

    # Write the data to the Excel file
    sheet[f"A{i}"] = product_name
    sheet[f"B{i}"] = product_price

# Save the Excel file
workbook.save("product_data.xlsx") 
