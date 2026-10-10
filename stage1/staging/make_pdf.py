from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, "Aeon Financial Holdings", ln=True)
pdf.set_font("Helvetica", "B", 13)
pdf.cell(0, 10, "Employee Handbook (Draft)", ln=True)
pdf.ln(5)

pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 8, "Section 1: Introduction", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 7, "This draft is circulated internally during the staging phase of the employee portal migration. Please do not distribute outside the IT team.")
pdf.ln(3)

pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 8, "Section 2: IT Policies", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 7, "All staff must use the internal VPN when accessing staging resources. Contact the helpdesk for staging credentials during the transition period.")
pdf.ln(3)

pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 8, "Section 3: Contacts", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 7, "IT Helpdesk: helpdesk@aeonfinancial.internal")
pdf.ln(3)

pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 8, "Section 4: Attachments", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 7, "See attached staff recognition photo:", ln=True)
pdf.set_text_color(0, 0, 255)
pdf.cell(0, 7, "employee_of_the_month.png", ln=True,
         link="http://localhost:8081/old-staging-portal/employee_of_the_month.png")
pdf.set_text_color(0, 0, 0)

pdf.output("staging/employee_handbook.pdf")
print("PDF created.")
