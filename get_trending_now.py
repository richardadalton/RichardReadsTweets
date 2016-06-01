import json
from auth import get_api

DUB_WOE_ID = 560743
UK_WOE_ID = 23424975

api = get_api()

dub_trends = api.trends_place(DUB_WOE_ID)
uk_trends = api.trends_place(UK_WOE_ID)

print json.dumps(dub_trends, indent=1)
# print json.dumps(uk_trends, indent=1)