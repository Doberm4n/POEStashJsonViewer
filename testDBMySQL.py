import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

app = QApplication(sys.argv)
w = QTextBrowser()

# DB type, host, user, password...
db = QSqlDatabase.addDatabase("QMYSQL");
db.setHostName("localhost")
db.setDatabaseName("test")
db.setUserName("root")
db.setPassword("")
ok = db.open()

# True if connected
if ok:
	w.insertHtml('Connected to MySQL<br />')
else:
	w.insertHtml('ERROR connecting to MySQL<br />')

# do a query "on" a DB connection
query = QSqlQuery(db)
if query.exec_("SHOW TABLES"):
	w.insertHtml('<br />')
	while query.next():
		table = query.value(0).toString()
		w.insertHtml('%s<br />' % table)

	w.insertHtml('<br />')
	w.insertHtml('TOTAL %s TABLES' % query.size())

w.show()
sys.exit(app.exec_())