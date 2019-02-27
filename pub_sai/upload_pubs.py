from pybtex.database.input import bibtex
from pub.models import Pub, Person
from django.core.exceptions import ValidationError
from usage_log.ChangeItemDataManager import ChangeItemDataManager
import pdb

def upload_bibtex(user,path):
    cdm = ChangeItemDataManager()
    success = []
    errors = []
    # open a bibtex file
    parser = bibtex.Parser()
    bibdata = parser.parse_file(path)
    pub_field_names = [field.name for field in Pub._meta.get_fields()]

    for citekey in bibdata.entries:
        try:
            persons = bibdata.entries[citekey].persons
            fields = dict(bibdata.entries[citekey].fields)
            args = {}
            args['citekey']=citekey
            args['type']=bibdata.entries[citekey].type
            for field_key,value in fields.items():
                if field_key in pub_field_names and field_key!=citekey and field_key!='type':
                    args[field_key]=value
            pdb.set_trace()
            pub = Pub.rmobjects.create(**args)
            for (role,role_persons) in persons.items():
                for person in role_persons:
                    first_names = person.first_names
                    middle_names = person.middle_names
                    last_names = person.last_names
                    args = {}
                    if first_names!= []:
                        args['first_names']=first_names[0].encode('utf8')
                    if middle_names!= []:
                        args['middle_names']=middle_names[0].encode('utf8')
                    if last_names!= []:
                        args['last_names']=last_names[0].encode('utf8')
                    p = Person.rmobjects.get_or_create(**args)
                    if role == 'lastname' and p[0] is not None:
                        pub.author.add(p[0])
                    elif role == 'middlename' and p[0] is not None:
                        pub.author.add(p[0])
                    elif role == 'firstname' and p[0] is not None:
                        pub.author.add(p[0])
                    elif role =='author' and p[0] is not None:
                        pub.author.add(p[0])
                    elif role=='editor' and p[0] is not None:
                        pub.editor.add(p[0])
            pub.save()
            success.append('Publication '+citekey+' upoad successful.')
            change_item_comment = 'Created Publication'
            cdm.create_change_item(user,change_item_comment,pub)
        except ValidationError as e:
            errors.append(e.messages[0])

    return (success, errors)