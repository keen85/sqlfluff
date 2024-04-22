r"""A list of all SQL key words.

https://docs.microsoft.com/en-us/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-ver16

Run the script in a browser console to extract all reserved keywords:

```js
(function () {
    const xpathResult = document.evaluate(
        '//div[@class=\'column\']/p[not(descendant::strong)]',
        document,
        null,
        XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
        null
    );
    const list = new Set();

    for (let index = 0; index < xpathResult.snapshotLength; ++index) {
        const node = xpathResult.snapshotItem(index);
        list.add(node.textContent.trim());
    }
    console.log([...list].sort().map(value => `    "${value}"`).join(',\n'));
})();
```

Be careful, some keywords are present in `UNRESERVED_KEYWORDS`.
"""

RESERVED_KEYWORDS = [
    "ADD",
    "ALL",
    "ALTER",
    "AND",
    "ANY",
    "APPEND",
    "AS",
    "ASC",
    "AUTHORIZATION",
    "BACKUP",
    "BATCHSIZE",
    "BEGIN",
    "BETWEEN",
    "BREAK",
    "BROWSE",
    "BULK",
    "BY",
    "CASCADE",
    "CASE",
    "CHECK",
    "CHECKPOINT",
    "CHECK_CONSTRAINTS",
    "CLOSE",
    "CLUSTERED",
    "COALESCE",
    "COLLATE",
    "COLUMN",
    "COMMIT",
    "COMPUTE",
    "CONSTRAINT",
    "CONTAINS",
    "CONTAINSTABLE",
    "CONTINUE",
    "CONVERT",
    "CREATE",
    "CROSS",
    "CURRENT",
    "CURRENT_CATALOG",  # *future*
    "CURRENT_DATE",
    "CURRENT_DEFAULT_TRANSFORM_GROUP",  # *future*
    "CURRENT_PATH",  # *future*
    "CURRENT_ROLE",  # *future*
    "CURRENT_SCHEMA",  # *future*
    "CURRENT_TIME",
    "CURRENT_TIMESTAMP",
    "CURRENT_TRANSFORM_GROUP_FOR_TYPE",  # *future*
    "CURRENT_USER",
    "CURSOR",
    "DATABASE",
    "DBCC",
    "DEALLOCATE",
    "DECLARE",
    "DEFAULT",
    "DELETE",
    "DENY",
    "DESC",
    "DISTINCT",
    "DISTRIBUTED",
    "DOUBLE",
    "DROP",
    "DYNAMIC",
    "ELSE",
    "END",
    "ERRLVL",
    "ESCAPE",
    "EXCEPT",
    "EXEC",
    "EXECUTE",
    "EXISTS",
    "EXIT",
    "EXTERNAL",
    "FAST_FORWARD",
    "FETCH",
    "FILE",
    "FILLFACTOR",
    "FOR",
    "FORWARD_ONLY",
    "FOREIGN",
    "FREETEXT",
    "FREETEXTTABLE",
    "FROM",
    "FULL",
    "FULLSCAN",
    "FUNCTION",
    "GLOBAL",
    "GO",
    "GOTO",
    "GRANT",
    "GROUP",
    "HAVING",
    "HOLDLOCK",
    "IDENTITY_INSERT",
    "IDENTITY",
    "IDENTITYCOL",
    "IF",
    "IN",
    "INDEX",
    "INNER",
    "INSERT",
    "INTERSECT",
    "INTO",
    "IS",
    "JOIN",
    "KEY",
    "KEYSET",
    "KILL",
    "LEFT",
    "LIKE",
    "LINENO",
    "LIST",
    "LOCAL",
    "MERGE",
    "NATIONAL",
    "NATIVE_COMPILATION",
    "NOCHECK",
    "NONCLUSTERED",
    "NOT",
    "NULL",
    "NULLIF",
    "OF",
    "OFF",
    "OFFSETS",
    "ON",
    "OPEN",
    "OPENDATASOURCE",
    "OPENQUERY",
    "OPENROWSET",
    "OPENXML",
    "OPTIMISTIC",
    "OPTION",
    "OR",
    "ORDER",
    "OUTER",
    "OVER",
    "OVERLAY",  # *future*
    "PERCENT",
    "PIVOT",
    "PLAN",
    "PRIMARY",
    "PRINT",
    "PROC",
    "PROCEDURE",
    "PUBLIC",
    "RAISERROR",
    "READ",
    "READ_ONLY",
    "READTEXT",
    "RECONFIGURE",
    "REFERENCES",
    "REPLICATION",
    "RESAMPLE",
    "RESTORE",
    "RESTRICT",
    "RETURN",
    "REVERT",
    "REVOKE",
    "RIGHT",
    "ROLLBACK",
    "ROWCOUNT",
    "ROWGUIDCOL",
    "RULE",
    "SAVE",
    "SCHEMA",
    "SCROLL",
    "SCROLL_LOCKS",
    "SELECT",
    "SEMANTICKEYPHRASETABLE",
    "SEMANTICSIMILARITYDETAILSTABLE",
    "SEMANTICSIMILARITYTABLE",
    "SESSION_USER",
    "SET",
    "SETUSER",
    "SHUTDOWN",
    "SOME",
    "STATIC",
    "STATISTICS",
    "SYSTEM_USER",
    "TABLE",
    "TABLESAMPLE",
    "TEXTSIZE",
    "THEN",
    "TO",
    "TOP",
    "TRAN",
    "TRANSACTION",
    "TRAN",
    "TRIGGER",
    "TRUNCATE",
    "TRY_CONVERT",
    "TSEQUAL",
    "TYPE_WARNING",
    "UNION",
    "UNIQUE",
    "UNPIVOT",
    "UPDATE",
    "UPDATETEXT",
    "USE",
    "USER",
    "VALUES",
    "VARYING",
    "VIEW",
    "WAITFOR",
    "WHEN",
    "WHERE",
    "WHILE",
    "WITH",
    "WRITETEXT",
]

