#!/usr/bin/env python
from multiprocessing import Pipe
from multiprocessing.connection import Connection
from argparse import ArgumentParser, RawTextHelpFormatter
import textwrap

FORMAT_STRING = "STRING"
FORMAT_JSON = "JSON"

COMPRESS_TYPE_TARGZ = "TAR.GZ"
COMPRESS_TYPE_ZIP = "ZIP"
COMPRESS_TYPE_NONE = None

VERSION = 0.1
#Unsupported currently
#FORMAT_XML = "XML"

def _add_argparser_args(argparser: ArgumentParser):
    '''
    Adds arguements to the provided argparser

    :param argparser:
    :return None:
    :potential_exceptions: Unknown at this time
    '''

    argparser.add_argument('-b', '--backup', metavar="id/name", 
        help='Runs the backup job associated with the provided "job" id or name. To get a job id, run "list" without any parameters')
    argparser.add_argument('-c', '--create', metavar="name",
        help=textwrap.dedent('''
        Creates a new job. Requires the following flags

        --source
            Can be either a file or directory

        --destination
            Must be a directory. If the directory does not exist, it will be created

        --increment
            Can be any of the following
                Integer followed by specifying character (EG 4D which is 4 days) Note: char is case sensitive
                    - Valid chars
                    - S (seconds)
                    - m (minutes)
                    - H (hours)
                    - D (days)
                    - W (weeks)
                    - M (months)
                    - Y (years)

        --save_history
            should be newest to oldest, split by "-", using the frequency format above. All saves will be kept up to the newest point. Below is an example
                1D-1W-1M-1Y
                    - This will compress all backups up to the first day and creates a "snapshot" of that backup
                    - It will then hold every "1D" snapshot until it hits the next increment which is "1W". 
                    - This will keep all backups up to the first one that is 1 day old. All others will be deleted except for the first that is 1 week old. All others will be deleted except for the first that is 1 month old. All others will be delete except for the first that is 1 year old. All others will be deleted


        The following flags are optional
        --compress_type
            Available options
                - tar.gz
                - zip
                - None
                    This will not compress the incremental snapshots. Not recommended
        --exclude
            directory/files that should be excluded. Can be one string delimited with colons (EG --exclude /dir1:/dir2), or can be included multiple times (EG --exclude /dir1 --exclude /dir2)
        ''')
        )
    argparser.add_argument('-d', '--delete', metavar="id/name",
        help=textwrap.dedent('''
        Deletes job associated with the provided "job" id or name. To get a job id, run "list" without any parameters

        Can be used in conjuction with the following optional arguments
        --yes
            If provided, this prevents a prompt for verification of deletion
        --all
            If provided, this will delete the job and all backups. By default this is set to false
        ''')
        )
    argparser.add_argument('-l', '--list', default=False, action="store_true",
        help=textwrap.dedent(
        '''
        Lists all jobs and associated backups with those jobs

        Optional params
            --job
                This can be either the jobs id or name. If provided, this will only list information related directly to this job
            --format
                Sets the return format type for the list command. By default this will be a tabular formatted string to be displayed in the terminal
                Available options
                    - Text
                    - JSON
        ''')
        )
    argparser.add_argument('-o', '--config', metavar="id/name",
        help=textwrap.dedent('''
        Configures any option on a job. Jobs can be provided via their id or name. All options listed in "create" can be modified via configure. For more details, check out --create
        
        Additionally, you can provide the flag --name to set a new unique name for this job

        --create
            Allows override of name of job
        ''')
        )
    argparser.add_argument('-r', '--restore', metavar="restore_id",
        help='Restores the job to an earlier point. To get a list of restore points, checkout --list with your jobs name/id')
    argparser.add_argument('--name', default=None, action="store", help="Used in conjunction with --config")
    argparser.add_argument('--source', default=None, action="store", help="Used in conjunction with --config or --create")
    argparser.add_argument('--destination', default=None, action="store", help="Used in conjunction with --config or --create")
    argparser.add_argument('--increment', default=None, action="store", help="Used in conjunction with --config or --create")
    argparser.add_argument('--save_history', default=None, action="store", help="Used in conjunction with --config or --create")
    argparser.add_argument('--compress_type', default=None, action="store", help="Used in conjunction with --config or --create")
    argparser.add_argument('--exclude', default=[], action='append', help="Used in conjunction with --config or --create")
    argparser.add_argument('--yes', default=False, action="store_true", help="Used in conjunction with --delete")
    argparser.add_argument('--all', default=False, action="store_true", help="Used in conjunction with --delete")
    argparser.add_argument('--job', default='', action="store", help="Used in conjunction with --list")
    argparser.add_argument('--format', default='', action="store", help="Used in conjunction with --list")
    argparser.add_argument('-v', '--verbose', default=False, action="store_true", help="Increases verbosity of program")
    argparser.add_argument('--version', default=False, action="store_true", help="Prints current version")

