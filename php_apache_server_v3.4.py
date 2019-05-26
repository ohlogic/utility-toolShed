import os
import sys
import zipfile
import shutil
import time
# --------------------   PHASER   By: Stan S.

apache_version  = "2.4.12"      # Apache's most recent version checked: 01-30-2015
php_version 	= "5.6.8"	    # PHP version last updated: 02-20-2015 (checked daily)

# PHp_Apache_SERver_V3.4        (9-23-2014) (.1 signifying this python coded version)(coded in python version 2.7.8)
#                                           (.2 update, python code replaces the previous superb gnu utilities that were used)
#                               (12-31-2014)(.3 update, to use the apache_version variable and php_version variable throughout)
#                               (01-16-2015)(.4 update, to use a drive letter to allow installation on drive other than c)
#                               (01-24-2015)(   small change to appearance, put a space between drive and raw string literal +r' to be clear)

# Usage: Place this in a folder of your choosing, perhaps c:\phaser 
#        with the Apache and PHP download zips in the same folder,
#        obtained from http://www.apachelounge.com/download/ and http://windows.php.net/download/ (thread safe version)
#        then run this python script.
#        Verify script runs cleanly without errors, as it does on my machine (note: windows fussy with deleting recently running binaries)
#             If restoring from your own httpd.conf and httpd-vhost.conf files that get backedup by this script, when updating Apache: update the ServerRoot statement line in httpd.conf : When updating PHP: edit both the lines beginning with LoadModule php5_module and PHPIniDir statements in httpd.conf
drive = 'c' # edit to your situation, which hard drive this is being installed to  -  NEW feature

# does the file exist the file is not empty, there's content in it
def empty_file(fpath):  
    return False if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else True

# write to file
def to_file(file, content):
	with open (file, "w") as fp:	# with closes the file
		fp.write(content)
		
# replace text in file
def bake_replace(file, old, new):
	with open (file, "r+") as fp:	# with closes the file
		data=fp.read()
		data = data.replace(old,new)
		fp.seek( 0 )
		fp.write(data)
		fp.truncate()

# find text string and append a newline
def bake_append(file, find, append):
	with open (file, "r+") as fp:	# with closes the file
		data=fp.read()
		data = data.replace(find,find+'\n'+append)
		fp.seek( 0 )
		fp.write(data)

def mkdirp(directory):	
	if not os.path.isdir(directory):
		os.makedirs(directory)
		print 'mkdirp: created directory ' + directory
	else:
		print 'mkdirp: cannot create directory ' + directory + ' : File exists'

def exists(path):
	return True if ( os.path.isfile(path) or os.path.isdir(path)) else False
					
def rmdir(directory, verify = False):

	if os.path.isdir(directory):
		shutil.rmtree(directory)	#deletes directory and its contents, os.rename() removes just empty directory
		print 'rmdir: removed directory ' + directory
	else:
		print 'rmdir: cannot remove directory ' + directory + ' : Directory does not exist'
	
	if (verify):
		is_there = exists(directory)
		print 'rmdir , verifying: does directory exist (' + str(is_there) + ')'
		return is_there

def sep_of_tested_yes_isdir(s): # the condition is that it's a directory, so this asks what's the separator?

	if ( s == '.' or s == '..' ):
		return os.path.sep

	if ( ":" in s ):
		s = s[s.index(':')+1:]
	
	if ( s == "/" or s == "\\" ):
		return s
		
	head, tail = os.path.split(s)  # be careful, this returns "" if the paths ends in "/" or "\", therefore, slight adjustment
	
	done = s[len(head):-len(tail)] # determines the separator of split
	if ( done == ""	):
                               # reversing string for added assurance
		if ( '/'  in s[::-1] ):  
			return '/'
	
		if ( '\\' in s[::-1] ):
			return '\\'
	else:
		return done
		
def cp(source, destination, binary = False):

	if os.path.isfile(source):
	
		if os.path.isfile(source) == True and os.path.isdir(destination) == True:
			
			sep = sep_of_tested_yes_isdir(destination)
			if ( not destination.endswith( sep ) ): # add it
				destination += sep + os.path.basename(source)
			else:                                   # already there
				destination += os.path.basename(source)
				
		bin = ''
		if (binary):
			bin = "b"
		
		with open ( source , "r"+bin ) as rfp:
			with open ( destination , "w"+bin ) as wfp:
				data = rfp.read( )
				wfp.write ( data )
				print 'cp: copied ' + source + ' to ' + destination
				
	elif os.path.isdir(source):
		
		if not os.path.isdir(destination):
			os.mkdir(destination)
		
		if os.access (destination, os.W_OK | os.X_OK):
			print 'good'
		else:
			sys.exit( 'cp: cannot copy directory ' + destination + ' : Directory is readonly or drive does not exist')
		
		if os.listdir(destination) == []: # or   if not os.listdir(destination):   due to [] evaluated to false
			rmdir(destination)
		else:
			sys.exit( 'cp: due to contents contained in the target directory, the safeguard is to not overwrite by copying into it')
		
		# therefore, note, destination folder required not to exist due to copytree function requirement
		shutil.copytree(source, destination)
		print 'cp: copied ' + source + ' to ' + destination

	else:
		print 'cp: cannot copy file or directory ' + source + ' : File does not exist or Directory does not exist'
	
