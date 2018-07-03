import argparse
from PIL import Image


class Maze():
	# 0 ---> X
	# |
	# v
	#
	# Y
	# 
	# 0 - black, 255 - white

	def __init__(self, image):
		self.image = image.convert(mode='L')
		self.pixels = self.image.load()
		self.width = self.image.size[0]
		self.height = self.image.size[1]

		self.start = self.end = 0
		self.parse()


	def parse(self):

		x = y = 0
		# Find start
		y = [i for i in xrange(self.height) if self.pixels[x,i] > 0]
		self.start = (x, y[0])
		# self.pixels[x, y[0]] = 8
		# Find end
		x = self.width-1
		y = [i for i in xrange(self.height) if self.pixels[x,i] > 0]
		self.end = (x, y[0])
		# self.pixels[x, y[0]] = 8

		print "Start: {}".format(self.start)
		print "End: {}".format(self.end)


	def solve(self):
		self.route, found = self.propagate(self.start, self.end, [])
		# print self.route


	def propagate(self, pos, target, route):
		# print 'Scanning {}...'.format(pos)
		route.append(pos)
		if pos == target:
			# print 'END!!!'
			return route, True
		x, y = pos
		for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
			new_x = x + dx
			new_y = y + dy
			# print '\tlooking for {}:'.format((new_x,new_y))
			if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
				# print '\tOut of bound'
				continue
			if self.pixels[(new_x,new_y)] == 0:
				# print '\tWall'
				continue
			if (new_x,new_y) in route:
				# print '\t Already search'
				continue
			new_route, found = self.propagate((new_x,new_y), target, route)
			if found == True:
				return new_route, True
		route.remove((x,y))
		return route, False



	def save_maze_solution(self, output_file_name="solve_maze.bmp"):
		out_image = self.image.convert(mode='RGB')
		out_pixel = out_image.load()
		for p in self.route:
			out_pixel[p] = (0, 128, 0)
		out_image.save(output_file_name)
		out_image.show()




def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--image-input', '-i', default="examples/tiny_maze.bmp", help='Input image of the maze')
	parser.add_argument('--image-output', '-o', default="solve_maze.bmp", help='Output image of the maze solved')
	args = parser.parse_args()


	maze = Maze(Image.open(args.image_input))
	# print maze.pixels[(0,7)]
	# maze.maze_image.show()
	maze.solve()
	maze.save_maze_solution(args.image_output)



if __name__ == "__main__":
	main()