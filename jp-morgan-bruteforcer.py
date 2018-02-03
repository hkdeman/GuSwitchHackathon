import hashlib, uuid

key = input("Please enter a password")
salt = uuid.uuid4().hex
mix = key
hashed_password = hashlib.sha512(mix.encode()).hexdigest()



for i in range(10000):
	try_key = str(i).zfill(3)
	salt = uuid.uuid4().hex
	mix = try_key
	hashed_try = hashlib.sha512(mix.encode()).hexdigest()
	if(hashed_try==hashed_password):
		print("\n Password found: "+str(i))
		break
	else:
		print("Trying "+str(i)+" ...")

 

