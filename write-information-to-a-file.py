# open file for reading
file = open('devices-01.txt', 'r')

#read info one line at a time and strip off whitespace
name = file.readline().strip()
ip_address = file.readline().strip()
os_type = file.readline().strip()
username = file.readline().strip()
password = file.readline().strip()

#display info using string formatting
print(3*'-','Device info nicely formatted',10*'-')
print('')
print('Name   IP  address    OS    Username    Password')
print(4*'-', 10*'-',4*'-',6*'-',6*'-')
print('{0:8} {1:15} {2:8} {3:10} {4:10}'.format(name, ip_address,os_type,username,password))


print('')
print(23*'-')

# create comma seperated string of device info
device_info = name # start with devie name
device_info = device_info + ',' + ip_address #adds comma and IP address
device_info = device_info + ',' + os_type 
device_info = device_info + ',' + username
device_info = device_info + ',' + password

#write device info string to file
print('')
print('-'*3, 'Writing device information to file ','-'*15)
print('')
outfile = open('devices-01-out.csv', 'w') #opens output file
outfile.write(device_info) #write the line of device info
outfile.write('\n') # ending new line with 'write'
outfile.close() #close file when writing is complete
print('--- Device information written to file ','-'*15)
print('')

#open file that was created 
infile = open('devices-01-out.csv', 'r') #open new one line file
device_info = infile.readline().strip() #read ine from file
infile.close() #close the file

#display info from file that was just created 
print('')
print('-'*3, 'Device info read from file we wrote', '-'*15)
print('')
print('Device Info: ', device_info)
print('')
print('-'*25)
print('')