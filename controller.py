class Controller:
    def __init__(self, model_, view_):
        self.model = model_
        self.view = view_
        self.test_stage = 0

    def start(self):
        self.view.build_01()

    def cmd(self, command_):
        cmd = command_[0]
        #print('command_:', command_, '\t', 'stage:', self.test_stage)

        if cmd == '01_combobox_01':
            self.model.lang.language_current = command_[1]
            self.view.refresh()
        elif cmd == '01_button_01':
            self.view.build_02()
        elif cmd == '02_button_01':
            self.view.frame_02.close()
        elif cmd == '01_button_03':
            self.view.build_03()
            self.view.build_04()
            self.model.timers_make()

        elif cmd == '03_r_button_00':
            self.test_stage = 1
            self.view.frame_03.test_stage_01()
            
        elif cmd == '03_button_10_13' and self.test_stage == 1:
            self.test_stage = 2
            self.view.frame_03.test_stage_02()
            
        elif cmd == '03_button_test_01':
            self.test_stage = 3
            self.view.frame_03.test_stage_03()
            self.model.timer_01.caller = '03_button_test_01_timer'
            self.model.timer_01.start()

        elif cmd == '03_button_test_01_timer':
            if command_[1] != 'stop':
                self.view.frame_03.timer_01_set(command_[1])
            else:
                self.test_stage = 4
                self.view.frame_03.test_stage_04()
                self.view.frame_03.timer_01_set('')

        elif cmd == '03_button_10_13' and self.test_stage == 4:
            self.test_stage = 5
            self.view.frame_03.test_stage_05()

        elif cmd == '03_button_test_02':
            self.test_stage = 6
            self.view.frame_03.test_stage_06()
            self.model.timer_02.caller = '03_button_test_02_timer'
            self.model.timer_02.start()
        elif cmd == '03_button_test_02_timer':
            if command_[1] != 'stop':
                self.view.frame_03.timer_02_set(command_[1])
            else:
                self.test_stage = 7
                self.view.frame_03.test_stage_07()
                self.view.frame_03.timer_02_set('')    

        elif cmd == '03_button_10_13' and self.test_stage == 7:
            self.test_stage = 8
            self.view.frame_03.test_stage_08()
        
        elif cmd == '04_button_test_03':
            self.test_stage = 9
            self.view.frame_03.test_stage_09()
            self.model.timer_03.caller = '04_button_test_03_timer_01'
            self.model.timer_03.start()

        elif cmd == '04_button_test_03_timer_01':
            if command_[1] != 'stop':
                self.view.frame_03.timer_03_set(command_[1])
            else:
                self.test_stage = 10
                self.view.frame_03.test_stage_10()
                self.model.timer_04.caller = '04_button_test_03_timer_02'
                self.model.timer_04.start()
                #self.view.frame_03.timer_02_set('')

        elif cmd == '04_button_test_03_timer_02':
            if command_[1] != 'stop':
                self.view.frame_03.timer_03_set(command_[1])
            else:
                self.test_stage = 11
                self.view.frame_03.test_stage_11()
                self.model.timer_05.caller = '04_button_test_03_timer_03'
                self.model.timer_05.start()
                #self.view.frame_03.timer_02_set('')

        elif cmd == '04_button_test_03_timer_03':
            if command_[1] != 'stop':
                self.view.frame_03.timer_03_set(command_[1])
            else:
                self.test_stage = 12
                self.view.frame_03.test_stage_12()
                self.view.frame_03.timer_03_set('')

        elif cmd == '03_button_10_13' and self.test_stage == 12:
            self.result = self.model.ruffier_test.result(self.view.frame_03.get_input())
            self.view.frame_04.show_result(self.result)

        
        elif cmd == '03_button_10_12':
            self.test_stage = 0
            self.view.frame_03.test_stage_00()
            self.model.timers_stop()

        elif cmd == '03_button_10_11':
            self.test_stage = 0
            self.view.frame_03.close()
            self.model.timers_stop()
