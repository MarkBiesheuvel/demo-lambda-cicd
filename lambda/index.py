import dice

def lambda_handler(event, context):
    outcome = dice.throw()

    print('Outcome: {}'.format(outcome))

    return {
        'statusCode': 200,
        'body': outcome
    }
