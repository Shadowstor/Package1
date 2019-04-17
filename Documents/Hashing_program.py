from sys import argv 
import hashlib
try:
    option = argv[1]
    fil = argv[2]
    with open(fil , 'rb') as hashfil:
        tbhashed = hashfil.read()
        if option == '-a':

            md5hed = hashlib.md5()
            md5hed.update(tbhashed)
            print( "Md5sum: " +  md5hed.hexdigest())
        
            sha1hed = hashlib.sha1()
            sha1hed.update(tbhashed)
            print("Sha1sum: " + sha1hed.hexdigest())
        
            sha256hed = hashlib.sha256()
            sha256hed.update(tbhashed)
            print("Sha256sum: " + sha256hed.hexdigest())
    
        elif option == '-m':
            md5hed = hashlib.md5()
            md5hed.update(tbhashed)
            print( "Md5sum: " +  md5hed.hexdigest())
    
        elif option == '-s':
            sha1hed = hashlib.sha1()
            sha1hed.update(tbhashed)
            print("Sha1sum: " + sha1hed.hexdigest())
    
        elif option == '-S':
            sha256hed = hashlib.sha256()
            sha256hed.update(tbhashed)
            print("Sha256sum: " + sha256hed.hexdigest())

        elif option == '-h':
            print('format is: python3 Hashing_program.py option filename\n' +
            '-a for all \n -m for md5sum \n -s for sha1sum \n -S for sha256sum')

        else:
            print("Invalid switch use -h for help on how to use this command")
except: 
    print('invalid format \n format is: python3 Hashing_program.py option filename\n' +
        '-a for all \n -m for md5sum \n -s for sha1sum \n -S for sha256sum')

