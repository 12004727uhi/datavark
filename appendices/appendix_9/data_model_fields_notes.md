# Additional notes for the data model fields as defined in the models.py file of the ie app.  

The fields were defined to store the entities extracted from the incoming data. These entities represented the NER class types (labels) of interest for this project; namely:

- Type(s) associated with the observation (obs_types field)
- Associated colour(s) (obs_colors field)
- Associated location(s) (obs_locs field)
- Associated dates (obs_dates field)
- Associated times (obs_times field)  

Also included were fields indicating timestamps for the record creation (record_created); record last modification (last_mod); the name of the original data source (source_name); and the source URL of the original data (source_url).  

The `record_created` and `last_mod` fields of the Report model contained the Boolean parameters ‘auto_add_now’ and ‘auto_now’, respectively. These ensured that the fields were automatically updated with correct timestamp when a record was added or modified.  

All fields of the Loc, Date, Time, Color and Type models were defined with a unique constraint, meaning that the values were not duplicated with the tables – which would be unnecessary, since each value may be assigned as a relation to multiple records in the Report table.  

In addition, a unique constraint was applied to the `source_url` field, to prevent the same source being duplicated in the database.
