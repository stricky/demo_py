class GeneratorConstants:
    #------------Output Type-----------
    DATA_TYPE_CSV = 'csv'
    DATA_TYPE_JSON = "json"
    DATA_TYPE_TXT = "txt"
    DATA_TYPE_SQL = "sql"
    DATA_TYPE_CQL = "cql"
    DATA_TYPE_FIREBASE = "firebase"
    DATA_TYPE_CUSTOM = "custom"
    DATA_TYPE_XLSX = "xlsx"
    DATA_TYPE_XML = "xml"
    DATA_TYPE_DBUNIT = "dbunit"
    DATA_TYPES = [DATA_TYPE_CSV,
                  DATA_TYPE_JSON,
                  DATA_TYPE_TXT,
                  DATA_TYPE_SQL,
                  DATA_TYPE_CQL,
                  DATA_TYPE_FIREBASE,
                  DATA_TYPE_CUSTOM,
                  DATA_TYPE_XLSX,
                  DATA_TYPE_XML,
                  DATA_TYPE_DBUNIT]

    #------------Line Endings-----------
    LINE_ENDING_WINDOWS = 'windows'
    LINE_ENDING_UNIX = 'unix'
    LINE_ENDINGS = [LINE_ENDING_UNIX,
                    LINE_ENDING_WINDOWS]

    #-----------Data Formats-------------
    DATA_FORMAT_DEF = "%-m/%-d/%Y"
    DATA_FORMAT_1 = "%m/%d/%Y"
    DATA_FORMAT_2 = "%Y-%m-%d"
    DATA_FORMAT_3 = "%-d/%-m/%Y"
    DATA_FORMAT_4 = "%d/%m/%Y"
    DATA_FORMAT_5 = "%-d.%-m.%Y"
    DATA_FORMAT_6 = "%d.%m.%Y"
    DATA_FORMAT_7 = "%d-%b-%Y"
    DATA_FORMAT_8 = "%Y/%m/%d"

    DATA_FORMATS = [DATA_FORMAT_1, DATA_FORMAT_2, DATA_FORMAT_3, DATA_FORMAT_4, DATA_FORMAT_5, DATA_FORMAT_6,
                    DATA_FORMAT_7, DATA_FORMAT_8, DATA_FORMAT_DEF]