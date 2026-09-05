import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import askstring

class View:

    BORDER = {'padx':2, 'pady':2}
    BORDER_L = {'padx':2, 'pady':2, 'sticky':tk.E}
    BORDER_B = {'padx':2, 'pady':2, 'sticky':tk.E}
    BORDER_E = {'padx':2, 'pady':2, 'sticky':tk.EW}
    BORDER_F = {'padx':2, 'pady':2, 'sticky':tk.NSEW}

    def __init__(self, root_ = None, lang_ = None):
        self.root = root_
        self.lang = lang_
        self.ctrl = None
        self.widget_list = []
        self.root.title(self.lang.txt('txt_title'))
        self.root.geometry("660x400")
        self.root.minsize(660, 400)
        #self.root.resizable(False, False)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def build_01(self):
        self.frame_01 = self.Frame_01(root_=self.root,
                                        widget_list_=self.widget_list,
                                        ctrl_=self.ctrl,
                                        lang_=self.lang,
                                        rc_ = self.rc,
                                        border_=self.BORDER)
        self.frame_01.refresh()
        self.frame_01.show()

    def build_02(self):
        self.frame_02 = self.Frame_02(root_=self.root,
                                        widget_list_=self.widget_list,
                                        ctrl_=self.ctrl,
                                        lang_=self.lang,
                                        rc_ = self.rc,
                                        border_=self.BORDER)
        self.frame_02.refresh()
        self.frame_02.show()

    def build_03(self):
        self.frame_03 = self.Frame_03(root_=self.root,
                                        widget_list_=self.widget_list,
                                        ctrl_=self.ctrl,
                                        lang_=self.lang,
                                        rc_ = self.rc,
                                        border_=self.BORDER)
        self.frame_03.refresh()
        self.frame_03.show()
        self.frame_03.test_stage_00()

    def build_04(self):
        self.frame_04 = self.Frame_04(root_=self.root,
                                        widget_list_=self.widget_list,
                                        ctrl_=self.ctrl,
                                        lang_=self.lang,
                                        )
        self.frame_04.refresh()
    
    class Frame_01:
        def __init__(S, root_=None, widget_list_=None, ctrl_=None, lang_=None, rc_=None, border_=None):
            S.root = root_
            S.lang = lang_
            S.ctrl = ctrl_
            S.widget_list = widget_list_
            S.widget_list.append(S)
            S.rc = rc_
            S.BORDER = border_

            S.style = ttk.Style()
            #S.style.configure('orange.TLabel', foreground='#f09000', font=(tk.NONE, '44', 'bold'))
            S.style.configure('orange.TLabel', foreground='#dd8f1c', font=(tk.NONE, '44', 'bold'))
            S.style.configure('green.TLabel', foreground='#00aa72', font=(tk.NONE, '22', 'bold'))
            S.style.configure('black.TLabel', foreground='#00aa72', font=(tk.NONE, '22', 'bold'))
            

            S.frame_main = ttk.Frame(S.root)
            for c, w in enumerate([5, 1, 1, 1, 5]): S.frame_main.columnconfigure(index=c, weight=w)
            for r, w in enumerate([1, 4, 3, 1, 1]): S.frame_main.rowconfigure(index=r, weight=w)
            S.label_03 = ttk.Label(S.frame_main, text='TKinter 2023', font=(tk.NONE, 10))
            S.frame_01 = ttk.Frame(S.frame_main)
            S.combobox_01 = ttk.Combobox(S.frame_01, state='readonly', values=S.lang.languages_list)
            S.combobox_01.set(S.lang.language_native)                                
            S.combobox_01.bind("<<ComboboxSelected>>", lambda x: S.ctrl.cmd(('01_combobox_01', S.combobox_01.get())))
            S.label_01 = ttk.Label(S.frame_01)
            S.label_02 = ttk.Label(S.frame_main, style="orange.TLabel")
            S.label_04 = ttk.Label(S.frame_main, font=(tk.NONE, 12), justify='center')
            S.button_01 = ttk.Button(S.frame_main, command=lambda: S.ctrl.cmd(('01_button_01', )))
            S.button_02 = ttk.Button(S.frame_main, state='disabled')
            S.button_03 = ttk.Button(S.frame_main, command=lambda: S.ctrl.cmd(('01_button_03', )))#, command=lambda: S.ctrl.cmd(('modal ask', askstring('title', 'prompt'))))

        def refresh(S):
            S.combobox_01['values'] = S.lang.languages_list
            S.label_01['text'] = S.lang.txt('local_name')
            S.label_02['text'] = S.lang.txt('txt_title_main')
            S.label_04['text'] = S.lang.txt('txt_hello')
            S.button_01['text'] = S.lang.txt('txt_btn_help')
            S.button_02['text'] = S.lang.txt('txt_btn_results')
            S.button_03['text'] = S.lang.txt('txt_btn_go_testing')

        def show(S):
            S.frame_main.grid(**S.rc(0, 0), sticky = 'snew', **S.BORDER)
            S.frame_01.grid(**S.rc(0, 0, 1, 5), sticky = 'ne')
            S.label_02.grid(**S.rc(1, 0, 1, 5))
            S.label_04.grid(**S.rc(2, 0, 1, 5))
            S.label_03.grid(**S.rc(4, 0, 1, 5), sticky = 's')
            S.label_01.grid(**S.rc(0, 0), sticky = 'e')
            S.combobox_01.grid(**S.rc(0, 1), sticky = 'w')
            S.button_01.grid(**S.rc(3, 1), sticky = 'we', **S.BORDER)
            S.button_02.grid(**S.rc(3, 2), sticky = 'we', **S.BORDER)
            S.button_03.grid(**S.rc(3, 3), sticky = 'we', **S.BORDER)

    class Frame_02:
        def __init__(S, root_=None, widget_list_=None, ctrl_=None, lang_=None, rc_=None, border_=None):
            S.root = root_
            S.lang = lang_
            S.ctrl = ctrl_
            S.widget_list = widget_list_
            S.widget_list.append(S)
            S.rc = rc_
            S.BORDER = border_

            S.main = tk.Toplevel(S.root)
            S.main.title(S.lang.txt('txt_title'))
            S.main.columnconfigure(0, weight=1)
            S.main.rowconfigure(0, weight=1)
            S.main.protocol("WM_DELETE_WINDOW", lambda: S.ctrl.cmd(('02_button_01', )))

            S.frame_main = ttk.Frame(S.main)
            for c, w in enumerate([5, 1, 5]): S.frame_main.columnconfigure(index=c, weight=w)
            for r, w in enumerate([5, 1]): S.frame_main.rowconfigure(index=r, weight=w)
            S.label_01 = ttk.Label(S.frame_main, font=(tk.NONE, 12), justify='center')
            S.button_01 = ttk.Button(S.frame_main, command=lambda: S.ctrl.cmd(('02_button_01', )))

        def close(S):
            S.main.destroy()
            S.main.grab_release() 
            if S in S.widget_list:
                S.widget_list.remove(S)
            del S
             
        def show(S):
            S.frame_main.grid(**S.rc(0, 0), sticky = 'snew', **S.BORDER)
            S.label_01.grid(**S.rc(0, 0, 1, 3), padx=10, pady=30)
            S.button_01.grid(**S.rc(1, 1), pady=20, sticky='we')
            S.main.update_idletasks() #fit
            S.main.minsize(S.main.winfo_width(),S.main.winfo_height())
            S.main.grab_set()

        def refresh(S):
            S.main.title(S.lang.txt('txt_title'))
            S.label_01['text'] = S.lang.txt('txt_instruction')
            S.button_01['text'] = S.lang.txt('txt_btn_go_back')

    class Frame_03:
        def __init__(S, root_=None, widget_list_=None, ctrl_=None, lang_=None, rc_=None, border_=None):
            S.root = root_
            S.lang = lang_
            S.ctrl = ctrl_
            S.widget_list = widget_list_
            S.widget_list.append(S)
            S.rc = rc_
            S.BORDER = border_

            S.style = ttk.Style()
            S.style.configure('black.TLabel', foreground='#000000', font=(tk.NONE, '22', 'bold'))
            S.style.configure('green.TLabel', foreground='#00aa72', font=(tk.NONE, '22', 'bold'))
            S.style.configure('green.TButton', foreground='#00aa72', font=(tk.NONE, '10', 'bold'))
            S.style.configure('red.TButton', foreground='#e20048', font=(tk.NONE, '10', 'bold'))
            

            S.main = tk.Toplevel(S.root)
            S.main.title(S.lang.txt('txt_title'))
            S.main.columnconfigure(0, weight=1)
            S.main.rowconfigure(0, weight=1)
            S.main.protocol("WM_DELETE_WINDOW", lambda: S.ctrl.cmd(('03_button_10_11', )))

            S.frame_main = ttk.Frame(S.main)
            for c, w in enumerate([2,  1]): S.frame_main.columnconfigure(index=c, weight=w)
            for r, w in enumerate([3, 3, 3, 3, 1]): S.frame_main.rowconfigure(index=r, weight=w)
                        
            S.frame_01 = ttk.Frame(S.frame_main, height = 80, borderwidth=1, relief=tk.SOLID)
            S.label_01_01 = ttk.Label(S.frame_main)
            S.age_rbtn_01 = tk.StringVar()
            S.frame_01_02 = ttk.Frame(S.frame_main)
            for c, w in enumerate([1, 1, 1, 1, 1]): S.frame_01_02.columnconfigure(index=c, weight=w)
            S.frame_01_02.rowconfigure(0, weight=1)
            def age_rbtn_get():
                return S.ctrl.cmd(('03_r_button_00', S.age_rbtn_01.get()))
            S.age_rbtn_01_00 = ttk.Radiobutton(S.frame_01_02, value=0, variable=S.age_rbtn_01, command = lambda: age_rbtn_get())
            S.age_rbtn_01_01 = ttk.Radiobutton(S.frame_01_02, value=1, variable=S.age_rbtn_01, command = lambda: age_rbtn_get())
            S.age_rbtn_01_02 = ttk.Radiobutton(S.frame_01_02, value=2, variable=S.age_rbtn_01, command = lambda: age_rbtn_get())
            S.age_rbtn_01_03 = ttk.Radiobutton(S.frame_01_02, value=3, variable=S.age_rbtn_01, command = lambda: age_rbtn_get())
            S.age_rbtn_01_04 = ttk.Radiobutton(S.frame_01_02, value=4, variable=S.age_rbtn_01, command = lambda: age_rbtn_get())
            
            S.frame_02 = ttk.Frame(S.frame_main, height = 80, borderwidth=1, relief=tk.SOLID)
            S.frame_02_01 = ttk.Frame(S.frame_main)
            for r, w in enumerate([5, 1, 1]): S.frame_02_01.rowconfigure(index=r, weight=w)
            for c, w in enumerate([1, 10]): S.frame_02_01.columnconfigure(index=c, weight=w)
            S.label_02_01 = ttk.Label(S.frame_02_01, justify='center')
            S.label_02_02 = ttk.Label(S.frame_02_01)
            S.entry_value_02_01 = tk.IntVar()
            S.entry_02_01 = ttk.Entry(S.frame_02_01, textvariable=S.entry_value_02_01)
            S.frame_02_02 = ttk.Frame(S.frame_main)
            for r, w in enumerate([5, 1]): S.frame_02_02.rowconfigure(index=r, weight=w)
            S.frame_02_02.columnconfigure(0, weight=1)
            S.label_02_03 = ttk.Label(S.frame_02_02, style="black.TLabel", justify='center')
            S.btn_test_02_01 = ttk.Button(S.frame_02_02, command=lambda: S.ctrl.cmd(('03_button_test_01', )))
            
            S.frame_03 = ttk.Frame(S.frame_main, height = 80, borderwidth=1, relief=tk.SOLID)
            S.label_03_01 = ttk.Label(S.frame_main, justify='center')
            S.frame_03_01 = ttk.Frame(S.frame_main)
            for r, w in enumerate([5, 1]): S.frame_03_01.columnconfigure(index=c, weight=w)
            S.frame_03_01.columnconfigure(0, weight=1)
            S.label_03_02 = ttk.Label(S.frame_03_01, style="black.TLabel", justify='center')
            S.btn_test_03_01 = ttk.Button(S.frame_03_01, command=lambda: S.ctrl.cmd(('03_button_test_02', )))

            S.frame_04 = ttk.Frame(S.frame_main, height = 80, borderwidth=1, relief=tk.SOLID)
            S.frame_04_01 = ttk.Frame(S.frame_main)
            for r, w in enumerate([5, 1, 1, 1, 1]): S.frame_04_01.rowconfigure(index=r, weight=w)
            for c, w in enumerate([1, 10]): S.frame_04_01.columnconfigure(index=c, weight=w)
            S.label_04_01 = ttk.Label(S.frame_04_01, justify='center')
            S.label_04_02 = ttk.Label(S.frame_04_01)
            S.entry_value_04_01 = tk.IntVar()
            S.entry_04_01 = ttk.Entry(S.frame_04_01, textvariable=S.entry_value_04_01)
            S.label_04_03 = ttk.Label(S.frame_04_01)
            S.entry_value_04_02 = tk.IntVar()
            S.entry_04_02 = ttk.Entry(S.frame_04_01, textvariable=S.entry_value_04_02)
            S.frame_04_02 = ttk.Frame(S.frame_main)
            for r, w in enumerate([5, 1]): S.frame_04_02.rowconfigure(index=r, weight=w)
            S.frame_04_02.columnconfigure(0, weight=1)
            S.label_04_04 = ttk.Label(S.frame_04_02, style="black.TLabel", justify='center')
            S.btn_test_04_01 = ttk.Button(S.frame_04_02, command=lambda: S.ctrl.cmd(('04_button_test_03', )))
            
            S.frame_10 = ttk.Frame(S.frame_main)
            for c, w in enumerate([5, 1, 1, 1, 5]): S.frame_10.columnconfigure(index=c, weight=w)
            S.frame_10.rowconfigure(0, weight=1)
            S.button_10_11 = ttk.Button(S.frame_10, command=lambda: S.ctrl.cmd(('03_button_10_11', )))
            S.button_10_12 = ttk.Button(S.frame_10, style='red.TButton', command=lambda: S.ctrl.cmd(('03_button_10_12', )))
            S.button_10_13 = ttk.Button(S.frame_10, style='green.TButton', command=lambda: S.ctrl.cmd(('03_button_10_13', )))

            S.group_00 = [S.button_10_12, S.button_10_13]
            S.group_01 = [S.label_01_01, S.age_rbtn_01_00, S.age_rbtn_01_01, S.age_rbtn_01_02, S.age_rbtn_01_03, S.age_rbtn_01_04]
            S.group_02 = [S.label_02_01, S.label_02_02, S.entry_02_01, S.label_02_03, S.btn_test_02_01]
            S.group_03 = [S.label_03_01, S.label_03_02, S.btn_test_03_01]
            S.group_04 = [S.label_04_01, S.label_04_02, S.entry_04_01, S.label_04_03, S.entry_04_02, S.label_04_04, S.btn_test_04_01]

        def test_stage_00(S):
            for i in S.group_00 + S.group_02 + S.group_03 + S.group_04:
                i['state'] = 'disabled'
            for i in S.group_01:
                i['state'] = 'enabled'
            S.button_10_13['text'] = S.lang.txt('txt_btn_test_start')
            S.age_rbtn_01.set('')
            S.label_04_04['style'] = 'black.TLabel'
            S.refresh()

        def test_stage_01(S):
            S.button_10_13['state'] = 'enabled'

        def test_stage_02(S):
            S.button_10_12['state'] = 'enabled'
            S.button_10_13['state'] = 'disabled'
            for i in S.group_01:
                i['state'] = 'disabled'
            for i in S.group_02:
                i['state'] = 'enabled'
            S.button_10_13['text'] = S.lang.txt('txt_btn_test_next')

        def test_stage_03(S):
            S.btn_test_02_01['state'] = 'disabled'
            S.button_10_13['state'] = 'disabled'

        def test_stage_04(S):
            S.btn_test_02_01['state'] = 'enabled'    
            S.button_10_13['state'] = 'enabled'

        def test_stage_05(S):
            for i in S.group_02:
                i['state'] = 'disabled'
            for i in S.group_03:
                i['state'] = 'enabled'
        
        def test_stage_06(S):
            S.btn_test_03_01['state'] = 'disabled'
            S.button_10_13['state'] = 'disabled'

        def test_stage_07(S):
            S.btn_test_03_01['state'] = 'enabled'
            S.button_10_13['state'] = 'enabled'

        def test_stage_08(S):
            for i in S.group_03:
                i['state'] = 'disabled'
            for i in S.group_04:
                i['state'] = 'enabled'
            S.button_10_13['state'] = 'disabled'
            S.button_10_13['text'] = S.lang.txt('txt_btn_show_result')
        
        def test_stage_09(S):
            S.label_04_04['style'] = 'green.TLabel'
            S.btn_test_04_01['state'] = 'disabled'
            S.button_10_13['state'] = 'disabled'

        def test_stage_10(S):
            S.label_04_04['style'] = 'black.TLabel'
        
        def test_stage_11(S):
            S.label_04_04['style'] = 'green.TLabel'

        def test_stage_12(S):
            S.btn_test_04_01['state'] = 'enabled'
            S.label_04_04['style'] = 'black.TLabel'
            S.button_10_13['state'] = 'enabled'

        def get_input(S):
            return (S.age_rbtn_01.get(), S.entry_02_01.get(), S.entry_04_01.get(), S.entry_04_02.get())


        def timer_01_set(S, time_):
            S.label_02_03['text'] = time_ 
        def timer_02_set(S, time_):
            S.label_03_02['text'] = time_
        def timer_03_set(S, time_):
            S.label_04_04['text'] = time_  

        def close(S):
            S.main.destroy()
            S.main.grab_release() 
            if S in S.widget_list:
                S.widget_list.remove(S)
            del S
             
        def show(S):
            S.frame_main.grid(**S.rc(0, 0), sticky = 'snew', **S.BORDER)

            S.frame_01.grid(**S.rc(0, 0, 1, 2), sticky = 'snew', **S.BORDER)
            S.label_01_01.grid(**S.rc(0, 0), padx = 10)
            S.frame_01_02.grid(**S.rc(0, 1), padx = 10)
            S.age_rbtn_01_00.grid(**S.rc(0, 0), ipadx = 10)
            S.age_rbtn_01_01.grid(**S.rc(0, 1), ipadx = 10)
            S.age_rbtn_01_02.grid(**S.rc(0, 2), ipadx = 10)
            S.age_rbtn_01_03.grid(**S.rc(0, 3), ipadx = 10)
            S.age_rbtn_01_04.grid(**S.rc(0, 4), ipadx = 10)
        
            S.frame_02.grid(**S.rc(1, 0, 1, 2), sticky = 'snew', **S.BORDER)
            S.frame_02_01.grid(**S.rc(1, 0), padx = 10, pady = 10, sticky='w')
            S.label_02_01.grid(**S.rc(0, 0, 1, 2), padx = 10, pady = 10)
            S.label_02_02.grid(**S.rc(1, 0), padx = 10, sticky='w')
            S.entry_02_01.grid(**S.rc(2, 0), padx = 10, sticky='w')
            S.frame_02_02.grid(**S.rc(1, 1), padx = 10, pady = 10, sticky = 's') 
            S.label_02_03.grid(**S.rc(0, 0), ipadx = 10)
            S.btn_test_02_01.grid(**S.rc(1, 0), ipadx = 10)
            
            S.frame_03.grid(**S.rc(2, 0, 1, 2), sticky = 'snew', **S.BORDER)
            S.label_03_01.grid(**S.rc(2, 0), padx = 10) 
            S.frame_03_01.grid(**S.rc(2, 1), padx = 10, pady = 10, sticky = 's')
            S.label_03_02.grid(**S.rc(0, 0), ipadx = 10)
            S.btn_test_03_01.grid(**S.rc(1, 0), ipadx = 10)

            S.frame_04.grid(**S.rc(3, 0, 1, 2), sticky = 'snew', **S.BORDER)
            S.frame_04_01.grid(**S.rc(3, 0), padx = 10, pady = 10)
            S.label_04_01.grid(**S.rc(0, 0, 1, 2), padx = 10, pady = 10)
            S.label_04_02.grid(**S.rc(1, 0), padx = 10, sticky='w')
            S.entry_04_01.grid(**S.rc(2, 0), padx = 10, sticky='w')
            S.label_04_03.grid(**S.rc(3, 0), padx = 10, sticky='w')
            S.entry_04_02.grid(**S.rc(4, 0), padx = 10, sticky='w')
            S.frame_04_02.grid(**S.rc(3, 1), padx = 10, pady = 10, sticky = 's') 
            S.label_04_04.grid(**S.rc(0, 0), ipadx = 10)
            S.btn_test_04_01.grid(**S.rc(1, 0), ipadx = 10)


            S.frame_10.grid(**S.rc(4, 0, 1, 2), sticky = 'snew', **S.BORDER)
            S.button_10_11.grid(**S.rc(0, 1), sticky = 'we', **S.BORDER)
            S.button_10_12.grid(**S.rc(0, 2), sticky = 'we', **S.BORDER)
            S.button_10_13.grid(**S.rc(0, 3), sticky = 'we', **S.BORDER)

            S.main.update_idletasks() #fit
            S.main.minsize(S.main.winfo_width(),S.main.winfo_height())
            S.main.grab_set()

        def refresh(S):
            S.main.title(S.lang.txt('txt_title'))
            S.label_01_01['text'] = S.lang.txt('txt_age')

            S.age_rbtn_01_00['text'] = S.lang.txt('txt_age_0')
            S.age_rbtn_01_01['text'] = S.lang.txt('txt_age_1')
            S.age_rbtn_01_02['text'] = S.lang.txt('txt_age_2')
            S.age_rbtn_01_03['text'] = S.lang.txt('txt_age_3')
            S.age_rbtn_01_04['text'] = S.lang.txt('txt_age_4') 
            
            S.label_02_01['text'] = S.lang.txt('txt_test1')
            S.label_02_02['text'] = S.lang.txt('txt_test1_1')
            S.label_02_03['text'] = ''
            S.btn_test_02_01['text'] = S.lang.txt('txt_starttest1')

            S.label_03_01['text'] = S.lang.txt('txt_test2')
            S.label_03_02['text'] = ''
            S.btn_test_03_01['text'] = S.lang.txt('txt_starttest2')

            S.label_04_01['text'] = S.lang.txt('txt_test3')
            S.label_04_02['text'] = S.lang.txt('txt_test3_1')
            S.label_04_03['text'] = S.lang.txt('txt_test3_2')
            S.label_04_04['text'] = ""
            S.btn_test_04_01['text'] = S.lang.txt('txt_starttest3')

            S.button_10_11['text'] = S.lang.txt('txt_btn_go_back')
            S.button_10_12['text'] = S.lang.txt('txt_btn_test_stop')
            S.button_10_13['text'] = S.lang.txt('txt_btn_test_start')


    class Frame_04:
        def __init__(S, root_=None, widget_list_=None, ctrl_=None, lang_=None):
            S.root = root_
            S.lang = lang_
            S.ctrl = ctrl_
            S.widget_list = widget_list_
            S.widget_list.append(S)
            S.title = ''
            S.index = 0
            S.result = 0
            S.list_result_text = []
            S.result_text = ''
            S.resume_text = ''
            

        def show_result(S, result_):
            if result_ != None:
                S.index, S.result = result_
                tk.messagebox.showinfo(title=S.title, message=f'{S.result_text} {S.index}\n\n{S.resume_text} {S.list_result_text[S.result]}')
                # tk.simpledialog.askfloat('title', 'prompt', **kw)
                # tk.simpledialog.askinteger(title, prompt, **kw)
                # tk.simpledialog.askstring(title, prompt, **kw)¶

        def refresh(S):
            S.title = S.lang.txt('txt_title')
            S.result_text = S.lang.txt('txt_index')
            S.resume_text = S.lang.txt('txt_workheart')
            S.list_result_text.clear() 
            S.list_result_text.append(S.lang.txt('txt_res1'))
            S.list_result_text.append(S.lang.txt('txt_res2'))
            S.list_result_text.append(S.lang.txt('txt_res3'))
            S.list_result_text.append(S.lang.txt('txt_res4'))
            S.list_result_text.append(S.lang.txt('txt_res5'))

    def set_controller(self, ctrl_):
        self.ctrl = ctrl_
 
    def refresh(self):
        self.root.title(self.lang.txt('txt_title'))
        for widget in self.widget_list:
            widget.refresh()
        self.root.update()
    
    def show(self):
        for widget in self.widget_list:
            widget.show()

    def rc(self, r, c, rs=1, cs=1):
        return {'row':r, 'column':c, 'rowspan':rs, 'columnspan':cs}


if __name__ == '__main__':
    import language
    lang = language.Language()
    root = tk.Tk()
    test = View(root, lang)

    test.build_01()
    test.refresh()
    test.show()
    root.mainloop()
