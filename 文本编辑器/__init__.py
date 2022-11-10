import masterUI
import tkinter


def main():
	master = tkinter.Tk()
	
	master.title("剧情文本编辑器")
	
	masterUI.UIController(master, 960, 540)
	
	master.mainloop()


if __name__ == '__main__':
	main()
