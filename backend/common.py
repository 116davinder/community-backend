import logging
import uuid

class PostLengthTooLong(Exception):
    pass

def setLoggingFormat(level=20):
    logging.basicConfig(
        format='{ "@timestamp": "%(asctime)s","level": "%(levelname)s","thread": "%(threadName)s","name": "%(name)s","message": "%(message)s" }'
    )
    logging.getLogger().setLevel(level)

def create_post(data):
    logging.info(type(data))
    try:
        _id = uuid.uuid5(uuid.NAMESPACE_DNS, data['title'])
    except:
        _id = uuid.uuid4()
    logging.info(_id)
    return _id

def validate_post(data):
    try:
        _title = data['title']
        _year = data['year']
        _likes = data['likes']
        if len(data) > 3:
            raise PostLengthTooLong
        return True,None
    except PostLengthTooLong as e:
        return False,"Too Long Post Data"
    except:
        return False,"All Fields are not specified"