# Future reserved keywords extracted from the documentation
FUTURE_RESERVED_KEYWORDS = [
    "ALIAS",
    "ARRAY",
    "CLASS",
    "DESTROY",
    "END-EXEC",
    "EVERY",
    "LIKE_REGEX",
]

UNRESERVED_KEYWORDS = [
    "ABORT",
    "ABORT_AFTER_WAIT",
    "ABSENT",
    "ACTION",
    "ATOMIC",
    "AFTER",
    "ALGORITHM",
    "ALLOWED",
    "ALLOW_PAGE_LOCKS",
    "ALLOW_ROW_LOCKS",
    "ALWAYS",
    "ANSI_DEFAULTS",
    "ANSI_NULL_DFLT_OFF",
    "ANSI_NULL_DFLT_ON",
    "ANSI_NULLS",
    "ANSI_PADDING",
    "ANSI_WARNINGS",
    "APPEND_ONLY",
    "APPLY",
    "ARITHABORT",
    "ARITHIGNORE",
    "AT",
    "AUTO_CREATE_TABLE",
    "AUTO",
    "BEFORE",  # *future*
    "BERNOULLI",
    "BINARY",
    "BLOCKERS",
    "BREAK",
    "CACHE",
    "CALLED",
    "CALLER",
    "CAST",
    "CATCH",
    "CHANGE_TRACKING",
    "CODEPAGE",
    "COLUMN_ENCRYPTION_KEY",
    "COLUMNSTORE_ARCHIVE",
    "COLUMNSTORE",
    "COMMITTED",
    "COMPRESS_ALL_ROW_GROUPS",
    "COMPRESSION_DELAY",
    "COMPRESSION",
    "CONCAT_NULL_YIELDS_NULL",
    "CONCAT",
    "CONNECTION_OPTIONS",
    "CONTAINED",
    "CONTINUE",
    "CONTROL",
    "CREDENTIAL",
    "COPY",
    "CURSOR_CLOSE_ON_COMMIT",
    "CYCLE",
    "DATA_COMPRESSION",
    "DATA_CONSISTENCY_CHECK",
    "DATA_DELETION",
    "DATA_SOURCE",
    "DATA",
    "DATAFILETYPE",
    "DATASOURCE",
    "DATE_FORMAT",
    "DATE",
    "DATEFIRST",
    "DATEFORMAT",
    "DAY",
    "DAYS",
    "DEADLOCK_PRIORITY",
    "DELAY",
    "DELAYED_DURABILITY",
    "DELIMITEDTEXT",
    "DELTA",
    "DENSE_RANK",
    "DETERMINISTIC",
    "DISABLE",
    "DISK",  # listed as reserved but functionally unreserved
    "DISTRIBUTION",  # Azure Synapse Analytics specific
    "DROP_EXISTING",
    "DUMP",  # listed as reserved but functionally unreserved
    "DURABILITY",
    "ELEMENT",  # *future*
    "ELEMENTS",
    "ENCODING",
    "ENCRYPTED",
    "ENCRYPTION_TYPE",
    "ENCRYPTION",
    "ERRORFILE_CREDENTIAL",
    "ERRORFILE_DATA_SOURCE",
    "ERRORFILE",
    "EXPAND",
    "EXPLAIN",  # Azure Synapse Analytics specific
    "EXPLICIT",
    "EXTERNALPUSHDOWN",
    "FAST",
    "FIELD_TERMINATOR",
    "FIELDQUOTE",
    "FIELDTERMINATOR",
    "FILE_FORMAT",
    "FILEGROUP",
    "FILESTREAM",
    "FILESTREAM_ON",
    "FILESTREAM",
    "FILE_TYPE",
    "FILETABLE_COLLATE_FILENAME",
    "FILETABLE_DIRECTORY",
    "FILETABLE_FULLPATH_UNIQUE_CONSTRAINT_NAME",
    "FILETABLE_PRIMARY_KEY_CONSTRAINT_NAME",
    "FILETABLE_STREAMID_UNIQUE_CONSTRAINT_NAME",
    "FILTER_COLUMN",
    "FILTER_PREDICATE",
    "FILTER",
    "FIPS_FLAGGER",
    "FIRE_TRIGGERS",
    "FIRST_ROW",
    "FIRST",
    "FIRSTROW",
    "FMTONLY",
    "FOLLOWING",
    "FORCE",
    "FORCED",
    "FORCEPLAN",
    "FORCESCAN",
    "FORCESEEK",
    "FORMAT_OPTIONS",
    "FORMAT_TYPE",
    "FORMAT",
    "FORMATFILE_DATA_SOURCE",
    "FORMATFILE",
    "FULLTEXT",
    "GENERATED",
    "HASH",
    "HEAP",  # Azure Synapse Analytics specific
    "HIDDEN",
    "HIGH",
    "HINT",
    "HISTORY_RETENTION_PERIOD",
    "HISTORY_TABLE",
    "IGNORE_CONSTRAINTS",
    "IGNORE_DUP_KEY",
    "IGNORE_NONCLUSTERED_COLUMNSTORE_INDEX",
    "IGNORE_TRIGGERS",
    "IGNORE",
    "IMPLICIT_TRANSACTIONS",
    "INBOUND",
    "INCLUDE_NULL_VALUES",
    "INCLUDE",
    "INCREMENT",
    "INFINITE",
    "INLINE",
    "INSTEAD",
    "INTERVAL",
    "IO",
    "ISOLATION",
    "JSON",
    "KEEP",
    "KEEPDEFAULTS",
    "KEEPFIXED",
    "KEEPIDENTITY",
    "KEEPNULLS",
    "KILOBYTES_PER_BATCH",
    "LABEL",  # *reserved* keyword in Azure Synapse; but would break TSQL parsing
    "LANGUAGE",
    "LAST",
    "LASTROW",
    "LEDGER",
    "LEDGER_VIEW",
    "LEGACY_CARDINALITY_ESTIMATION",
    "LEVEL",
    "LOAD",  # listed as reserved but functionally unreserved
    "LOB_COMPACTION",
    "LOCATION",
    "LOCK_TIMEOUT",
    "LOG",
    "LOGIN",
    "LOOP",
    "LOW",
    "MASTER",
    "MANUAL",
    "MASKED",
    "MATCHED",
    "MAX_DURATION",
    "MAX_GRANT_PERCENT",
    "MAX",
    "MAXDOP",
    "MAXERRORS",
    "MAXRECURSION",
    "MAXVALUE",
    "MEMORY_OPTIMIZED",
    "MIGRATION_STATE",
    "MIN_GRANT_PERCENT",
    "MINUTES",
    "MINVALUE",
    "MONTH",
    "MONTHS",
    "NAME",
    "NEXT",
    "NO_PERFORMANCE_SPOOL",
    "NO",
    "NOCOUNT",
    "NOEXEC",
    "NOEXPAND",
    "NOLOCK",
    "NONE",
    "NORMAL",
    "NOWAIT",
    "NTILE",
    "NUMERIC_ROUNDABORT",
    "OBJECT",
    "OFFSET",
    "ONLINE",
    "OPENJSON",
    "OPERATION_TYPE_COLUMN_NAME",
    "OPERATION_TYPE_DESC_COLUMN_NAME",
    "OPTIMIZE_FOR_SEQUENTIAL_KEY",
    "OPTIMIZE",
    "ORC",
    "OUT",
    "OUTBOUND",
    "OUTPUT",
    "OVERRIDE",
    "OWNER",
    "PAD_INDEX",
    "PAGE",
    "PAGLOCK",
    "PARAMETER",
    "PARAMETERS",  # *future*
    "PARAMETERIZATION",
    "PARQUET",
    "PARSEONLY",
    "PARSER_VERSION",
    "PARTIAL",  # *future*
    "PARTITION",
    "PARTITIONS",
    "PASSWORD",
    "PATH",
    "PAUSE",
    "PAUSED",
    "PERCENTAGE",
    "PERCENTILE_CONT",
    "PERCENTILE_DISC",
    "PERIOD",
    "PERSISTED",
    "POPULATION",
    "PRECEDING",
    "PRECISION",  # listed as reserved but functionally unreserved
    "PRIOR",
    "PROFILE",
    "PROPERTY",
    "PUSHDOWN",
    "QUERY_GOVERNOR_COST_LIMIT",
    "QUERYTRACEON",
    "QUOTED_IDENTIFIER",
    "R",  # sqlcmd command
    "RANDOMIZED",
    "RANGE",
    "RANK",
    "RAW",
    "RCFILE",
    "READCOMMITTED",
    "READCOMMITTEDLOCK",
    "READONLY",
    "READPAST",
    "READUNCOMMITTED",
    "REBUILD",
    "RECEIVE",
    "RECOMPILE",
    "RECURSIVE",
    "REGENERATE",
    "REGR_AVGX",  # *future*
    "REGR_AVGY",  # *future*
    "REGR_COUNT",  # *future*
    "REGR_INTERCEPT",  # *future*
    "REGR_R2",  # *future*
    "REGR_SLOPE",  # *future*
    "REGR_SXX",  # *future*
    "REGR_SXY",  # *future*
    "REGR_SYY",  # *future*
    "REJECTED_ROW_LOCATION",
    "REJECT_SAMPLE_VALUE",
    "REJECT_TYPE",
    "REJECT_VALUE",
    "REMOTE_DATA_ARCHIVE",
    "REMOTE_PROC_TRANSACTIONS",
    "RENAME",  # Azure Synapse Analytics specific
    "REORGANIZE",
    "REPEATABLE",
    "REPEATABLEREAD",
    "REPLACE",
    "REPLICATE",  # Azure Synapse Analytics
    "RESPECT",
    "RESULT_SET_CACHING",  # Azure Synapse Analytics specific
    "RESUMABLE",
    "RESUME",
    "RETENTION_PERIOD",
    "RETURNS",
    "ROBUST",
    "ROLE",
    "ROOT",
    "ROUND_ROBIN",  # Azure Synapse Analytics specific
    "ROW_NUMBER",
    "ROW",
    "ROWGUIDCOL",
    "ROWLOCK",
    "ROWS_PER_BATCH",
    "ROWS",
    "ROWTERMINATOR",
    "S",
    "SCALEOUTEXECUTION",
    "SCHEMA_AND_DATA",
    "SCHEMA_ONLY",
    "SCHEMABINDING",
    "SCHEME",
    "SCOPED",
    "SEARCH",
    "SECRET",
    "SECURITYAUDIT",  # listed as reserved but functionally unreserved
    "SELF",
    "SEQUENCE_NUMBER_COLUMN_NAME",
    "SEQUENCE_NUMBER",
    "SEQUENCE",
    "SERDE_METHOD",
    "SERIALIZABLE",
    "SERVER",
    "SERVICE",
    "SETERROR",
    "SETVAR",  # sqlcmd command
    "SHOWPLAN_ALL",
    "SHOWPLAN_TEXT",
    "SHOWPLAN_XML",
    "SINGLE_BLOB",
    "SINGLE_CLOB",
    "SINGLE_NCLOB",
    "SNAPSHOT",
    "SORT_IN_TEMPDB",
    "SOURCE",
    "SPARSE",
    "SPATIAL_WINDOW_MAX_CELLS",
    "SPLIT",
    "START",
    "STATISTICAL_SEMANTICS",
    "STATISTICS_INCREMENTAL",
    "STATISTICS_NORECOMPUTE",
    "STOPLIST",
    "STRING_AGG",
    "STRING_DELIMITER",
    "SWITCH",
    "SYNONYM",
    "SYSTEM_TIME",
    "SYSTEM_VERSIONING",
    "SYSTEM",
    "TABLOCK",
    "TABLOCKX",
    "TAKE",
    "TARGET",
    "TEXTIMAGE_ON",
    "THROW",
    "TIES",
    "TIME",
    "TIMEOUT",
    "TIMESTAMP",
    "TRANSACTION_ID_COLUMN_NAME",
    "TRANSACTION_ID",
    "TRUNCATE_TARGET",  # Azure Synapse Analytics specific
    "TRY",
    "TYPE",
    "UNBOUNDED",
    "UNCOMMITTED",
    "UNKNOWN",
    "UPDLOCK",
    "USE_TYPE_DEFAULT",
    "USED",
    "USER_DB",  # Azure Synapse Analytics specific, deprecated
    "USING",
    "VALUE",
    "VIEW_METADATA",
    "WAIT_AT_LOW_PRIORITY",
    "WAITFOR",
    "WEEK",
    "WEEKS",
    "WHILE",
    "WITHIN",
    "WITHOUT_ARRAY_WRAPPER",
    "WORK",
    "XACT_ABORT",
    "XLOCK",
    "XML",
    "XMLAGG",  # *future*
    "XMLATTRIBUTES",  # *future*
    "XMLBINARY",  # *future*
    "XMLCAST",  # *future*
    "XMLCOMMENT",  # *future*
    "XMLCONCAT",  # *future*
    "XMLDATA",
    "XMLDOCUMENT",  # *future*
    "XMLELEMENT",  # *future*
    "XMLEXISTS",  # *future*
    "XMLFOREST",  # *future*
    "XMLITERATE",  # *future*
    "XMLNAMESPACES",  # *future*
    "XMLPARSE",  # *future*
    "XMLPI",  # *future*
    "XMLQUERY",  # *future*
    "XMLSCHEMA",
    "XMLSERIALIZE",  # *future*
    "XMLTABLE",  # *future*
    "XMLTEXT",  # *future*
    "XMLVALIDATE",  # *future*
    "XML_COMPRESSION",
    "XSINIL",
    "YEAR",
    "YEARS",
    "ZONE",
]
