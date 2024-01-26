def hello_world():
	dummy = 'Hello World!'
	return dummy 
def hello_world_n(N):
	return " ".join(["Hello World!" for _ in range(N)])

result_hello_world = hello_world()
result_hello_world_n = hello_world_n(3)

print(result_hello_world)
print(result_hello_world_n)

