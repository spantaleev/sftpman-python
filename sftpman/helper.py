import os, errno
import subprocess

def mkdir_p(path):
	"""NOOP if the directory exists. If not, it creates the the whole directory tree."""
	
	try:
		os.makedirs(path)
	except OSError as exc:
 		if exc.errno != errno.EEXIST:
 			raise


def rmdir(path):
	"""Safe rmdir (non-recursive) which doesn't throw if the directory is not empty."""
	
	try:
		os.rmdir(path)
	except OSError as exc:
		print str(exc)
		
		
def shell_exec(command):
	"""Executes the given shell command and returns its output."""
	
	return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]
	
	
def kill_pid(pid, signal=15):
	"""Sends a signal to the process with the given id."""
	
	shell_exec("/bin/kill -%d %d" % (signal, pid))
	

def open_file_browser(path):
	"""Opens a file browser at the specified path."""
	
	subprocess.Popen(["/usr/bin/nautilus", path])
