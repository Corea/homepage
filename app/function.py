import glob

def get_file_list():
	lst = glob.glob("./static/picture/*")
	return lst
