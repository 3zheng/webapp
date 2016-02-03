#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wu Liao'

import time, uuid, functools, threading, logging
import MySQLdb

g_engine = None

'''
def create_engine(user, password, database, host='127.0.0.1', port=3306, **kw):
	global g_engine
	if g_engine is not None
		raise DBError('Engine is already initialized.')
	g_engine = MySQLdb.connect(host, user, password, database)
	with g_engine:
		cur = g_engine.cursor()
		cur.execute('create table user (id varchar(20) primary key, name varchar(20))')
		cur.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
		cur.rowcount
		conn.commit()
		cur.close()
'''
class _Engine(object):
	def __init__(self, host, user, password, database):
		self.host = host
		self.user = user
		self.password = password
		self.database = database
	
	def connect()
		return MySQLdb.connect(self.host, self.user, self.password, self.database)

def create_engine(user, password, database, host='127.0.0.1', port=3306, **kw):
	global g_engine
	if g_engine is not None
		raise DBError('Engine is already initialized.')
	g_engine = _Engine(host, user, password, database)
		
class _LasyConnection(object):
	def __init__(self):
		self.connection = None
		if g_engine is None:
			print '_LasyConnection __init__ failed, use create_engine first, then connection'
		
	def cursor(self):
		if self.connection is None:
			connection = engine.connect()
            logging.info('open connection <%s>...' % hex(id(connection)))
			self.connection = connection
		return self.connection.cursor()
	
	def cleanup(self):
	
	def commit(self):
	
	def rollback(self):

	
class _DbCtx(threading.local):
	def __init__(self):
		self.connection = None
		self.transactions = 0
		
	def is_init(self):
		return self.connection is not None
	
	def init(self):
		logging.info('open lazy connection...')
		if self.connection is None
			self.connection = _LazyConnection()
			self.transactions = 0
			
	def cleanup(self):
		self.connection.cleanup();
		self.connection = None
	
	def cursor(self):
		return self.connection().cursor()

		
g_db_ctx = _DbCtx()

class _ConnectionCtx(object):
	def __enter__(self):
		global g_db_ctx
		self.should_cleanup = False	#should_cleanup数据库链接是否需要释放的标志位
		if not g_db_ctx.is_init():
			g_db_ctx.init()
			self.should_cleanup = True
		return self
	
	def __exit__(self, exctype, excvalue, traceback):
		global g_db_ctx
		if self.should_cleanup:
			g_db_ctx.cleanup()
			

def connection()
	return _ConnectionCtx();