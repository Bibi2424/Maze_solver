

from PIL import Image
from graph import *

class Maze():
	def __init__(self, image):
		self.maze_image = image
		self.maze_pix = self.maze_image.load()
		self.maze_width = self.maze_image.size[0]
		self.maze_height = self.maze_image.size[1]
		self.maze_graph = Graph()

		self.parse_maze_image()

		self.save_maze_solution()

	def parse_maze_image(self):
		# Find start and end
		x = 0
		y = [i for i in xrange(self.maze_height) if self.maze_pix[x,i] > 0]
		self.maze_start = (x, y[0])
		self.maze_pix[x, y[0]] = 8

		x = self.maze_width-1
		y = [i for i in xrange(self.maze_height) if self.maze_pix[x,i] > 0]
		self.maze_start = (x, y[0])
		self.maze_pix[x, y[0]] = 8

		#TODO: WIP


	def save_maze_solution(self):
		self.maze_image.save("solv_maze.bmp")


def main():
	#TODO: Change to png image
	maze_image = Image.open("examples/dummy_maze.bmp")
	# maze_image = Image.open("examples/tiny_maze.bmp")
	maze = Maze(maze_image)

	# im = Image.open("simple_maze.bmp")
	# print im.format, im.size, im.mode
	# pix = im.load()
	# print pix[0, 5]
	# for i in im.getdata():
	# 	print i


	# graph = Graph()
	# graph.add_link('start', 'step1', 1)	
	# graph.add_link('step1', 'step2', 4)
	# print graph


if __name__ == "__main__":
	main()
