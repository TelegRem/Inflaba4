import re


def convert_xml_to_yaml():
    input_path = "C:/Users/User/Desktop/ИТМО/Информатика/Лабы/Лаба 4/pythonProject1/data/schedule.xml"
    output_path = "C:/Users/User/Desktop/ИТМО/Информатика/Лабы/Лаба 4/pythonProject1/data/task2_schedule.yaml"

    openTag = r'<([^/]\w+)>'
    closeTag = r'</\w+>'
    lstClass = r'\s{12}<(\w+)>'
    lstDay = r'\s{4}<(\w+) name="(\w+)">'
    tab = r'    '
    overflow = r'\s{7}-\s(\w+:\s{1}(\d+:\d+|\w+))'

    with open(input_path, 'r', encoding='utf-8') as scheduleXml:

        s = scheduleXml.read()[39:]

        s = re.sub(lstClass, "        - \\1: ", s)

        s = re.sub(lstDay, "- \\1:\n      '@name': \\2", s)

        s = re.sub(openTag, '\\1: ', s)
        s = re.sub(closeTag, '', s)
        print(s)
        s = re.sub(tab, '  ', s)
        s = re.sub(r'(\s*<[^/].*?>)(.*?)(?=<)', r'\1\n\2', s)
        s= re.sub(overflow,'\n        \\1',s)
        line = s.split('\n')
        lines = filter(str.strip, line)
        s = '\n'.join(lines)

        with open(output_path, 'a', encoding='utf-8') as scheduleYaml:
            scheduleYaml.write(s)


