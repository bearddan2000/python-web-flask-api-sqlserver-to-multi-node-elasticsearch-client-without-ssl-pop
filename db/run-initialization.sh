function do-sql()
{
    local cmd=/opt/mssql-tools/bin/sqlcmd
    local server="localhost"
    local user="sa"
    local password="z!x<?oB1ab"
    local sql_file=$1

    $cmd -S $server -U $user -P $password -i $sql_file
}
# Wait to be sure that SQL Server came up
sleep 90s

# Run the setup script to create the DB and the schema in the DB
# Note: make sure that your password matches what is in the Dockerfile

echo "processing file /usr/src/app/schema.sql"
do-sql /usr/src/app/schema.sql