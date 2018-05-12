SERVER = "127.0.01.1"
FROM = "kpurohit@ttswireless.com"
TO = ["krutagnapurohit@gmail.com", ""st

SUBJECT = "Subject"
TEXT = "Your Text"

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()



# def main():
# 	try:
		# global conn_detail
		# conn_detail = { 'user': 'root',  'password': 'root',  'host': '127.0.0.1',  'database': 'sondb', 'port': 3306}
		# dbConnection = ConnectDB(conn_detail)
		# print "connection established"
		# query='SELECT count(0) FROM servers_list where inprod = "Y" and (free_memory / 1024 < 3 or free_swap / 1024 < 3 or free_total / 1024 < 3 or disk_perc > 90 or cpu_usage > 90) and type = "Application"'
		# args = ()
		# stoppedInstances =dbConnection.select(query = query, args = args)

		# if stoppedInstances>0:
			# emailEngine = EmailEngine()
			# failed_instances_table = get_user_failed_instances()   
			# email_detail = get_email_detail(failed_instances_table)
			# status_code = emailEngine.send_email(email_detail) # returns status code of email
			# print status_code
			# if status_code == 202: # Sendgrid gives 202 status if email successfully queued/sent
			# 	self.log ("Alert Email Sent Successfully to User Email -> {}...".format(user_email))
			# else:
			# 	self.log ("ERROR : Status code.." + str(status_code))
			# 	self.log ("ERROR : Sending email alert to User Email -> {}.. Please check logs..".format(user_email))
# 	except Exception,e:
# 		print "Error: ", str(e)


# if __name__ == '__main__':
# 	main()


















# #!/usr/bin/env python
# import sys
# import mysql.connector
# from collections import Counter, defaultdict

# def PrintFields(database, table):
#     """ Connects to the table specified by the user and prints out its fields in HTML format used by Ben's wiki. """
#     conn = mysql.connector.connect(user='root', password='root',host='127.0.0.1',port='3306', database='sondb')
#     cur = conn.cursor()
#     sql = """ SELECT Market, if(vendor='E','ERC','NOK') as Vendor, trim(replace(Tech,'Nokia','')) as Tech, Host, OSS, round(free_memory/1024,2) as free_memory, round(free_swap/1024,2) as free_swap, round(free_total/1024,2) as free_total, disk_perc, cpu_usage from servers_list where inprod = 'Y' and (free_memory / 1024 < 3 or free_swap / 1024 < 3 or free_total / 1024 < 3 or disk_perc > 90 or cpu_usage > 90) and type = 'Application' """
#     cur.execute(sql)
#     fields=cur.fetchall()
#     # print '<table border="0"><tr><th>order</th><th>name</th><th>type</th><th>description</th></tr>'
    # print '<tbody>'

    # counter = Counter(fields)
    # html_content = defaultdict(int)
    # print "<table>"
    # for word in counter.keys():
    # 	print "<tr>"
    # 	print "<td>" +str(word)+ ":" + str(counter[word]) +"</td>"
    # 	print "</tr>"
    # 	html_content[word] = counter[word]
    # print "</table>"

    # print '</tbody>'
    # print '</table>'
    # print fields
#     cur.close()
#     conn.close()

# users_database = sys.argv[1]
# users_table = sys.argv[2]
# print "Wikified HTML for " + users_database + "." + users_table
# print "========================"
# PrintFields(users_database, users_table)





# html = """<HTML>
# <body>
#     <h1>Attendance list</h1>
#     <table>
#         {0}
#     </table>
# </body>
# </HTML>"""

# items = [['Jason', 'Brown', 'Leeds', '40'], ['Sarah', 'Robinson', 'Bristol', '32'], ['Carlo', 'Baldi', 'Manchester', '41']]
# tr = "<tr>{0}</tr>"
# td = "<td>{0}</td>"
# subitems = [tr.format(''.join([td.format(a) for a in item])) for item in items]





# row = ",".join([unicode(r) for r in stoppedInstances])
		# print row



for s in sent:
    sentence = ''.join(filter(lambda x: x.isalpha() or x in [' ', "'"], list(s)))
    words = sentence.lower().split(' ')
    shared_words = set(words) & set(newsorted)
    if bool(shared_words):
        print("------\n" + s)















# import mysql.connector
 
# try:
# 	conn = mysql.connector.connect(user='root', password='root',
# 								  host='127.0.0.1',port='3306',
# 								  database='sondb',charset="utf8", use_unicode = True)
# 	cursor = conn.cursor()
# 	query = """ SELECT * from servers_list"""
# 	args = ()
# 	stoppedInstances =dbConnection.select(query = query, args = args)	
# 	print stoppedInstance
# 	cursor.execute(query)
# 	print query
# 	cursor.close()
# 	conn.close()
# except Exception,e:
# 	print "Error:",str(e)

#take list of lists as argument	
# def nlist_to_html(list2d):
# 	#bold header
# 	htable=u'<table border="1" bordercolor=000000 cellspacing="0" cellpadding="1" style="table-layout:fixed;vertical-align:bottom;font-size:13px;font-family:verdana,sans,sans-serif;border-collapse:collapse;border:1px solid rgb(130,130,130)" >'
# 	list2d[0] = [u'<b>' + i + u'</b>' for i in list2d[0]] 
# 	for row in list2d:
# 		newrow = u'<tr>' 
# 		newrow += u'<td align="left" style="padding:1px 4px">'+unicode(row[0])+u'</td>'
# 		row.remove(row[0])
# 		newrow = newrow + ''.join([u'<td align="right" style="padding:1px 4px">' + unicode(x) + u'</td>' for x in row])  
# 		newrow += '</tr>' 
# 		htable+= newrow
# 	htable += '</table>'
# 	return htable
	
 
 
# def sql_html(query):
# 	print nlist_to_html(query_mysql(query))





# #!/usr/bin/env python
# import mysql.connector
# import smtplib

# db = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "root", db = "sondb")

# cur = db.cursor()

# cur.execute("SELECT * from servers_list")

# for row in cur.fetchall():
# 	print row[0]

# db.close()


# output = "<html><body><table>"
# for key in cur:
#   output += "<tr><td>%s</td><td>%s</td></tr>"
# output += "</table></body></html>"
# print output