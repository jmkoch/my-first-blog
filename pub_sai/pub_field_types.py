# publication types
ARTICLE = 'article'
BOOK = 'book'
INBOOK = 'inbook'
INCOLLECTION = 'incollection'
INPROCEEDING = 'inproceeding'
MANUAL = 'manual'
MASTERTHESIS = 'masterthesis'
MISC = 'misc'
PHDTHESIS = 'phdthesis'
PROCEEDINGS = 'proceedings'
TECHREPORT = 'techreport'
UNPUBLISHED = 'unpublished '

# field types
ADDRESS = 'address'
ANNOTATE = 'annotate'
#AUTHOR = 'author'
LASTNAME = 'lastName'
MIDDLENAME = 'middleName'
FIRSTNAME = 'firstName'
BOOKTITLE = 'booktitle'
CHAPTER = 'chapter'
CROSSREF = 'crossref'
EDITION = 'edition'
EDITOR = 'editor'
HOWPUBLISHED = 'howpublished'
INSTITUTION = 'institution'
JOURNAL = 'journal'
CITEKEY = 'citekey'
MONTH = 'month'
NOTE = 'note'
NUMBER = 'number'
ORGANIZATION = 'organization'
PAGES = 'pages'
PUBLISHER = 'publisher'
SCHOOL = 'school'
SERIES = 'series'
TITLE = 'title'
TYPE = 'type'
VOLUME = 'volume'
YEAR = 'year'


ABSTRACT = 'abstract'
DOI = 'doi'
KEYWORDS = 'keywords'
URL = 'url'

# pub type fields structure
# pub_type: [[required_fields],[optional_fields]]
PUB_TYPE_FIELDS = {
    ARTICLE: [[TITLE,JOURNAL,YEAR],[VOLUME,NUMBER,PAGES,MONTH,NOTE]],
    BOOK: [[TITLE,PUBLISHER,YEAR],[(VOLUME,NUMBER),SERIES,ADDRESS,EDITION,MONTH,NOTE]],
    INBOOK: [[TITLE,(CHAPTER,PAGES),PUBLISHER,YEAR],[(VOLUME,NUMBER),SERIES,ADDRESS,EDITION,MONTH,NOTE]],
    #INCOLLECTION: [[TITLE,BOOKTITLE,PUBLISHER,YEAR],[(VOLUME,NUMBER),SERIES,CHAPTER,PAGES,ADDRESS,EDITION,MONTH,NOTE]],
    #INPROCEEDING: [[],[]],
    MANUAL: [[TITLE],[ORGANIZATION,ADDRESS,EDITION,MONTH,YEAR,NOTE]],
    #MASTERTHESIS: [[],[]],
    MISC: [[],[TITLE,HOWPUBLISHED,MONTH,YEAR,NOTE]],
    #PHDTHESIS: [[TITLE,SCHOOL,YEAR],[ADDRESS,MONTH,NOTE]],
    #PROCEEDINGS: [[],[]],
    #TECHREPORT: [[],[]],
    UNPUBLISHED: [[TITLE,NOTE],[MONTH,YEAR]]
}

def get_field_types():
    return PUB_TYPE_FIELDS