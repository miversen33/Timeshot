#!/usr/bin/env python
from multiprocessing import Pipe
from multiprocessing.connection import Connection

FORMAT_STRING = "STRING"
FORMAT_JSON = "JSON"
#Unsupported currently
#FORMAT_XML = "XML"
def backup(job: int) -> Connection:
    '''
    Runs the backup job associated with the provided "job" id

    :param job: id associated with the job to run. To get this id, run the "list" command
    :return Connection: returns the child connection of a pipe that the function creates when it drops to a subprocess to begin the backup process.
    :potential_exceptions: Unknown at this time
    '''
    return None

def restore(job: int, restore_point: int) -> Connection:
    '''
    Runs the restore job associated with the provided "job" id

    :param job: id associated with the job to run. To get this id, run the "list" command
    :return Connection: returns the child connection of a pipe that the function creates when it drops to a subprocess to begin the restore process.
    :potential_exceptions: Unknown at this time
    '''
    return None

def list(job: int=-1, format: str=FORMAT_STRING) -> str:
    '''
    Lists all jobs and associated backups with those jobs

    :param job (optional): id associated with a specific job to get backups from. To get this id, run the "list" command without an id
    :param format (optional): String indicating the desired return format of the information to display. By default this is set to "String" which will result in the information being returned in a tabular stream designed for STDOUT
    :return String: Returns the information from the list command in a formatted string related to the param format. See :param format: for more details
    :potential_exceptions: Unknown at this time
    '''
    return ''

def configure(job: int, **kwargs) -> None:
    '''
    Configures any option on a job.

    :param job: id associated with the job to run. To get this id, run the "list" command
    :param kwargs: PENDING LISTING
    :return None:
    :potential_exceptions: Unknown at this time
    '''
    pass

def delete(job: int) -> None:
    '''
    Runs the backup job associated with the provided "job" id

    :param job: id associated with the job to run. To get this id, run the "list" command
    :return None:
    :potential_exceptions: Unknown at this time
    '''
    pass

def create(**kwargs) -> int:
    '''
    Creates a new job

    :param kwargs: PENDING LISTING
    :return int: New job's id
    :potential_exceptions: Unknown at this time
    '''
    return -1

if __name__ == "__main__":
    pass