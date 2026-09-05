import sys, os, pathlib

class Model:
    def __init__(self, root_, lang_, lang_file_mask_pattern_ = ''):
        self.root = root_
        self.ctrl = None
        self.lang = lang_
        self.lang.languages_list += self.lang.languages.keys()

        self.app_path_and_name = sys.argv[0]
        self.app_path = os.path.dirname(self.app_path_and_name)
        self.app_name = os.path.basename(self.app_path_and_name)
        self.app_name_0 = os.path.splitext(self.app_name)[0]

        if lang_file_mask_pattern_ == '':
            self.lang_file_mask_pattern = self.app_name_0 + '.lng-???'
        else:
            self.lang_file_mask_pattern = lang_file_mask_pattern_ + '.lng-???'
        
        self.lang_file_list = self.get_list_files_by_mask()
        if len(self.lang_file_list) > 0:
            for self.i_lang in self.lang_file_list:
                self.new_lang_name = os.path.splitext(os.path.basename(self.i_lang))[1].split('-')[1].upper()
                self.lang.languages_list.append(self.new_lang_name)
                self.lang.languages[self.new_lang_name] = dict()
                
                with open(self.i_lang, 'r', encoding='utf-8') as file:
                    for line in file:
                        self.temp_item = line.split(',')
                        if len(self.temp_item) == 2:
                            if self.temp_item[0] in self.lang.languages[self.lang.language_native]:
                                self.lang.languages[self.new_lang_name][self.temp_item[0]] = self.temp_item[1].replace('\n','')
            
        self.lang.languages_list.sort()
      
        self.ruffier_test = self.Ruffier_test()
    
    class Ruffier_test:
        def __init__(S):
            S.age = 0
            S.P1, S.P2, S.P3 = 0, 0, 0
            S.index = 0
            S.data = {0:[0, 6.5, 12, 17, 21, 200],
                        1:[0, 5, 10.5, 15.5, 19.5, 200],
                        2:[0, 3.5, 9, 14, 19, 200],
                        3:[0, 2, 7.5, 12.5, 16.5, 200],
                        4:[0, 0.5, 6, 11, 15, 200]}
        def result(S, measurements_):
            S.age, S.P1, S.P2, S.P3 = tuple(map(int, measurements_))
            S.index = (4 * (S.P1 + S.P2 + S.P3) - 200) / 10
            for i in range(5):
                if S.data[S.age][i] <= S.index < S.data[S.age][i+1]:
                    return (S.index, i)
    
    def timers_make(S):
        S.timer_01 = S.Timer(S.root, S.ctrl, 15, 0, 1000)
        S.timer_02 = S.Timer(S.root, S.ctrl, 0, 30, 1500)
        S.timer_03 = S.Timer(S.root, S.ctrl, 60, 45, 1000)
        S.timer_04 = S.Timer(S.root, S.ctrl, 44, 16, 1000)
        S.timer_05 = S.Timer(S.root, S.ctrl, 15, 0, 1000)

    def timers_stop(S):
        S.timer_01.stop()
        S.timer_02.stop()
        S.timer_03.stop()
        S.timer_04.stop()
        S.timer_05.stop()

    class Timer:
        def __init__(S, root_, ctrl_, begin_ = 0, end_ = 0, delay_ = 0):
            S.root = root_
            S.ctrl = ctrl_
            S.begin = begin_
            S.step = 0
            S.end = end_
            S.delay = delay_
            S.name = None
            S.caller = ''

        def start(S):
            if S.name != None:
                S.root.after_cancel(S.name)
            S.step = S.begin
            S.tick()
        
        def stop(S):
            if S.name != None:
                S.root.after_cancel(S.name)

        def tick(S):
            if S.begin < S.end:
                if S.step <= S.end:
                    S.name = S.root.after(S.delay, S.tick)
                    S.ctrl.cmd((S.caller, S.step))
                    S.step += 1
                else:
                    S.ctrl.cmd((S.caller, 'stop'))    
            elif S.begin > S.end:
                if S.step >= S.end:
                    S.name = S.root.after(S.delay, S.tick)
                    S.ctrl.cmd((S.caller, S.step))
                    S.step -= 1
                else:
                    S.ctrl.cmd((S.caller, 'stop')) 

    def get_list_files_by_mask(self):
        currentDirectory = pathlib.Path(self.app_path)
        list_files = []
        for currentFile in currentDirectory.glob(self.lang_file_mask_pattern):
            list_files.append(currentFile)
        return list_files
    def set_controller(self, ctrl_):
        self.ctrl = ctrl_

if __name__ == '__main__':
    import language
    lang = language.Language()
    model = Model(lang, 'app-health-2023')
    print(model.lang.txt('local_name'))
    print(model.lang.languages_list)
    model.ruffier_test.age = 4
    model.ruffier_test.index = 16
    print(model.ruffier_test.result())