def mv(source, destination):
	if os.path.isfile(source) or os.path.isdir(source):
	
		if os.path.isfile(source) == True and os.path.isdir(destination) == True:
			
			sep = sep_of_tested_yes_isdir(destination);
			if ( not destination.endswith( sep ) ):
				destination += sep + os.path.basename(source)
			else:
				destination += os.path.basename(source)
				
		# if both are directories, do either   s,d    endswith   directory separator    to check still
		os.rename(source, destination)
		print 'mv: renamed ' + source + ' to ' + destination
	else:
		print 'mv: cannot rename file ' + source + ' : File does not exist'
                                                                                           # NOTE !
# backup any custom files, for hosting, etc., situations may vary, edit as you see fit:
cp(drive +r':\phaser\bin\apache\apache'+apache_version+'\conf\httpd.conf','.')              # the r is outside quotes 
cp(drive +r':\phaser\bin\apache\apache'+apache_version+'\conf\extra\httpd-vhosts.conf','.') # to create a raw string literal
                                                                                           # it prevents escape sequences, can use the backslash regularly in a string
																						   # https://docs.python.org/2/reference/lexical_analysis.html#string-literals


# The following 3 statements for convenience are ok, but a bit problematic with the following condition: 
# when Apache is stopped in the same cmd.exe (console) window and then try to run this installation-update script,
# due to a strange window delete file, folder delay (when a binary has recently been in use), delete does not happen as expected,
# that is why as a sort of fix, exit is called in the apache_stop.bat to close the cmd.exe window , as a workaround, 
# so I then open a new console window to run this script.  It seems the console is retaining a hold on a previously running binary, hindering deletion.

# purpose,intent: To remove any previous version installed.
rmdir('./bin',	verify=True)
rmdir('./logs',	verify=True)
rmdir('./tmp',	verify=True)


# make empty directories
mkdirp('./tmp')
mkdirp('./logs')

print 'Creating Apache version ' + apache_version

with zipfile.ZipFile('httpd-'+apache_version+'-win32-VC11.zip', "r") as z:
    z.extractall('./httpd')

mkdirp('./bin/apache')
mv('./httpd/Apache24','./bin/apache/apache'+apache_version) 
rmdir('./httpd')


var = './bin/apache/apache'+apache_version
if( os.path.isdir(var) ):
	print 'Created directory: ' + var
else:
	print 'did not create directory, exiting: ' + var
	sys.exit( 1 )

	
print 'Creating PHP version ' + php_version


with zipfile.ZipFile('php-'+php_version+'-Win32-VC11-x86.zip', "r") as z:
    z.extractall('./php-'+php_version)

	
mkdirp('./bin/php')

mv('./php-'+php_version,'./bin/php/php-'+php_version)


var = './bin/php/php-'+php_version
if( os.path.isdir(var) ):
	print 'Created directory: ' + var
else:
	print 'did not create directory, exiting: ' + var
	sys.exit( 1 )

	
print 'Now to edit httpd.conf and php.ini'


conf = drive +r':\phaser\bin\apache\apache'+apache_version+'\conf\httpd.conf'


old = 'ServerRoot "c:/Apache24"'
new = 'ServerRoot "'+drive+':/phaser/bin/apache/apache'+apache_version+'"'
bake_replace(conf, old, new)

old = 'DocumentRoot "c:/Apache24/htdocs"'
new = 'DocumentRoot "'+drive+':/www"'
bake_replace(conf, old, new)

old = '<Directory "c:/Apache24/htdocs">'
new = '<Directory "'+drive+':/www">'
bake_replace(conf, old, new)

old = 'DirectoryIndex index.html'
new = 'DirectoryIndex index.php index.php3 index.html index.htm'
bake_replace(conf, old, new)


find = '#LoadModule xml2enc_module modules/mod_xml2enc.so'
append = 'LoadModule php5_module "'+drive+':/phaser/bin/php/php-'+php_version+'/php5apache2_4.dll"'
bake_append(conf, find, append)

find = 'LoadModule php5_module "'+drive+':/phaser/bin/php/php-'+php_version+'/php5apache2_4.dll"'
append = 'PHPIniDir "'+drive+':/phaser/bin/php/php-'+php_version+'"'
bake_append(conf, find, append)

