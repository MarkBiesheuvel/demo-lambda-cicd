from arithmetic import add

def lambda_handler(event, context):
    outcome = add(event['a'], event['b'])

    print('Outcome: {}'.format(outcome))

    return {
        'statusCode': 200,
        'body': outcome
    }
