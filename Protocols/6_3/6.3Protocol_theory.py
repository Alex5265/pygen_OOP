
def parse_file_number():
    flag_script = False
    res = {}
    with open(r'F:\python\9208863050.vxml', 'rt', encoding='UTF-8') as number:
        for row in number:
            if '<script>' in row:
                print('hi')
                flag_script = True
            if '</script>' in row:
                flag_script = False
            if flag_script and '=' in row:
                key, val = row.strip().split('=', 1)
                res[key.strip()] = val.strip()
    return res


n = parse_file_number()


for k,v in n.items():
    print(f'{k} : {v}')