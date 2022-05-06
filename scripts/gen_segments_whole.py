width=15
height=1
step=0.75
var_gap = 1
eps=0.2
clause_width = 2
clause_height = 2
clause_gap = 1

xbeg_label = '\\x0'
ybeg_label = '\\y0'

dic={xbeg_label : 0, ybeg_label : 0}
idx={'x' : 0, 'y' : 0}

def magic_str(x):
	s = str(x) + 'label'
	return s.replace('1', 'a')\
	.replace('2', 'b')\
	.replace('3', 'c')\
	.replace('4', 'd')\
	.replace('5', 'e')\
	.replace('6', 'f')\
	.replace('7', 'g')\
	.replace('8', 'h')\
	.replace('9', 'i')\
	.replace('0', 'j')

def next_id(dim, value):
	global idx
	global dic
	idx[dim] = idx[dim] + 1
	label = '\\' + dim + magic_str(idx[dim])
	dic[label] = value
	return label
	
def add_eps(x, sign):
	global dic
	x_cropped=x[1:]
	label = '\\meps' + x_cropped if sign == '-' else '\\eps' + x_cropped
	if sign == '-':
		dic[label] = dic[x] - eps
	else:
		dic[label] = dic[x] + eps
	return label
	
def movey(label, much):
	return next_id('y', dic[label] + much)
	
def movex(label, much):
	return next_id('x', dic[label] + much)
	
def get_rect_y1(i):
	if i == 1:
		return ybeg_label
	else:
		return movey(get_rect_y2(i-1), var_gap)

def get_rect_y2(i):
	return movey(get_rect_y1(i), 2*step)

def variable_segment(i):
	xeps = add_eps(xbeg_label, '-')
	y1 = get_rect_y1(i)
	y2 = get_rect_y2(i)
	width_label = next_id('x', width)
	width_label_smol = next_id('x', width/4)
	width_half = next_id('x', width/2)
	yhalf = movey(y1, step)
	label = '{VARIABLE-gadget$_' + str(i) + '$}'
	x_true = '{$x_' + str(i) + ' = \\true$}'
	x_false = '{$x_' + str(i) + ' = \\false$}'
	out = f'''Draw ({width_half},{y1}) -- ({width_label},{y1}) node[pos=0.2, above] {x_true};
Draw ({width_half},{y2}) -- ({width_label},{y2}) node[pos=0.2, above] {x_false};
Filldraw [fill=lime!30, draw=black] ({xeps},{add_eps(y1, '-')}) rectangle ({add_eps(width_half, '+')}, {add_eps(y2, '+')});
Draw ({xbeg_label},{y1}) -- ({width_label},{y1});
Draw ({xbeg_label},{y1}) -- ({xbeg_label},{yhalf});
Draw ({width_label_smol},{y1}) -- ({width_label_smol},{y2});
Draw ({width_label_smol},{y2}) -- ({width_label},{y2});
Draw ({xbeg_label},{yhalf}) -- ({width_label_smol},{yhalf});
\\node[above right] at ({xeps},{add_eps(y2, '+')}) {label};'''.replace("Draw", "\\draw").replace("Filldraw", "\\filldraw")
	return out


def get_clause_x1(i):
	if i == 1:
		quarter_width = next_id('x', 3*width/4)
		return quarter_width
	else:
		return movex(get_clause_x2(i-1), clause_gap)
		
def get_clause_x2(i):
	return movex(get_clause_x1(i),clause_width)

stepx = clause_width / 10
stepy = clause_height / 6

or_width = 3*stepx

def or_gadget(x0, y0):
	h = 2 * stepy
	ytop = movey(y0, h)
	y1 = movey(y0, h/4)
	y2 = movey(y0, 2*h/4)
	y3 = movey(y0, 3*h/4)
	x1 = movex(x0, stepx)
	x2 = movex(x1, stepx)
	x3 = movex(x2, stepx)	
	out = f'''
Draw ({x0},{y0}) -- ({x0},{ytop});
Draw ({x0},{y1}) -- ({x2},{y1});
Draw ({x0},{y3}) -- ({x2},{y3});
Draw ({x1},{y1}) -- ({x1},{y3});
Draw ({x2},{y1}) -- ({x2},{y3});
Draw ({x2},{y2}) -- ({x3},{y2});'''.replace("Draw", "\\draw").replace("Filldraw", "\\filldraw")
	return out

def clause_gadget(i, x_id, x_val, y_id, y_val, z_id, z_val):
	label = '{CLAUSE-gadget$_' + str(i) + '$}'
	x1 = get_clause_x1(i)
	x2 = get_clause_x2(i)
	y_top = movey(get_rect_y2(3), clause_height)
	y_start = get_rect_y2(3)
	x11_x = movex(x1, stepx)
	x11_y = movey(y_start, 2*stepy)
	y11_x = movex(x1, 2*stepx)
	y11_y = movey(y_start, 4*stepy)
	z11_x = movex(x1, 3*stepx)
	z11_y = movey(y_start, 5*stepy)
	or1_x = movex(x1, 4*stepx)
	or2_x = movex(or1_x, or_width)
	def function(b):
		if b:
			return get_rect_y1
		else:
			return get_rect_y2
	out = f'''
Filldraw [fill=cyan!30, draw=black] ({add_eps(x1,'-')},{add_eps(ybeg_label,'-')}) rectangle ({add_eps(x2,'+')}, {add_eps(y_top, '+')});
Draw ({x11_x},{function(x_val)(x_id)}) -- ({x11_x},{x11_y});
Draw ({x11_x},{x11_y}) -- ({or1_x},{x11_y});
Draw ({y11_x},{function(y_val)(y_id)}) -- ({y11_x},{y11_y});
Draw ({y11_x},{y11_y}) -- ({or1_x},{y11_y});
Draw ({z11_x},{function(z_val)(z_id)}) -- ({z11_x},{z11_y});
Draw ({z11_x},{z11_y}) -- ({or2_x},{z11_y});
\\node[above right] at ({add_eps(x1,'-')},{add_eps(y_top,'+')}) {label};'''.replace("Draw", "\\draw").replace("Filldraw", "\\filldraw")
	return out + or_gadget(or1_x, x11_y) + or_gadget(or2_x, movey(z11_y, - 2 * stepy))


def gen_tikzmath():
	out = ''
	for x,y in dic.items():
		out += x + '=' + str(y) + ';\n'
	return out 

variable_segment1 = variable_segment(1)
variable_segment2 = variable_segment(2)
variable_segment3 = variable_segment(3)

clause_gadget1 = clause_gadget(1, 2, True, 3, True, 1, False)
clause_gadget2 = clause_gadget(2, 3, False, 1, True, 2, True)

output = '''{
\\begin{figure}
\\centering
\\begin{tikzpicture}
\\tikzmath{
''' + gen_tikzmath() + '''}
''' + clause_gadget1 + '''
''' + clause_gadget2 + '''
''' + variable_segment1 + '''
''' + variable_segment2 + '''
''' + variable_segment3 + '''
\\end{tikzpicture}
\\caption{\\textbf{Scheme of the whole construction.}}
General layout of VARIABLE-gadgets and CLAUSE-gadgets and how they
interact with each other.
\\label{fig:segment_apx_whole}
\\end{figure}
'''
print(output)

