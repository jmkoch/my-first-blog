from import_export import resources
from pub.models import Pub
from import_export.admin import ImportExportModelAdmin
from .forms import PubForm
from import_export.fields import Field

headers_to_print = []
#expected_headers = ['id', 'genus', 'species', 'isi', 'fruit_type']

class PubResource(resources.ModelResource):
    full_pub = Field()

    class Meta:
        model = Pub
        fields = ['lastName', 'middleName', 'firstName', 'citekey', 'pub_type']
        export_order = ['lastName', 'middleName', 'firstName', 'citekey', 'pub_type']
        skip_unchanged = True
        report_skipped = True

    def dehydrate_full_pub(self, Pub):
    	return '%s gen %s spec' % (Pub.genus, Pub.species)

# before importing csv, this checks for a blank 'id' col. This adds 'id' col if not present
    def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs): #raise_errors=True
        if 'citekey' not in dataset.headers:
            dataset.insert_col(0, lambda row: "", header='citekey')

        
        print('Here are the columns you will import:' )
        print(dataset.headers)

#        for key in kwargs:
#        	print("another keyword arg: %s: %s:" % (key, kwargs[key]))  # kwargs 
            # get columns in correct order if user imports incorrectly-formatted csv

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.full_clean()  # i is not a trait object yet; so far it's a tuple with whole dataset
        #print('done')
		# add additional cleaning functions in here (for_delete? etc.)

    def export_pubs_csv(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="pubs_output.csv"'

        writer = csv.writer(response)
        writer.writerow(['lastName', 'middleName', 'firstName', 'citekey', 'pub_type'])

        pubs = Pub.objects.all().values_list('lastName', 'middleName', 'firstName', 'citekey', 'pub_type')
	    
        for pub in pubs:
            writer.writerow(pub)

        return response

class PubAdmin(ImportExportModelAdmin):
    list_display = ('lastName', 'middleName', 'firstName', 'citekey', 'pub_type')
    form = PubForm
    resource_class = PubResource
