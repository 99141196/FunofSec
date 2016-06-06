from Crypto.Hash import SHA256
from Crypto.Random import random
from Crypto.Hash import MD5, SHA256, SHA512


from lib.helpers import read_hex


raw_prime = """FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1
29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD
EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245
E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED
EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D
C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F
83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D
670C354E 4ABC9804 F1746C08 CA237327 FFFFFFFF FFFFFFFF"""
prime = read_hex(raw_prime)


def create_dh_key():

    #Generator = random.randint(0, int(2**8)) #It might be an issue that the generator is not consistent
    Generator = 4
    my_private_key = random.randint(0, int(2**8))
    my_public_key = (Generator ** my_private_key)%prime
    return (my_public_key, my_private_key)
    #This section is designed to return my public key and my private key
    #My private key is my private number
    #My public key is the generator ^ my private number, mod prime


def calculate_dh_secret(their_public, my_private):
    shared_secret = (their_public ** my_private)%prime

    #print("shared secret:", shared_secret)
    msg = bytes(str(shared_secret),"ascii")
    shared_hash = SHA256.new(msg).hexdigest()
    

    # Hash the value so that:
    # (a) There's no bias in the bits of the output
    #     (there may be bias if the shared secret is used raw)
    # (b) We can convert to raw bytes easily
    # (c) We could add additional information if we wanted
    # Feel free to change SHA256 to a different value if more appropriate


    #shared_hash = SHA256.new(bytes(shared_secret, "ascii")).hexdigest()
    return shared_hash
        #Secret is what each person will share over their network



#Below is the testing code

#(my_public_key, my_private_key) = create_dh_key()
#(their_public_key, their_private_key) = create_dh_key()
#shared_hash = calculate_dh_secret(my_public_key, their_private_key)
#print("my public:", my_public_key, "their private key:", their_private_key, "my private key:", my_private_key, "their public key:", their_public_key)
#print("my session key:", (their_public_key ** my_private_key)%prime)
#print("their session key:", (my_public_key ** their_private_key)%prime)

