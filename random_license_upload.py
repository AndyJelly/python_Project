# -*- coding: utf-8 -*-
# python2.7

from xml.etree import ElementTree as ET
import uuid
import subprocess
import re
import time
from random import randint


class XmlUtil(object):
    def __init__(self, text):
        if not text:
            raise ValueError('Empty XML!')
        else:
            if '<?' in text:
                self.xmlstr_ = text[text.find('?>') + 2:]
            else:
                self.xmlstr_ = text
            self.root = ET.fromstring(self.xmlstr_)

    def get_cnt(self, xmlpath):
        xmlpath = self._split_xpath(xmlpath)
        return len(self.root.findall(xmlpath))

    def get_v(self, xmlpath, pos=0):
        xmlpath = self._split_xpath(xmlpath)
        return self.root.findall(xmlpath)[pos].text

    def get_atrrib(self, xmlpath, pos=0):
        # 返回的是一个字典
        xmlpath = self._split_xpath(xmlpath)
        return self.root.findall(xmlpath)[pos].attrib

    def get_int(self, xmlpath, pos=0):
        return int(self.get_v(xmlpath, pos))

    def set_attrib(self, xmlpath, dict_attrib, pos=0):
        xmlpath = self._split_xpath(xmlpath)
        for k,v in dict_attrib.items():
            return self.root.findall(xmlpath)[pos].set(k, v)

    def to_string(self):
        return ET.tostring(self.root, encoding='utf-8')

    # def write_to_file(self, file_path):
    #     return ET.write(file_path, encoding='utf-8')

    def _split_xpath(self, xmlpath):
        if not xmlpath:
            raise ValueError('Invaild xpath!')
        else:
            xpathlist = xmlpath.split('/')[2:]
            return '/'.join(xpathlist)


list_random_license = []


def modify_upload_license(file_path='./', license_plate=''):
    with open(file_path + 'config.xml', 'r') as cfg_file:
        xml_content = cfg_file.read()

    obj = XmlUtil(xml_content)
    sLicense_attrib = obj.get_atrrib('/ALARM/struPlateInfo/sLicense')   # {'value': 'A8888866'}
    # print(sLicense_attrib)

    sLicense_attrib['value'] = license_plate     # get_random_string(6)
    # print(sLicense_attrib)
    obj.set_attrib('/ALARM/struPlateInfo/sLicense', sLicense_attrib)
    sLicense_attrib = obj.get_atrrib('/ALARM/struPlateInfo/sLicense')  # {'value': 'A8888866'}
    print(sLicense_attrib)
    xml_new_content = obj.to_string()

    with open(file_path + 'config.xml', 'w+') as cfg_file:
        cfg_file.write(xml_new_content)


def get_random_string(string_length=10):
    str_random = str(uuid.uuid4()).upper()
    # print(str_random)
    str_random = str_random.replace("-", "")
    return str_random[0: string_length]


def get_config_file_path():
    exec_path = get_prcoess_exec_path('HCSimulateDevice')
    return exec_path + '/Alarm/COMM_UPLOAD_PLATE_RESULT/'


def get_prcoess_exec_path(process_name=''):
    # psutil 三方库获取 https://www.liaoxuefeng.com/wiki/1016959663602400/1183565811281984

    # 自动获取 进程的执行目录
    system_cmd = 'wmic process where name="' + process_name + '.exe" get ExecutablePath'       # wmic process where name="HCSimulateDevice.exe"
    ret = subprocess.Popen(system_cmd, stdout=subprocess.PIPE).communicate()[0]
    '''
        C:\Users\huguodong>wmic process where name="HCSimulateDevice.exe" get ExecutablePath
        ExecutablePath
        D:\Tools\HCSimulatorV2.3.3.1_build20210125_WIN32_ZH\lib\HCSimulateDevice.exe 
    '''
    ret = str(ret)
    print(ret)

    if 'No Instance(s) Available' in ret:
        raise ValueError('No Instance(s) Available')

    list_str_ret = ret.split("\r\n", 1)
    # print(list_str_ret)
    title = re.split(r"[ ]+", list_str_ret[0])
    value = re.split(r"[ ]+", list_str_ret[1])

    dict_proc_info = {}
    for i in range(0, min(len(title), len(value))):
        dict_proc_info[title[i]] = value[i]
    print(dict_proc_info)

    if 'ExecutablePath' not in dict_proc_info:
        raise ValueError('Get ExecutablePath Failed')

    # print(dict_proc_info['ExecutablePath'])
    exec_path =''
    for item in dict_proc_info['ExecutablePath'].split('\\')[:-1]:
        exec_path += (item + ('/'))
    # print(exec_path)
    return exec_path

	```
	#Root
log4j.rootLogger=INFO, R

log4j.appender.R=org.apache.log4j.RollingFileAppender
log4j.appender.R.Append=true
log4j.appender.R.File=../Log/SYS/vehiclebiz.s/default.log
log4j.appender.R.MaxFileSize=40MB
log4j.appender.R.MaxBackupIndex=5
log4j.appender.R.layout=org.apache.log4j.PatternLayout
log4j.appender.R.layout.ConversionPattern=[%d][%c][%p]%m[%t]%n

#LPR 
log4j.logger.vehiclebiz.s.anpr=INFO, vehiclebiz.s.anpr
log4j.appender.vehiclebiz.s.anpr=org.apache.log4j.RollingFileAppender
log4j.appender.vehiclebiz.s.anpr.Append=true
log4j.appender.vehiclebiz.s.anpr.File=../Log/SYS/vehiclebiz.s/LPR.log
log4j.appender.vehiclebiz.s.anpr.MaxFileSize=40MB
log4j.appender.vehiclebiz.s.anpr.MaxBackupIndex=5
log4j.appender.vehiclebiz.s.anpr.layout=org.apache.log4j.PatternLayout
log4j.appender.vehiclebiz.s.anpr.layout.ConversionPattern=[%d][%c][%p]%m[%t]%n
log4j.additivity.vehiclebiz.s.anpr=false
	```
	

if __name__ == '__main__':

    # random_mode = input('请输入车牌随机模式（1-一直随机，2-指定集合范围内随机）：')
    # # print(type(random_mode))
    #
    # if int(random_mode) != 1 and int(random_mode) != 2:
    #     raise ValueError('Error  Mode')
    #
    # freq = input('请输入车牌上报频率（单位:s）：')
    # # print(type(freq))
    #
    # if int(random_mode) == 2:
    #     for i in range(0, 10):                 # 默认100个车牌
    #         license_plate = get_random_string(6)
    #         list_random_license.append(license_plate)
    #     print(list_random_license)
    #
    file_path = get_config_file_path()
    freq = 30
    random_mode = 1
    while 1:

        if random_mode == 1:
            license_plate = get_random_string(6)
        elif random_mode == 2:
            index_num = randint(1, 1000) % len(list_random_license)
            license_plate = list_random_license[index_num]

        modify_upload_license(file_path, license_plate)

        time.sleep(int(freq))

    # get_prcoess_exec_path('HCSimulateDevice')



