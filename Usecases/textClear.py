import re
import string


def text_clear(data_string):
    data_string = data_string.encode('ascii', 'ignore').decode()
    data_string = re.sub(r'https*\S+', ' ', data_string)
    data_string = re.sub(r'@\S+', ' ', data_string)
    data_string = re.sub(r'#\S+', ' ', data_string)
    data_string = re.sub(r'\'\w+', '', data_string)
    data_string = re.sub('[%s]' % re.escape(string.punctuation), ' ', data_string)
    data_string = re.sub(r'\w*\d+\w*', '', data_string)
    data_string = re.sub(r'\s{2,}', ' ', data_string)
    return data_string