find = '#ServerName www.example.com:80'
append = 'ServerName localhost:80'
bake_append(conf, find, append)

find = 'ServerName localhost:80'
append = 'HostnameLookups Off'
bake_append(conf, find, append)

find = 'AddType application/x-gzip .gz .tgz'
append = 'AddType application/x-httpd-php .php'
bake_append(conf, find, append)
    
find = 'AddType application/x-httpd-php .php'
append = 'AddType application/x-httpd-php .php3'
bake_append(conf, find, append)


source = drive +r':\phaser\bin\php\php-'+php_version+'\php.ini-development'
destination = drive +r':\phaser\bin\php\php-'+php_version+'\php.ini'


mv(source, destination)


if( empty_file(destination) == False ):
	print 'Created file: ' + destination
else:
	print 'did not create, mv file' + destination
	sys.exit( 1 )


ini = drive +r':\phaser\bin\php\php-'+php_version+'\php.ini'


old = ';date.timezone ='
new = 'date.timezone = "America/New_York"'
bake_replace(ini, old, new)

old = ';error_log = php_errors.log'
new = 'error_log = "'+drive+':/phaser/logs/php_error.log"'
bake_replace(ini, old, new)

old = '; extension_dir = "ext"'
new = 'extension_dir = "'+drive+':/phaser/bin/php/php-'+php_version+'/ext/"'
bake_replace(ini, old, new)

old = ';upload_tmp_dir ='
new = 'upload_tmp_dir = "'+drive+':/phaser/tmp"'
bake_replace(ini, old, new)

old = ';session.save_path = "/tmp"'
new = 'session.save_path = "'+drive+':/phaser/tmp"'
bake_replace(ini, old, new)


def make_apache_start(apache_version):

	content = r"""

@echo off
cd /D %~dp0
echo Apache {version} is starting ...

bin\apache\apache{version}\bin\httpd.exe

if errorlevel 255 goto finish
if errorlevel 1 goto error
goto finish

:error
echo.
echo Apache could not be started
pause

:finish

""".format ( version = apache_version )

	to_file( 'apache_start.bat', content ) #note: put back unescaped newlines, nice

	if( empty_file('apache_start.bat') == False ):
		print 'Created file: ' + 'apache_start.bat'
	else:
		print 'did not create file, exiting: ' + 'apache_start.bat'
		sys.exit( 1 )
		

def make_apache_stop(apache_version):

	content = r"""

rem To close the program just click the X of the console window and after a few moments it will close
rem Optionally: this bat file will close it a couple seconds faster using pv.exe
rem rm to del , cp to copy

@echo off
cd /D %~dp0
copy pv.exe bin\apache\apache{version}\bin\
bin\apache\apache{version}\bin\pv -f -k httpd.exe -q
rem due to a strange windows os filesystem delay to delete, not going to delete it then
rem del bin\apache\apache{version}\bin\pv.exe
if not exist apache\logs\httpd.pid GOTO exit
del apache\logs\httpd.pid
:exit
exit

""".format( version = apache_version )

	to_file( 'apache_stop.bat',   content ) #note: put back unescaped newlines, nice
	
	if( empty_file('apache_stop.bat') == False ):
		print 'Created file: ' + 'apache_stop.bat'
	else:
		print 'did not create file, exiting: ' + 'apache_stop.bat'
		sys.exit( 1 )
		
		
make_apache_start(apache_version)
make_apache_stop(apache_version)

# Done.
# Recommended to not use this next feature and for example instead, preferred is os-wide python script.
# For convenience, optional, OS-wide php scripting (that merely requires the following two files), to update:
os_wide_php_exe = drive +r':\bins\php\php.exe'
os_wide_php_dll = drive +r':\bins\php\php5ts.dll'
if ( exists(os_wide_php_dll) ):            # denotes you use it
	os.remove(os_wide_php_exe)
	os.remove(os_wide_php_dll)
	cp (drive +r':\phaser\bin\php\php-'+php_version+'\php.exe'   , os_wide_php_exe, binary=True) # to latest version
	cp (drive +r':\phaser\bin\php\php-'+php_version+'\php5ts.dll', os_wide_php_dll, binary=True) # to newest and finest

# For convenience, the next two functions are to show and hide the console window that Apache runs in:
# For use if you intend to install Autohotkey or already have done so.
# Usage: Presumes that the cmd.exe Apache is running within is the last taskbar program running, and will hide that, otherwise show:
def hide():
	content = """
	
WinHide, ahk_class ConsoleWindowClass
"""
	to_file( 'hide.ahk',   content )
	
def show():
	content = """

WinShow, ahk_class ConsoleWindowClass
"""
	to_file( 'show.ahk',   content )

hide()
show()