import torch.nn as nn
import torch.autograd as autograd
import torch.optim as optim

class LSTM(nn.Module):
	def __init__(self,input_size,hidden_size,output_size,):
		super(LSTM, self).__init__()
		self.hidden_dim = hidden_size
		self.input_size = input_size
		self.lstm = nn.LSTM(input_size, hidden_dim)
		self.hidden2label = nn.Linear(hidden_dim,output_size)
		self.hidden = self.init_hidden()

	def init_hidden(self):
		return(autograd.Variable(torch.zeros(1, 1, self.hidden_dim)),autograd.Variable(torch.zeros(1, 1, self.hidden_dim)))
	
	def forwardPropagation(self, input):
		output, hidden = self.lstm(input,self.hidden)
		output = self.hidden2label(output.view(x.size()[0],-1))
		return output

class TBPTT():
	def __init__():

	def train():

		
model = LSTM(10,128,1)