import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

app = QApplication(sys.argv)
w = QTextBrowser()

# DB type, host, user, password...
db = QSqlDatabase.addDatabase("QMYSQL");
db.setHostName("localhost")
db.setDatabaseName("testdbmysql")
db.setUserName("root")
db.setPassword("admin")
ok = db.open()

# True if connected
if ok:
	w.insertHtml('Connected to MySQL<br />')
else:
	w.insertHtml('ERROR connecting to MySQL<br />')

# do a query "on" a DB connection
query = QSqlQuery(db)
query.exec_("CREATE TABLE `testdbmysql`.`new_table` (`idnew_table` INT UNSIGNED NOT NULL, PRIMARY KEY (`idnew_table`));")
#CREATE TABLE `testdbmysql`.`erw` (
 # );
if query.exec_("SHOW TABLES"):
	w.insertHtml('<br />')
	while query.next():
		table = query.value(0).toString()
		w.insertHtml('%s<br />' % table)

	w.insertHtml('<br />')
	w.insertHtml('TOTAL %s TABLES' % query.size())

w.show()
sys.exit(app.exec_())