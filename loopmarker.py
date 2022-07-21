######## ---- loopmarker.py ----
######## !! works with python 2.7 !! (don't use python3)
######## THIS IS A SUPER BASIC CODE TO ADD SAMPLER MARKERS
######## TO ADD LOOP TO WAVE FILES THAT YOU WOULD LIKE TO USE
######## WITH SAMPLERS LIKE SAMPLERBOX
#### feel free to fork and improve
#### Florent Jean Gaston


import struct
import binascii


print "welcome here buddy"
print "##################"
print "so you want to add sampler markers to a wave file ?"
print ""
print ""


my_file = raw_input("What's the name of your file ?")
print my_file

with open(my_file, 'rb+') as f:
    #for i in range (4, 7) :
    f.seek(4)
    data = f.read(4)
    data = struct.unpack("<L",data)
    data = int(data[0])
    print "Your file : "+my_file
    print "File size : "+str(data)+" bytes"
    
    print " "
    start_loop = input("First sample of the loop ? ")
    
    end_loop = input("Last sample of the loop ? ")
    
    sure = raw_input("Are you really sure that you want to proceed (y/n) ? ") 
    if sure == "n":
        print "abord mission ..."
        quit()
    else:
        print "proceeding ..."
        
    
    data = data+68 #ajoute 68 bytes au fichier
    
    #print data
    
    data = struct.pack("<L",data)
    #print data
    f.seek(4)
    f.write(data)
    f.close
    
  
    
with open(my_file, 'a+') as f:
    
    smplmarker = '736D706C3C0000000000000000000000000000003C00000000000000000000000000000001000000000000000000000000000000'
    smplmarker = binascii.unhexlify(smplmarker)
    #print smplmarker
    f.write(smplmarker)
    start_loop = struct.pack("<L",start_loop)
    f.write(start_loop)
    end_loop = struct.pack("<L",end_loop)
    f.write(end_loop)
    endmarker = '0000000000000300'
    endmarker = binascii.unhexlify(endmarker)
    f.write(endmarker)
    f.close
print 'Done !!!'    



    