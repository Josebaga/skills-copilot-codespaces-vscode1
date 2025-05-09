#decodificar infinitamente base64
import base64
flag_file = "http://conclave.thehackerconclave.es:42101"
fh = open(flag_file,"r")
data = fh.read()
fh.close()
print(f"###Flag file: {flag_file}")
i= 0
while True:
    print(f"**ROUND {i}: Decoding Base64 data : {len(data)} bytes")   
    bytes_data = data.encode()
    try:
        bytes_b64 = base64.b64decode(bytes_data)
        data = bytes_b64.decode()
        i += 1
    except:
        print(f"*** FLAG: {bytes_data.decode()}")
        break    
    
    
    
    
