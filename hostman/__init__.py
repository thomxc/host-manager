import urllib.request
import re

filename = '/etc/hosts'
hosts_url = 'https://someonewhocares.org/hosts/hosts'

string_begin = '## HostGenerated BEGIN ##'
string_end = '## HostGenerated END ##'
def main():
    request = urllib.request.Request(hosts_url)
    response = urllib.request.urlopen(request).read().decode('utf-8')

    # read file
    with open(filename, 'r') as file:
        read = file.read()

    # print(read)
    hosts = string_begin + '\n' + response + '\n' + string_end
    # replace with regex
    replaced = re.sub(r'' + string_begin +'\s+([\w\W]*)\s+' + string_end, '', read)
    # write file back
    with open(filename, 'w') as file:
        file.writelines(replaced)

    with open(filename, 'a') as file:
        file.writelines(hosts)


if __name__ == '__main__':
    main()


