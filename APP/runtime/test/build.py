#!/usr/bin/python

import os
import sys
import getpass
import subprocess

try:
	from fabricate import *
except ImportError, e:
	print "Couldn't find the fabricate module."
	sys.exit(1)

sender_sources = ['sender.c']
receiver_sources = ['receiver.c']
#sqlreceiver_sources = ['sql_receiver.c']
includes = []

#ldflags = ['-lsqlite3']


cflags = ['-ggdb', '-O2', '-fPIC', 
		  '-std=gnu99', '-Wall', '-Werror'] + includes 

def build():
	objects = compile(sender_sources)
	link(objects, "sender")
	objects = compile(receiver_sources)
	link(objects, "receiver")
#	objects = compile(sqlreceiver_sources)
#	link(objects, "sql_receiver")

def compile(sources):
	for source in sources:
		run('gcc', cflags, '-c', source, '-o', source.replace('.c', '.o'))
	objects = [s.replace('.c', '.o') for s in sources]
	return objects

def link(objects, target):
	run('gcc', ldflags, objects, '-o', target)

def clean():
	autoclean()


if __name__ == '__main__':
	main()
