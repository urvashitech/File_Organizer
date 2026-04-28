import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


file_path = "sales.csv"   

df = pd.read_csv(file_path)   


total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
sales_by_product = df.groupby("Product")["Sales"].sum()


report = f"""
📊 Daily Sales Report

Total Sales: {total_sales}
Average Sales: {average_sales:.2f}

Sales by Product:
{sales_by_product.to_string()}
"""


sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
app_password = "your_app_password"   
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "📊 Automated Daily Report"

msg.attach(MIMEText(report, "plain"))


try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)

    server.send_message(msg)
    server.quit()

    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Error sending email:", e)