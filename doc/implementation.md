Entrypoint
- backup (job)
- restore (job)
  - backup_id
    - Required to tell restore _which_ backup needs to be redone
- list
  - job
    - optional. If provided, will only list backup information for this particular job
  - format (see below for formats)
    - yaml
    - json
    - text (default, will be done via tabular data)
- configure (job)
- delete (job)
  - If job is running currently, it is killed and the current partial backup is discarded
  - -y
    - If provided, does not prompt for verification before deleting job
  - all
    - If provided, deletes job _and_ deletes all backups created associated with job
- create
  - source
    - can be file or directory
  - destination
    - must be directory
  - increment
    - Can be any of the following
      - Integer (this is whatever the lowest form of time tracking cron has available. Seconds most likely)
      - Integer followed by specifying character (EG 4D which is 4 days) Note: char is case sensitive
        - Valid chars
          - S (seconds)
          - m (minutes)
          - H (hours)
          - D (days)
          - W (weeks)
          - M (months)
          - Y (years)
  - save
    - should be newest to oldest, split by "-", using the frequency format above. All saves will be kept up to the newest point. Below is an example
      - 1D-1W-1M-1Y
        - This will compress all backups up to the first day and creates a "snapshot" of that backup
        - It will then hold every "1D" snapshot until it hits the next increment which is "1W". 
        - This will keep all backups up to the first one that is 1 day old. All others will be deleted except for the first that is 1 week old. All others will be deleted except for the first that is 1 month old. All others will be delete except for the first that is 1 year old. All others will be deleted
  - exclude
    - directory/files that should be excluded. Can be one string delimited with colons (EG --exclude /dir1:/dir2), or can be included multiple times (EG --exclude /dir1 --exclude /dir2)
  - compress-type
    - default will be tar.gz
      - Also will support zip (maybe rar?)
    - Option None can be provided, this will not compress the incremental snapshots. Not recommended