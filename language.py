class Language():
    def __init__(self):
        self.language_native = 'RUS'
        self.language_current = self.language_native
        self.languages_list = []
        self.languages = {
                'RUS':
                {'local_name': 'Русский',
                'txt_title': 'Здоровье - Тест Руфье',
                'txt_title_main': 'Тест Руфье',
                'txt_hello': 'Добро пожаловать в программу по определению состояния здоровья!\n\nЭто приложение позволит вам провести первичную диагностику\nвашего здоровья',
                'txt_instruction': 'Проба (тест) Руфье представляет собой нагрузочный комплекс,\n'
                                    'предназначенный для оценки работоспособности сердца при физической нагрузке.\n\n'
                                    'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                                    'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n\n'
                                    'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                                    'а потом — за последние 15 секунд первой минуты периода восстановления.\n\n'
                                    'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение,\n'
                                    'шум в ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.',
                'txt_age': 'Выберите ваш возраст (полных лет):',
                'txt_age_0': '7–8 лет',
                'txt_age_1': '9—10 лет',
                'txt_age_2': '11–12 лет',
                'txt_age_3': '13–14 лет',
                'txt_age_4': 'от 15 лет и старше',                                
                'txt_btn_help': 'Как это работает',
                'txt_btn_results': 'Результаты',
                'txt_btn_go_testing': 'Начать тестирование',
                'txt_btn_go_back': 'Назад',
                'txt_btn_test_stop': 'Остановить',
                'txt_btn_test_start': 'Старт',
                'txt_btn_test_next': 'Далее',
                'txt_btn_show_result': 'Результат теста',
                'txt_test1': 'Лягте на спину и замерьте пульс за 15 секунд.\n'
                                'Нажмите кнопку «Начать первый тест», чтобы запустить таймер.\n'
                                'Результат запишите в соответствующее поле.',
                'txt_test1_1': 'пульс за 15 секунд',                                
                'txt_test2': 'Выполните 30 приседаний за 45 секунд.\n'
                                'Для этого нажмите кнопку «Начать делать приседания»,'
                                '\nчтобы запустить счетчик приседаний.',
                'txt_test3': 'Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты,\n'
                                'затем за последние 15 секунд.\n'
                                'Нажмите кнопку «Начать финальный тест», чтобы запустить таймер.\n'
                                'Зеленым обозначены секунды, в течение которых необходимо проводить измерения,\n'
                                'черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.',
                'txt_test3_1': 'пульс за первые 15 секунд',
                'txt_test3_2': 'пульс за последние 15 секунд',
                #'txt_next': 'Начать',
                # 'txt_name': 'Введите Ф.И.О.:',
                # 'txt_hintname': "Ф.И.О.",
                #txt_hintage = "0"
                #'txt_sendresults': 'Отправить результаты',
                #txt_hinttest1 = '0'
                #txt_hinttest2 = '0'
                #txt_hinttest3 = '0'
                'txt_starttest1': 'Начать первый тест',
                'txt_starttest2': 'Начать делать приседания',
                'txt_starttest3': 'Начать финальный тест',
                #'txt_finalwin': 'Результаты',
                'txt_index': 'Индекс Руфье:',
                'txt_workheart': 'Работоспособность сердца:',
                'txt_res1': "низкая. Срочно обратитесь к врачу!",
                'txt_res2': "удовлетворительная. Обратитесь к врачу!",
                'txt_res3': "средняя. Возможно, стоит дополнительно обследоваться у врача.",
                'txt_res4': "выше среднего",
                'txt_res5': "высокая"
                },

                'ENG':
                {'local_name': 'English',
                'txt_title': 'Health - Test Ruffier',
                'txt_title_main': 'Test Ruffier',
                'txt_hello': 'Welcome to the health assessment program!\n\nThis application will allow you\n to conduct a primary diagnosis of your health',
                'txt_instruction': 'Sample (test) Rufier is a load complex,\n'
                                    'designed to assess the performance of the heart during exercise.\n\n'
                                    'The subject, who is in the supine position for 5 minutes, determines the pulse rate for 15 seconds;\n'
                                    'then, within 45 seconds, the subject performs 30 squats.\n\n'
                                    'After the end of the load, the subject lies down, and the number of pulsations is again calculated for him in the first 15 seconds,\n'
                                    'and then for the last 15 seconds of the first minute of the recovery period.\n\n'
                                    'Important! If during the test you feel unwell (dizziness appears,\n'
                                    'tinnitus, severe shortness of breath, etc.), then the test should be interrupted and consult a doctor.',
                'txt_age': 'Select your age (full years):',
                'txt_age_0': '7–8 years',
                'txt_age_1': '9—10 years',
                'txt_age_2': '11–12 years',
                'txt_age_3': '13–14 years',
                'txt_age_4':'more than 15',
                'txt_btn_help': 'How it work',
                'txt_btn_results': 'Results',
                'txt_btn_go_testing': 'Start testing',
                'txt_btn_go_back': 'Back',
                'txt_btn_test_stop': 'Cancel',
                'txt_btn_test_start': 'Start',
                'txt_btn_test_next': 'Next',
                'txt_btn_show_result': 'Result of test',
                'txt_test1': 'Lie on your back and take your pulse for 15 seconds.Click the «Start first Test» button to start the timer.\n'
                            'Write the result in the corresponding field.',
                'txt_test1_1': 'pulse in 15 seconds',
                'txt_test2': 'Perform 30 squats in 45 seconds. To do this, click the «Start doing squats» button.,\nto start the squat counter.',
                'txt_test3': 'Lie on your back and take your pulse, first for the first 15 seconds of the minute, then for the last 15 seconds.\n'
                                'Click the «Start Final Test» button to start the timer.\n'
                                'Green indicates the seconds during which it is necessary totake measurements,\n'
                                'black - seconds without measuring pulsations. Record the results in the appropriate fields.',
                'txt_starttest1': 'Start first test',
                'txt_starttest2': 'Start doing squats',
                'txt_starttest3': 'Start final test',
                'txt_test3_1': 'pulse in the first 15 seconds',
                'txt_test3_2': 'pulse in the last 15 seconds',
                #'txt_finalwin': 'Results',
                'txt_index': 'Rufier index:',
                'txt_workheart': 'Heart performance:',
                'txt_res1': "low. Urgently consult a doctor!",
                'txt_res2': "satisfactory. Consult a doctor!",
                'txt_res3': "average. It may be worth further examination by a doctor.",
                'txt_res4': "above average",
                'txt_res5': "high"
                }}
        
    def txt(self, txt=''):
        if txt in self.languages[self.language_current]:          
            return self.languages[self.language_current][txt]
        else:
            return '-нет значения-'
