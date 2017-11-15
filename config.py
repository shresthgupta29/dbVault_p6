import os
cwd = os.getcwd()  #/current working directory
java_home='/scratch/jdk1.8.0_144'
oracle_home = '/u01/app/pgbuora/product/12.2.0/dbhome_1'
oracle_base = '/u01/app/pgbuora' 
host = 'kkm00adp.in.oracle.com' #host name of current machine 
client_path = '/scratch/db_vault/database' # path of 'database' folder containing 'runInstaller.sh'
p6db= '/scratch/db_vault/p6db/database' # path of 'database' folder for p6 containf 'dbsetup.sh'
admin_pass='Manager1' # password for sys/system/admin accounts
cdb = 'orcl' #container db name
pgdb = 'pdb' # pluggable db name

