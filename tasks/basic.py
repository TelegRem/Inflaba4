
def simple_xml_yaml():
    scheduleXml = open('C:/Users/User/Desktop/ИТМО/Информатика/Лабы/Лаба 4/pythonProject1/data/schedule.xml', mode='r', encoding='utf-8')
    scheduleYaml = open('C:/Users/User/Desktop/ИТМО/Информатика/Лабы/Лаба 4/pythonProject1/data/basic_schedule.yaml', mode='a', encoding='utf-8')
    schedule = [line.rstrip() for line in scheduleXml]

    for line in range(1, len(schedule)):
        s = schedule[line]
        for symbol in range(0, len(schedule[line])-1):
            if s[symbol] == '<' and s[symbol + 1] == '/':
                s = s[:symbol]
                break
            if s[symbol] == '<':
                s = s.replace(s[symbol], '*', 1)
            if s[symbol+1] == '>':
                s = s.replace(s[symbol+1], '&', 1)
            if s[symbol] == s[symbol+1] == ' ':
                s = s.replace(s[symbol], '?', 1)
                s = s.replace(s[symbol+1], '^', 1)



        s = s.replace('*', '').replace('&', ': ').replace('?^', ' ')
        if s == '      class: ':
            s = '    - class: '
        if s == '  day name="Saturday": ':
            s = "- day: \n    '@name': Saturday"
        if s.strip() == '':
            continue


        scheduleYaml.write(s + '\n')
    scheduleXml.close()
    scheduleYaml.close()