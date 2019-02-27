
from django.shortcuts import render
from scripts import upload_pubs
from django.template.context_processors import csrf
import sys,os
import time
from pub.models import Pub
from django.contrib.auth.models import User
from pub.PubDataManager import PubDataManager
from pub.forms import *
from django.forms.models import model_to_dict
from django.core.files.storage import FileSystemStorage
from pub.pub_field_types import get_field_types


# Create your views here.

pub_data_manager = PubDataManager()

#views for browsing Publications
def browse_pubs(request):
    """
    Returns all the Pub records (publications)
    :param request: incoming HTTP request
    :return: HTTP response with all the Pub records
    """
    args = {}
    pubs,_ = pub_data_manager.browse_query_pubs(request.user,{},None)
    search_form = PubSearchForm()
    args['pubs']=pubs
    args['search_form']=search_form
    return render(request, 'browse_pubs.html',args)

def browse_query_pubs(request):
    info_list = []; success_list=[]; warning_list=[];danger_list=[]
    args = {'info_alerts':info_list, 'success_alerts':success_list,'warning_alerts':warning_list,'danger_alerts':danger_list}
    query_params = {}
    fields = [f.name for f in Pub._meta.get_fields()]
    for field in request.POST.citekeys():
        try:
            if field in request.POST and field in fields :
                if request.POST[field]!='' and request.POST[field]!=None:
                    query_params[field]=request.POST[field]
        except:
            continue
    query_data, query_params = pub_data_manager.browse_query_pubs(request.user,query_params,request.POST['match_type'])
    search_form = PubSearchForm()
    args['search_form']=search_form
    args['pubs'] = query_data
    args['query_params'] = query_params
    return render(request,'browse_pubs.html',args)

def browse_single(request,citekey):
    """
    Returns specific information regarding a single publication given citation key
    :param request: incoming HTTP response
    :param key: ciation key (unique to each Pub)
    :return: HTTP respose with the Pub record
    """
    args = {}
    pub = pub_data_manager.browse_single_pub(request.user,citekey)
    args['pub']=pub
    return render(request, 'pub_detail2.html',args)


#views for editing/deleting
def pub_update(request,citekey):
    """
    Updates a Pub
    :param request: incoming HTTP request
    :param key: citation key of the Pub record to be updated
    :return: HTTP response with the updated pub or HTTP response indicating failure
    """
    info_alerts =[]; success_alerts=[]; warning_alerts = []; danger_alerts=[];
    args = {'info_alerts': info_alerts, 'success_alerts': success_alerts, 'warning_alerts': warning_alerts,'danger_alerts': danger_alerts}
    pub = pub_data_manager.browse_single_pub(request.user, citekey)
    if request.POST:
        success = pub_data_manager.update_pub(request.user,citekey,request.POST)
        if success:
            success_alerts.append(citekey + " successfully updated.")
        else:
            danger_alerts.append(citekey + " was not successfully updated.")
        args['pub'] = pub
        return render(request,'pub_detail2.html',args)
    else:
        form = PubUpdateForm(initial=model_to_dict(pub))
        args['form'] = form
        args['pub'] = pub
        return render(request, 'pub_update2.html',args)

def pub_delete(request,citekey):
    """
    Deletes a Pub record with citation key key
    :param request: incoming HTTP response
    :param key: citation key of Pub to be deleted
    :return: HTTP response indicating success or failure
    """
    info_alerts =[]; success_alerts=[]; warning_alerts = []; danger_alerts=[];
    args = {'info_alerts':info_alerts, 'success_alerts':success_alerts,'warning_alerts':warning_alerts,'danger_alerts':danger_alerts}
    args['pub'] = pub_data_manager.browse_single_pub(request.user,citekey)
    if request.POST:
        success = pub_data_manager.delete_pub(request.user,citekey)
        if success:
            success_alerts.append(citekey + " successfully deleted. It no longer exists in the system.")
        else:
            danger_alerts.append(citekey + " was not deleted. It still exists in the system.")
    args.update(csrf(request))
    return render(request, 'delete_pub.html',args)


#Views for adding Publications
def upload_bfile(request):
    """
    Uploads and inserts Pub records specified by publication entries in a bibtex file
    :param request: incoming HTTP request
    :return: HTTP response indicating success or failure
    """
    """Uploads and inserts the publications in a given bibtex into the database"""
    info_alerts =[]; success_alerts=[]; warning_alerts = []; danger_alerts=[];
    args = {'info_alerts':info_alerts, 'success_alerts':success_alerts,'warning_alerts':warning_alerts,'danger_alerts':danger_alerts}
    form = BibtexForm()
    #Handle POST
    if request.POST:
        form = BibtexForm(request.POST, request.FILES)
        if form.is_valid():
            bibfile = request.FILES['file_name']
            fs = FileSystemStorage()
            bib_filename = fs.save(bibfile.name,bibfile)
            (success,errors) = pub_data_manager.upload_pubs_bibtex(request.user,fs.path(bib_filename) )
            args['success']=success
            args['success_count']=len(success)
            args['errors']=errors
            args['errors_count']=len(errors)
            success_alerts.append(str(len(success))+" publications uploaded successfully.")
            danger_alerts.append(str(len(errors))+" publications upload failed.")
        else:
            danger_alerts.append("File path not found.")
            
    args['form']=form
    args.update(csrf(request))
    return render(request, 'upload_bibtex.html',args)

def enter_single_publication(request):
    """
    Inserts a single publication into the database
    :param request: incoming HTTP request
    :return: HTTP response with info regarding success or failure
    """
    """Inserts a single publication into the database"""
    info_alerts =[]; success_alerts=[]; warning_alerts = []; danger_alerts=[];
    args = {'info_alerts':info_alerts, 'success_alerts':success_alerts,'warning_alerts':warning_alerts,'danger_alerts':danger_alerts}

    if request.POST:
        success = []
        errors = []
        (success,errors) = pub_data_manager.enter_single_pub(request.user,request.POST)
        args['success']=success
        args['success_count']=len(success)
        args['errors']=errors
        args['errors_count']=len(errors)
        if len(success)>0:
            success_alerts.append("Publication entry was successful.")
        else:
            danger_alerts.append("Publication entry failed. Please check required fields.")

    form = PubForm()
    args['form']=form
    args['fields']= get_field_types()
    return render(request,'upload_single_pub2.html',args)
