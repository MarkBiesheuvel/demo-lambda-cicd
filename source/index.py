from arithmetic import add, multiply


def lambda_handler(event, context):
    parameters = event.get('queryStringParameters', {})

    a = int(parameters.get('a', 0))
    b = int(parameters.get('b', 0))

    total = multiply(a, b)

    print('A: {}'.format(a))
    print('B: {}'.format(b))
    print('Total: {}'.format(total))

    return {
        'statusCode': 200,
        'headers': {
            'operation': 'add'
        },
        'body': total
    }