def backup(job_int: int=-1, job_name: str="") -> Connection:
    '''
    Runs the backup job associated with the provided "job" id or provided "job" name

    :param job_id (optional): id associated with the job to backup. Either this or job_name must be provided. To get this id, run the "list" command
    :param job_name (optional): name of job to backup. Either this or job_id must be provided
    :return Connection: returns the child connection of a pipe that the function creates when it drops to a subprocess to begin the backup process.
    :potential_exceptions: Unknown at this time
    '''
    return None

def restore(job_id: int=-1, job_name: str="", restore_point: int=None) -> Connection:
    '''
    Runs the restore job associated with the provided "job" id

    :param job_id (optional): id associated with the job to restore. Either this or job_name must be provided. To get this id, run the "list" command
    :param job_name (optional): name of job to restore. Either this or job_id must be provided
    :param restore_point: id of the point to restore to. To find available restore points for your job, run "list" with the provided job id/name
    :return Connection: returns the child connection of a pipe that the function creates when it drops to a subprocess to begin the restore process.
    :potential_exceptions: Unknown at this time
    '''
    return None

def list(job_id: int=-1, job_name: str="", format: str=FORMAT_STRING) -> str:
    '''
    Lists all jobs and associated backups with those jobs

    :param job_id (optional): id associated with a specific job to get backups from. To get this id, run the "list" command without an id
    :param job_name (optional): name associated with a specific job to get backups from. 
    :param format (optional): String indicating the desired return format of the information to display. By default this is set to "STRING" which will result in the information being returned in a tabular stream designed for STDOUT
        :Default "STRING":
    :return String: Returns the information from the list command in a formatted string related to the param format. See :param format: for more details
    :potential_exceptions: Unknown at this time
    '''
    return ''

def configure(job_id: int=-1, job_name: str="", **kwargs) -> None:
    '''
    Configures any option on a job. All options listed in "create" can be modified via configure

    :param job_id (optional): id associated with the job to configure. Either this or job_name must be provided. To get this id, run the "list" command
    :param job_name: name associated with the job to configure. Either this or job_id must be provided
    :param kwargs: See :create: for more details on kwargs
    :return None:
    :potential_exceptions: Unknown at this time
    '''
    pass

def delete(job_id: int=-1, job_name: str="", all: bool=False) -> None:
    '''
    Runs the backup job associated with the provided "job" id

    :param job_id (optional): id associated with the job to delete. Either this or job_name must be provided. To get this id, run the "list" command
    :param job_name (optional): name associated with the job to delete. Either this or job_id must be provided.
    :param all (optional): if set to True, tells us to delete both the job and all associated backups with the job. 
        :Default False:
    :return None:
    :potential_exceptions: Unknown at this time
    '''
    pass

def create(
    name: str,
    source: str,
    destination: str,
    increment: str,
    save: str,
    exclude: str = "",
    compress_type: str = COMPRESS_TYPE_TARGZ) -> int:
    '''
    Creates a new job

    :param name: This must be a unique name
    :param source: Can be either a file or directory
    :param destination: Must be a directory. If the directory does not exist, it will be created
    :param increment: Can be any of the following
        Integer followed by specifying character (EG 4D which is 4 days) Note: char is case sensitive
            - Valid chars
            - S (seconds)
            - m (minutes)
            - H (hours)
            - D (days)
            - W (weeks)
            - M (months)
            - Y (years)
    :param save_history: Should be newest to oldest, split by "-", using the frequency format above. All saves will be kept up to the newest point. Below is an example
        1D-1W-1M-1Y
            - This will compress all backups up to the first day and creates a "snapshot" of that backup
            - It will then hold every "1D" snapshot until it hits the next increment which is "1W". 
            - This will keep all backups up to the first one that is 1 day old. All others will be deleted except for the first that is 1 week old. All others will be deleted except for the first that is 1 month old. All others will be delete except for the first that is 1 year old. All others will be deleted
    :param exclude (optional): Locations that should be excluded. Can be string delimited with colons to indicate multiple locations (EG /dir1/:/dir2)
    :param compress_type (optional): Available options
        - tar.gz
        - zip
        - None
            This will not compress the incremental snapshots. Not recommended
        :Default "TAR.GZ":
    :return int: New job's id
    :potential_exceptions: Unknown at this time
    '''
    return -1


argparser = ArgumentParser(description='''
    Timeshot Interface to manage backups and restorations of linux machines
    ''',
    formatter_class=RawTextHelpFormatter)
_add_argparser_args(argparser)

if __name__ == "__main__":
    args = argparser.parse_args()
    pass