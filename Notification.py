from pusher_push_notifications import PushNotifications

beams_client = PushNotifications(
    instance_id='a2b45528-bf46-4dc4-8b15-c6930a5b5fa5',
    secret_key='72B1AE3571C1F2B9CE0FDA000CFBBDB8D9F00D5D8635D01EFFA8FC5C435D41F3',
)


response = beams_client.publish_to_interests(
    interests=['hello'],
    publish_body={
        'apns': {
            'aps': {
                'alert': 'Hello!'
            }
        },
        'fcm': {
            'notification': {
                'title': 'Car Alarm',
                'body': 'Unknown login!!!'
            }
        }
    }
)

print(response['publishId'])

