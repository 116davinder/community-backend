import logging
import uuid

class PostLengthTooLong(Exception):
    pass

def setLoggingFormat(level=20):
    logging.basicConfig(
        format='{ "@timestamp": "%(asctime)s","level": "%(levelname)s","thread": "%(threadName)s","name": "%(name)s","message": "%(message)s" }'
    )
    logging.getLogger().setLevel(level)

def create_post(table,data):
    logging.info(type(data))
    try:
        _id = uuid.uuid5(uuid.NAMESPACE_DNS, data['title'])
    except:
        _id = uuid.uuid4()
    
    _dict = {
        "id": _id,
        "title": data['title'],
        "description" : data['description'],
        "year": data['year'],
        "likes": data['likes']
    }

    table.append(_dict)

    logging.info(_id)
    return _id

def validate_post(data):
    """
    It will validate the content and size of post data.
    """
    try:
        _title = data['title']
        _description = data['description']
        _year = data['year']
        _likes = data['likes']
        if len(data) > 4:
            raise PostLengthTooLong
        return True,None
    except PostLengthTooLong as e:
        return False,"Too Long Post Data"
    except:
        return False,"All Fields are not specified"