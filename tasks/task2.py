import re


def convert_xml_to_yaml():
    input_path = "C:/Users/User/Desktop/ИТМО/Информатика/Лабы/Лаба 4/pythonProject1/data/schedule.xml"
    output_path = "C:/Users/User/Desktop/ИТМО/Информатика/Лабы/Лаба 4/pythonProject1/data/task3_schedule.yaml"

    openTag = r'<([^/]\w+)>'
    closeTag = r'</\w+>'
    lstClass = r'            <class>'
    lstDay = r'    <day name="(\w+)">'
    tab = r'    '

    with open(input_path, 'r', encoding='utf-8') as scheduleXml:

        s = scheduleXml.read()[39:]

        s = re.sub(lstClass, '      - class:', s)
        s = re.sub(lstDay, "- day:\n      '@name': \\1", s)
        s = re.sub(openTag, '\\1: ', s)
        s = re.sub(closeTag, '', s)
        s = re.sub(tab, '  ', s)

        s = re.sub(r'(\s*<[^/].*?>)(.*?)(?=<)', r'\1\n\2', s)

        with open(output_path, 'a', encoding='utf-8') as scheduleYaml:
            scheduleYaml.write(s)


