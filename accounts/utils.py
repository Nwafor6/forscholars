from uuid import uuid4

def generate_random_id(length=5):
	random_id = str(uuid4())
	print(random_id)
	return random_id[:length]