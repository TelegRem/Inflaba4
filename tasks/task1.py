import xmltodict
import yaml

def lib_xml_to_yaml():
    input_file = "C:/Users/User/Desktop/ИТМО/Информатика/Лабы/Лаба 4/pythonProject1/data/schedule.xml"
    output_file = "C:/Users/User/Desktop/ИТМО/Информатика/Лабы/Лаба 4/pythonProject1/data/task1_schedule.yaml"
    with open(input_file, 'r', encoding='utf-8') as xml_file:
        xml_dict = xmltodict.parse(xml_file.read())

    with open(output_file, 'w', encoding='utf-8') as yaml_file:
        yaml.dump(xml_dict, yaml_file, allow_unicode=True)




