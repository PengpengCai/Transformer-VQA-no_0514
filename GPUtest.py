import torch
print(torch.cuda.is_available())  # Should print True if CUDA is available
print(torch.cuda.device_count())  # Should print the number of available GPUs