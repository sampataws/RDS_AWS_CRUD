from com.sampat.aws.rds.client_factory import RDSClient
from com.sampat.aws.rds.rds import RDS


def get_rds():
    rds_client = RDSClient().get_client()
    rds = RDS(rds_client)
    return rds


def deploy_resources():
    rds_client = RDSClient().get_client()
    rds = RDS(rds_client)

    rds.create_postgresql_instance()

    print("Creating RDS PostgreSQL Instance...")


def describe_my_instances():
    print(str(get_rds().describe_instances()))


def modify_master_password():
    get_rds().modify_master_user_password('mypostgresdb', 'mybrandnewpassword')


def take_backup():
    tags = [{'Key': 'Name', 'Value': 'MyFirstSnapshot'}]
    get_rds().take_backup_of_db_instance('mypostgresdb', 'myveryfirstsnaphot', tags)


def restore_db():
    get_rds().restore_db_from_backup('mypostgresdbfromsnapshot', 'rds:mypostgresdb-2018-07-07-12-47')


def delete_db():
    get_rds().delete_db('mypostgresdbfromsnapshot')

def get_db_tables_snapshot():
    get_rds().export_rds_table_to_s3()


if __name__ == '__main__':

    print(get_db_tables_snapshot())
    #deploy_resources()
    # describe_my_instances()
    # modify_master_password()
    # take_backup()
    # restore_db()
    # delete_db()
