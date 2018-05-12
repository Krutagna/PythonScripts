import pymysql
import os
import html
import smtplib

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='sondb')

cur = conn.cursor()

#mysql query

query = ("""SELECT * FROM servers_list where inprod = 'Y' and (free_memory / 1024 < 3 or free_swap / 1024 < 3 or free_total / 1024 < 3 or disk_perc > 90 or cpu_usage > 90) and type = 'Application'""")

cur.execute(query)

rows = cur.fetchall()

for row in rows:
    for col in row:
        print "%s," % col
    print "\n"

htmlcode = HTML.servers_list(rows)

print htmlcode


content = 'email report'

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('email@email.com', 'pw')

mail.sendmail('email@email.com', 'email@email.com', htmlcode)

mail.close()






















# from ConnectDB import ConnectDB
# from EmailEngine import EmailEngine

# conn_detail = { 'user': 'root',  'password': 'root',  'host': '127.0.0.1',  'database': 'sondb', 'port': 3306}
# dbConnection = ConnectDB(conn_detail)
# print "connection established"

# query='SELECT count(0) FROM servers_list where inprod = "Y" and (free_memory / 1024 < 3 or free_swap / 1024 < 3 or free_total / 1024 < 3 or disk_perc > 90 or cpu_usage > 90) and type = "Application"'
# args = ()
# stoppedInstances = dbConnection.select(query = query, args = args)	
# print stoppedInstances



# db = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "root", db = "sondb")

# cur = db.cursor()

# print cur.execute("SELECT count(0) FROM servers_list where inprod = 'Y' and (free_memory / 1024 < 3 or free_swap / 1024 < 3 or free_total / 1024 < 3 or disk_perc > 90 or cpu_usage > 90) and type = 'Application'")

# if cur.rowcount > 0:
# 	try:
# 		html_content = "<html> <body>"
# 		html_content += "<font face='calibri' size = '3'>Hello,<br /><br />Below mentioned servers have abnormal current usage of Memory / CPU / Disk Space.<br /><br />"
# 		html_content += "<table border='1'><tr bgcolor=yellow><th><font color='grey' face='calibri' size = '3'>Market</font></th><th><font color='grey' face='calibri' size = '3'>Vendor</font></th><th><font color='grey' face='calibri' size = '3'>Tech</font></th><th><font color='grey' face='calibri' size = '3'>Host</font></th><th><font color='grey' face='calibri' size = '3'>OSS</font></th><th><font color='grey' face='calibri' size = '3'>Free Memory (GB)</font></th><th><font color='grey' face='calibri' size = '3'>Free Swap (GB)</font></th><th><font color='grey' face='calibri' size = '3'>Total Free Memory (GB)</font></th><th><font color='grey' face='calibri' size = '3'>% Used Disk</font></th><th><font color='grey' face='calibri' size = '3'>CPU Usage</font></th></tr>"
# 		html_content += "</body> </html>"

# 		query = cur.execute("SELECT Market, if(vendor='E','ERC','NOK') as Vendor, trim(replace(Tech,'Nokia','')) as Tech, Host, OSS, round(free_memory/1024,2) as free_memory, round(free_swap/1024,2) as free_swap, round(free_total/1024,2) as free_total, disk_perc, cpu_usage from servers_list where inprod = 'Y' and (free_memory / 1024 < 3 or free_swap / 1024 < 3 or free_total / 1024 < 3 or disk_perc > 90 or cpu_usage > 90) and type = 'Application'")
# 		if query.return_rows:

# 			html_content += "<tr><td><font face='calibri' size = '3'>" + rs1.getString("Market")
# 								+ "</font></td><td><font face='calibri' size = '3'>" + rs1.getString("Vendor")
# 								+ "</font></td><td><font face='calibri' size = '3'>" + rs1.getString("Tech")
# 								+ "</font></td><td><font face='calibri' size = '3'>" + rs1.getString("Host")
# 								+ "</font></td><td><font face='calibri' size = '3'>" + rs1.getString("OSS")
# 								+ "</font></td>"


# 			return html_content
# 		else:
# 			return "row empty"
# 		info['content'] = { "type": "text/html", "body": html_content}

# 		info['content'] = []

# 		return info


# 	except Exception,e:
# 		print "Error: ", str(e)



		