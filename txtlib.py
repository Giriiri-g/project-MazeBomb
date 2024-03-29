#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame

BOLD = 'bold'
ITALIC = 'italic'
UNDERLINE = 'underline'
SIZE = 'size'
FONT = 'font'
COLOR = 'color'

BEGIN = 'begin'
END = 'end'

class Point:

	def __init__(self, classe, pos, type, attr=None):
		self.pos = pos
		self.classe = classe
		self.type = type
		self.attr = attr


class Text:

	def __init__(self, size, font, font_size=16, text=''):
		self.rect = pygame.Rect((0, 0), size)
		self.area = pygame.Surface(size, pygame.SRCALPHA | pygame.HWSURFACE)
		self.background_color = (255, 255, 255)
		
		self.text = text
		self.points = []
		
		self.text_start = 0
		self.line_numbers = False # XXX doesn't work yet
		self.antialias = True
		self.border = 5
		
		self.default_size = font_size
		self.default_font = font
		self.default_color = (0, 0, 0)
		self.fonts = {}
		self.load_font(font, font_size)

	def set_background_color(self, color):
                self.background_color = color
	
	def clear(self):
		self.text = ''
	
	# this transform markup text in html style in txtlib style
	def html(self, code):
		code = str(code)
		processing = False
		if code.find('<'):
			text = ''
			txt_id = 0
			for id in range(len(code)):
				if code[id] not in ('<', '>') and not processing:
					text += code[id]
					txt_id += 1
				elif code[id] == '>':
					processing = False
				elif code[id] == '<':
					processing = True
					if code[id+1] != '/':
						if code[id+1].lower() == 'b':
							self.points.append(Point(BEGIN, len(self.text)+txt_id, BOLD))
						elif code[id+1].lower() == 'i':
							self.points.append(Point(BEGIN, len(self.text)+txt_id, ITALIC))
						elif code[id+1].lower() == 'u':
							self.points.append(Point(BEGIN, len(self.text)+txt_id, UNDERLINE))
						else:
							end = code[id:].lower().find('>') + id
							if code[id:end].find('color') != -1:
								rgb = code[id+8:end-1].replace(' ', '')
								r, g, b = rgb.split(',')
								self.points.append(Point(BEGIN, len(self.text)+txt_id, COLOR, (int(r), int(g), int(b))))
							elif code[id:end].lower().find('size') != -1:
								size = int(code[id+7:end-1])
								self.points.append(Point(BEGIN, len(self.text)+txt_id, SIZE, size))
							elif code[id:end].lower().find('font') != -1:
								font = code[id+7:end-1]
								self.points.append(Point(BEGIN, len(self.text)+txt_id, FONT, font))
					else:
						if code[id+2].lower() == 'b':
							self.points.append(Point(END, len(self.text)+txt_id, BOLD))
						elif code[id+2].lower() == 'i':
							self.points.append(Point(END, len(self.text)+txt_id, ITALIC))
						elif code[id+2].lower() == 'u':
							self.points.append(Point(END, len(self.text)+txt_id, UNDERLINE))
						elif code[id+2].lower() == 'c':
							self.points.append(Point(END, len(self.text)+txt_id, COLOR, None))
						elif code[id+2].lower() == 's':
							self.points.append(Point(END, len(self.text)+txt_id, SIZE, None))
						elif code[id+2].lower() == 'f':
							self.points.append(Point(END, len(self.text)+txt_id, FONT, None))
			
			self.text += text
		else:
			self.text += code
	
	# add a style
	def add_style(self, start, end, type, attr=None):
		self.points.append(Point(BEGIN, start, type, attr))
		self.points.append(Point(END, end, type, attr))
		
		self.points.sort(key=lambda x: x.pos)
	
	def load_font(self, font, size):
		if font in pygame.font.get_fonts():
			f = pygame.font.SysFont(font, size)
			if font in self.fonts:
				self.fonts[font][size] = f
			else:
				self.fonts[font] = {size:f}
		else:
			try:
				f = pygame.font.Font(font, size)
			except:
				f = pygame.font.Font(None, size)
			
			if font in self.fonts:
				self.fonts[font][size] = f
			else:
				self.fonts[font] = {size:f}
	
	def check_fonts(self):
		font = [self.default_font]
		size = [self.default_size]
		for point in self.points:
			if point.classe == BEGIN:
				if point.type == FONT:
					font.append(point.attr)
				elif point.type == SIZE:
					size.append(point.attr)
			else:
				if point.type == FONT:
					font.pop()
				elif point.type == SIZE:
					size.pop()
			
			if font[len(font)-1] not in self.fonts:
				self.load_font(font[len(font)-1], size[len(size)-1])
			
			if size[len(size)-1] not in self.fonts[font[len(font)-1]]:
				self.load_font(font[len(font)-1], size[len(size)-1])
	
	# check the line height
	def line_height(self, font, char, line):
		line_height = font
		size = [self.default_size]
		font = [self.default_font]
		for point in self.points:
			if point.classe == BEGIN:
				if point.type == FONT:
					font.append(point.attr)
				elif point.type == SIZE:
					size.append(point.attr)
			else:
				if point.type == FONT:
					font.pop()
				elif point.type == SIZE:
					size.pop()
			
			if char <= point.pos <= char+len(line) and point.type in (FONT, SIZE):
				f = self.fonts[font[len(font)-1]][size[len(size)-1]].get_height()
				if f > line_height:
					line_height = f
		
		return line_height
	
	# replace some characters like tabs
	def replace(self, text):
		text = text.replace('\t', '    ')
		
		return text
	
	# redraw the text
	def update(self):
		# control if the needed fonts are loaded
		self.check_fonts()
		
		self.area.fill(self.background_color)
		
		l = 0 # line number
		dist_from_top = 0
		char = 0 # char num from the beginning
		bottom_border = -self.text_start + self.rect.height
		
		bold = False
		italic = False
		underline = False
		color = [self.default_color]
		size = [self.default_size]
		font = [self.default_font]
		for line in self.text.split('\n'):
			# check for line_height
			h = self.fonts[font[len(font)-1]][size[len(size)-1]].get_height()
			line_height = self.line_height(h, char, line)
			
			id = 0
			l_id = 0
			x = self.border # need changes to support line numers
			printed = False
			for point in self.points:
				if char <= point.pos <= char+len(line):
					# don't draw text if it's over the top border
					if -self.text_start <= dist_from_top <= bottom_border and l_id == 0:
						f = self.fonts[font[len(font)-1]][size[len(size)-1]]
						f.set_bold(bold)
						f.set_italic(italic)
						f.set_underline(underline)
						
						text = self.replace(line[:point.pos-char])
						
						render = f.render(text, self.antialias, color[len(color)-1])
						line_pos = (line_height-f.get_height())/2
						self.area.blit(render, (x, dist_from_top+self.text_start+line_pos+self.border))
						
						x += render.get_width()
						printed = True
					
					if point.classe == BEGIN:
						if point.type == BOLD:
							bold = True
						elif point.type == ITALIC:
							italic = True
						elif point.type == UNDERLINE:
							underline = True
						elif point.type == COLOR:
							color.append(point.attr)
						elif point.type == SIZE:
							size.append(point.attr)
						elif point.type == FONT:
							font.append(point.attr)
					elif point.classe == END:
						if point.type == BOLD:
							bold = False
						elif point.type == ITALIC:
							italic = False
						elif point.type == UNDERLINE:
							underline = False
						elif point.type == COLOR:
							color.pop()
						elif point.type == SIZE:
							size.pop()
						elif point.type == FONT:
							font.pop()
					
					# don't draw text if it's over the top border
					if -self.text_start <= dist_from_top <= bottom_border:
						f = self.fonts[font[len(font)-1]][size[len(size)-1]]
						f.set_bold(bold)
						f.set_italic(italic)
						f.set_underline(underline)
						
						try:
							text = self.replace(line[point.pos-char:self.points[id+1].pos-char])
						except:
							text = self.replace(line[point.pos-char:])
						
						render = f.render(text, self.antialias, color[len(color)-1])
						line_pos = (line_height-f.get_height())/2
						self.area.blit(render, (x, dist_from_top+self.text_start+line_pos+self.border))
						
						x += render.get_width()
						printed = True
					
					l_id += 1
				
				id += 1
			
			if not printed and -self.text_start <= dist_from_top <= bottom_border:
					f = self.fonts[font[len(font)-1]][size[len(size)-1]]
					f.set_bold(bold)
					f.set_italic(italic)
					f.set_underline(underline)
					
					text = self.replace(line)
					
					render = f.render(text, self.antialias, color[len(color)-1])
					line_pos = (line_height-f.get_height())/2
					self.area.blit(render, (x, dist_from_top+self.text_start+line_pos+self.border))
					
					x += render.get_width()
					printed = True
					

			l += 1
			char += len(line) + 1
			dist_from_top += line_height
