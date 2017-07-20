from PyQt4 import QtSql, QtGui
from PyQt4 import QtCore

def createDB():
   print QtSql.QSqlDatabase.isDriverAvailable("QSQLITE")
   db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('sports.db')
   #db.setDatabaseName('DRIVER={SQL Server};SERVER=localhost;DATABASE=testDBDB;UID=;PWD=;')

   if not db.open():
      print 'jtfuffujf'
      print db.lastError().text()
      QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
         QtGui.qApp.tr("Unable to establish a database connection.\n"
            "This example needs SQLite support. Please read "
            "the Qt SQL driver documentation for information "
            "how to build it.\n\n" "Click Cancel to exit."),
         QtGui.QMessageBox.Cancel)

      return False

   query = QtSql.QSqlQuery()



   query.exec_("create table sportsmen(id INTEGER PRIMARY KEY AUTOINCREMENT, "
      "firstname varchar(20), lastname varchar(20))")

   a='?'*2

   #a = [', '.join(i) for i in a]

   #for i in a:
   print a
   a = ', '.join(a)

   print a

   query.prepare("INSERT INTO sportsmen (firstname, lastname) VALUES (" + a + ")")
   # values = [1, '1', '2']
   # values = QtCore.QVariant(values)


   #QSqlQuery query;
   #query.prepare("INSERT INTO numbers (number) VALUES(?)");
   #query.addBindValue(values);

   #query.execBatch()



   #query.prepare(INSERT INTO `table` VALUES (?, ?))

   var=[[1, 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)'], [1, 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)', 1.0, 'QtCore.QVariant(QtCore.QVariant.Double)']]
   #var2=
   print var[0][0]
   query.addBindValue(var[0])
   query.addBindValue(var[1])
   # query.addBindValue(var1)
   # query.addBindValue(var1)
   # query.addBindValue(var1)
   # query.addBindValue(var1)
   # query.addBindValue(var1)
   query.execBatch()




   #print a

   # var1=[1, '.ewq0', 'rwerwe']
   # var2=[2, 'rwerwe', '32.ewq6']

   # #print QtCore.QVariant(var1)

   # query.addBindValue(QtCore.QVariant(var1))
   # query.addBindValue(QtCore.QVariant(var2))
   # query.execBatch()
   # db.transaction()
   # db.commit()

   #query.exec_("insert into sportsmen (firstname, lastname) values('Roger', 'Federer')")
   # query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
   # query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
   # query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
   # query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
   # return True

if __name__ == '__main__':
   import sys

   app = QtGui.QApplication(sys.argv)
   createDB()