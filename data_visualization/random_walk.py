from random import choice

class RandomWalk:
	def __init__(self, num_points = 5000):
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]
		

	def fill_walk(self):
	
		while len(self.x_values) < self.num_points:
			x_val, y_val = self.get_step()
			if x_val == 0 and y_val == 0 :
				continue

			x = self.x_values[-1] + x_val
			y = self.y_values[-1] + y_val

			self.x_values.append(x)
			self.y_values.append(y)

	def get_step(self):
		x_pos = choice([-1,1])
		x_dis = choice([1,2,3,4,5,6,7,8,9])
		x_val = x_pos * x_dis

		y_pos = choice([-1, 1])
		y_dis = choice([1,2,3,4,5])
		y_val = y_pos * y_dis

		return x_val, y_val

		
