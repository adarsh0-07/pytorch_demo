import torch

# creating tensors
print(torch.FloatTensor([1, 2, 3]))
print(torch.IntTensor([1, 2, 3]))
a = torch.FloatTensor([1, 2, 3])

# 1D tensors indexing
print("------tensor indexing------")
tensor = torch.FloatTensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(tensor[0])  # first element
print(tensor[0:3])  # first three elements (excluding)
print(tensor[:])  # All elements
print(tensor[2:4])  # starting index 2 and not including 4

# tensor operations
print("-----tensor operations-------")
x = torch.rand(2, 2)
y = torch.rand(1, 1)
z = x + y
print(z)
print(x.shape)
print(y.shape)
print(a.shape)

# GPU Tensor operations
print(torch.cuda.is_available())

# creating GPU Tensors

X = torch.rand(2, 2, device=torch.device("cuda"))  # X = X.to(torch.device("cuda"))
Y = torch.rand(3, 3, device=torch.device("cuda"))
print(X)
print(Y)

# Moving a GPU Tensor to CPU

X = X.to("cpu")
