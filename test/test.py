
a = [1,2,3]
b = [4,5,6]
c = [9,0,1,7,8]

zipped_data = zip(a,c)
print zipped_data


for x,y in zipped_data:
	print('x is ',x)
	#print('y is ',y)

g_engine = None
import MySQLdb
from MySQLdb import FieldType
global g_engine
if g_engine is not None:
	raise DBError('Engine is already initialized.')
g_engine = MySQLdb.connect('127.0.0.1', 'root', '123456', 'test')
with g_engine:
	cur = g_engine.cursor()
	cur.execute('select * from user where id != 0')
	
	if cur.description:
		names = [x[0] for x in cur.description]
		for x in cur.description:
			print FieldType.get_info(x[1]))
			print x
	print names
	for x in cur.fetchall():
		print x
	cur.close()
