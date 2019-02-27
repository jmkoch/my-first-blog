from pub.models import Pub, Person
from pub.forms import PubForm, PubUpdateForm
import pub.upload_pubs as upload_pubs
from django.core.exceptions import ValidationError
from usage_log.ChangeItemDataManager import ChangeItemDataManager
import pdb

class PubDataManager():
    """Defines and implements sets of user functions to upload, edit, and delete Publications. Also
     abstracts a current instance or working set of Publications"""
    current_pub_query = Pub.rmobjects.all()
    current_person_query = Person.rmobjects.all()

    cdm = ChangeItemDataManager()

    def browse_query_pubs(self,user,query_params,match_type):
        """
        Returns a set of Pub records matching a query defined by query_params and match t`ype
        :param user: user currently logged into Traitable
        :param query_params: query parameters (dict)
        :param match_type: 'exact' or 'partial'
        :return: the query data and the query filters or None if user does not have proper permissions
        """
        original_data = query_params
        if user.has_perm("pubs.view_pub"):
            if match_type ==None or match_type=='exact':
                query_data = Pub.rmobjects.filter(**query_params)
                self.current_query = query_data
            else:
                for citekey in query_params.citekeys():
                    query_params[citekey+"__icontains"]=query_params.pop(citekey)
                query_data = Trait.rmobjects.filter(**query_params)
                self.current_pub_query = query_data
            return query_data, original_data
        else:
            return None, None

    def browse_single_pub(self,user,pub_key):
        """
        Returns a single publication given ciation key
        :param user: user currently logged into Traitable
        :param pub_key: citation key
        :return: the Pub record or None if user does not have proper permissions
        """
        if user.has_perm("pubs.view_pub"):
            return Pub.rmobjects.get(citekey=pub_key)
        else:
            return None

    def update_pub(self,user,pub_key,update_data):
        """
        Updates publication with citation key key and update data update_data
        :param user: user currently logged into Traitable
        :param pub_key: citation key of Pub to update
        :param update_data: dict of params and values to update
        :return: True if Publication is updated with update_data, False if update fails, None if user does not have proper permissions
        """
        if user.has_perm("pubs.change_pub"):
            original = Pub.rmobjects.get(citekey=pub_key)
            form = PubUpdateForm(update_data, instance=original)
            if form.is_valid():
                form.save()
                changed_fields = form.changed_data
                changed_fields.remove('comment')
                change_item_fields = ', '.join(changed_fields)
                change_item_comment = update_data['comment']
                self.cdm.create_change_item(user,change_item_comment,Pub.objects.get(citekey=update_data['citekey']),fields=change_item_fields)
                return True
            else:
                return False
        else:
            return None


    def delete_pub(self,user,pub_key):
        """
        Deletes Pub with key pub_key
        :param user: user currently logged into Traitable
        :param pub_key: citation key of the Pub
        :return: True if Pub is deleted, False if not, or None if user does not have proper permissions
        """
        if user.has_perm("pubs.delete_pub"):
            try:
                pub = Pub.rmobjects.get(citekey=pub_key).delete()
                return True
            except:
                return False
        elif user.has_perm("pubs.safe_delete_pub"):
            try:
                pub = Pub.rmobjects.get(citekey=pub_key)
                pub.safe_deleted = True
                pub.save()
                return True
            except:
                return False
        else:
            return None

    def upload_pubs_bibtex(self,user,bibtex_file):
        """
        Uploads Pub records from a bibtex file
        :param user: user currently logged into Traitable
        :param bibtex_file: bibtex file to be uploaded
        :return: success, error tuple of Pub records that were successfully uploaded, or failed, None if user
        does not have proper permission
        """
        pdb.set_trace()
        if user.has_perm("pubs.add_pub"):
            return upload_pubs.upload_bibtex(user,bibtex_file)
        else:
            return None

    def enter_single_pub(self,user,form_data):
        """
        Upload Pub record manually from entery form
        :param user: user currently logged into Traitable
        :param form_data: the form data as a dict
        :return: success, error tuple corresponding to success or failure or None if user does not have proper permission
        """
        if user.has_perm("pubs.add_pub"):
            success = []
            errors = []
            args={}
            try:
                for (citekey,value) in form_data.items():
                    if citekey!='author' and citekey!='editor' and value !='' and value!=None:
                        args[citekey]=value
                    elif citekey!='lastName' and citekey!='firstName' and citekey!= 'middleNme' and citekey!='author' and citekey!='editor' and value!='' and value!=None:
                        args[citekey]=value
                form = PubForm(args)
                if form.is_valid():
                    pub = form.save()
                    pub.save()
                    success.append(pub)
                    change_item_comment = "Created Publication"
                    self.cdm.create_change_item(user, change_item_comment,pub)
                else:
                    print(form.errors)
                    errors.append("Publication was not added successfully. Please check all required fields.")
            except ValidationError as e:
                errors.append(e.messages[0])
            return (success, errors)
        else:
            return None

    def last_pub_query(self,user):
        """
        Returns the last data of the last Pub query
        :param user: user currently logged into Traitable
        :return: the last query or None if user does not have proper permission
        """
        if user.has_perm("pubs.view_pub"):
            return self.current_pub_query
        else:
            return None


    #functions relating to Person model
    def browse_all_persons(self,user):
        """Returns a set of all Persons in the system"""
        pass

    def browse_query_persons(self,user,query_params):
        """Returns a set of all Persons matching query"""
        pass

    def browse_person(self,user,id):
        """Returns Person matching id"""
        pass

    def update_person(self,user,id,request):
        """Updates Person matching id with form data"""
        pass

    def delete_person(self,user,id):
        """Deletes or safe deletes Person matching id"""
        pass