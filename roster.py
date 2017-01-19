import pyexcel
from glob import glob
from base64 import b64encode

def dataurl(fname):
    ans = 'data:image/{};base64,'.format('png' if fname.endswith('png') else 'jpeg')
    with open(fname, 'rb') as stream:
        ans += b64encode(stream.read()).decode('ascii')
    return ans

fname = sorted(glob('*.xls'))[-1]
records = pyexcel.get_sheet(file_name=fname, name_columns_by_row=1, sheet_name='Groups')
done = set(['','User ID'])
for record in records.to_records():
    try:
        if record['User ID'] in done: continue
        else: done.add(record['User ID'])
        
        if 'Groups' not in record or len(record['Groups']) == 0:
            grp = 'staff'
        else:
            grp = sorted(record['Groups'].split(', '))[-1].split(' ')[2]
            if grp[3] == '0': grp = grp[5:]
            else: grp = grp[:4]
        img = glob('/home/lat7h/Students/'+record['User ID']+'.jpg')+glob('/home/lat7h/Students/'+record['User ID']+'@*.jpg')+['/home/lat7h/Students/empty.png']
        img=dataurl(img[0])
        print("INSERT OR IGNORE INTO person (compid, name, image, role, section, help_time, last_helped) VALUES ('{}', '{}', '{}', '{}', '{}', 0, 0);".format(
            record['User ID'].replace("'", "''"),
            record['Name'].replace("'", "''"),
            img.replace("'", "''"),
            'Student' if 'tud' in record['Role'] else 'Staff',
            grp.replace("'", "''"),
        ))
    except IndexError:
        pass


records = pyexcel.get_sheet(file_name=fname, name_columns_by_row=1, sheet_name='Roster')
for record in records.to_records():
    try:
        if record['User ID'] in done: continue
        else: done.add(record['User ID'])
        
        img = glob('/home/lat7h/Students/'+record['User ID']+'.jpg')+glob('/home/lat7h/Students/'+record['User ID']+'@*.jpg')+['/home/lat7h/Students/empty.png']
        img=dataurl(img[0])
        print("INSERT OR IGNORE INTO person (compid, name, image, role, section, help_time, last_helped) VALUES ('{}', '{}', '{}', '{}', null, 0, 0);".format(
            record['User ID'].replace("'", "''"),
            record['Name'].replace("'", "''"),
            img.replace("'", "''"),
            'Student' if 'tud' in record['Role'] else 'Staff',
            grp.replace("'", "''"),
        ))
    except IndexError:
        pass
