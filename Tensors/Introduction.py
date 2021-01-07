import torch

# creating tensors
print(torch.FloatTensor([1, 2, 3]))
print(torch.IntTensor([1, 2, 3]))


# 1D tensors indexing

tensor = torch.FloatTensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(tensor[0])  # first element
print(tensor[0:3])  # first three elements (excluding)
print(tensor[:])  # All elements
print(tensor[2:4])  # starting index 2 and not including 4
